"""Player map with fog of war: reveals only the map areas the character has discovered.

Examples:
    python Scripts/fogmap.py --campaign Randuvil --map Scenarios/Crypt/Maps/MapCrypt.svg --reveal 1 2
    python Scripts/fogmap.py --campaign Randuvil --map Scenarios/Crypt/Maps/MapCrypt.svg --secret plyta
    python Scripts/fogmap.py --campaign Randuvil --map Scenarios/Crypt/Maps/MapCrypt.svg --list
    python Scripts/fogmap.py --campaign Randuvil --map Scenarios/Crypt/Maps/MapCrypt.svg --open

Next to the SVG map there must be an areas file with the same name and the
extension .areas.json (e.g. MapCrypt.areas.json). It describes the areas to
reveal, the secrets and the GM-only elements (format: see AGENTS.md, Mapy).

The discovery state is saved in the campaign folder in <name>Map.json, and
the player map in <name>Map.svg together with a self-refreshing preview
<name>Map.html. The name defaults to the name of the scenario or setting
folder whose Maps subfolder holds the map (e.g. Crypt).
"""

import argparse
import copy
import json
import sys
import webbrowser
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

from gm import campaign_folder

ROOT = Path(__file__).resolve().parent.parent
SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")

HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
  html, body {{ margin: 0; height: 100%; background: #f4f1ea; }}
  body {{ display: flex; align-items: center; justify-content: center; }}
  img {{ max-width: 100vw; max-height: 100vh; box-shadow: 0 0 24px rgba(0, 0, 0, .25); background: #fff; }}
</style>
</head>
<body>
<img id="map" src="{svg}" alt="{title}">
<script>
  // The map reloads every 2 seconds, so revealed areas appear by themselves.
  setInterval(function () {{
    var img = new Image();
    img.onload = function () {{ document.getElementById("map").src = img.src; }};
    img.src = "{svg}?t=" + Date.now();
  }}, 2000);
</script>
</body>
</html>
"""


def load_json(path, default=None):
    if not path.exists():
        if default is not None:
            return default
        sys.exit(f"Error: missing file {path}.")
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def check_ids(given, known, kind):
    bad = [g for g in given if g not in known]
    if bad:
        sys.exit(f"Error: unknown {kind}: {', '.join(bad)}. Available: {', '.join(known)}.")


def remove_ids(root, ids):
    parents = {child: parent for parent in root.iter() for child in parent}
    for el in list(root.iter()):
        if el.get("id") in ids and el in parents:
            parents[el].remove(el)


def tag(name):
    return f"{{{SVG_NS}}}{name}"


def hidden_ids(spec, state):
    """Elements missing from the player map: GM-only ones and undiscovered secrets."""
    hidden = set(spec.get("gm_only", []))
    for key, secret in spec.get("secrets", {}).items():
        if key not in state["secrets"]:
            hidden.update(secret["ids"])
    return hidden


def inside(x, y, poly):
    """Whether a point lies inside a polygon (ray casting)."""
    result = False
    for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1]):
        if (y1 > y) != (y2 > y) and x < x1 + (y - y1) * (x2 - x1) / (y2 - y1):
            result = not result
    return result


def num(el, attr):
    try:
        return float(el.get(attr, "").rstrip("px"))
    except ValueError:
        return None


def player_shapes(svg_path, spec, state):
    """Labels and rectangles of the player map (without hidden elements), in SVG coordinates.

    Skips elements with a transform attribute on themselves or an ancestor,
    because their coordinates are not absolute (e.g. the legend).
    """
    root = ET.parse(svg_path).getroot()
    remove_ids(root, hidden_ids(spec, state))
    parents = {child: parent for parent in root.iter() for child in parent}

    def transformed(el):
        while el is not None:
            if el.get("transform"):
                return True
            el = parents.get(el)
        return False

    labels, rects, seen = [], [], set()
    for el in root.iter():
        if transformed(el):
            continue
        if el.tag == tag("text"):
            text = " ".join("".join(el.itertext()).split())
            x, y = num(el, "x"), num(el, "y")
            if text and x is not None and y is not None and (text, x, y) not in seen:
                seen.add((text, x, y))
                labels.append((text, x, y))
        elif el.tag == tag("rect"):
            x, y, w, h = (num(el, a) for a in ("x", "y", "width", "height"))
            if None not in (x, y, w, h):
                rects.append({"x": x, "y": y, "w": w, "h": h, "fill": el.get("fill", ""),
                              "stroke": el.get("stroke", "none"), "rx": num(el, "rx") or 0})
    return labels, rects


def print_plan(svg_path, spec, state, keys):
    """Layout of discovered areas for the GM: player map labels in order and with distances.

    Shows only what is on the player map, so it reveals nothing undiscovered.
    Optionally uses fields of the areas file: "scale" (pixels per metre),
    "corridor" (fill colour of corridors, splits labels into the sides of the
    corridor) and "objects" (rectangles to count in rooms, e.g. beds:
    {"name": "beds", "size": [min_short, max_short, min_long, max_long] in
    metres, "rounded": true}).
    """
    labels, rects = player_shapes(svg_path, spec, state)
    scale = spec.get("scale")
    corridor_fill = spec.get("corridor")

    for key in keys:
        polys = spec["areas"][key]["polygons"]
        within = lambda x, y: any(inside(x, y, p) for p in polys)
        area_labels = [(t, x, y) for t, x, y in labels if within(x, y)]
        west = min(x for p in polys for x, _ in p)
        north = min(y for p in polys for _, y in p)

        corridor = None
        if corridor_fill:
            halls = [r for r in rects if r["fill"].lower() == corridor_fill.lower()
                     and within(r["x"] + r["w"] / 2, r["y"] + r["h"] / 2)]
            corridor = max(halls, key=lambda r: r["w"] * r["h"], default=None)
        horizontal = corridor is None or corridor["w"] >= corridor["h"]

        def side_of(x, y):
            if corridor is None:
                return ""
            if horizontal:
                top, bottom = corridor["y"], corridor["y"] + corridor["h"]
                return "North side" if y < top else "South side" if y > bottom else "Corridor"
            left, right = corridor["x"], corridor["x"] + corridor["w"]
            return "West side" if x < left else "East side" if x > right else "Corridor"

        names = [""] if corridor is None else (
            ["North side", "Corridor", "South side"] if horizontal
            else ["West side", "Corridor", "East side"])
        sides = {name: [l for l in area_labels if side_of(l[1], l[2]) == name] for name in names}

        # A room is a rectangle with a stroke and no fill (walls). Objects
        # from the "objects" field (e.g. beds) are rectangles of the given
        # size in metres. They count in the smallest room that contains them,
        # next to a label lying in the same room.
        rooms = [r for r in rects if r["fill"] == "none" and r["stroke"] != "none"]

        def room_of(x, y):
            hits = [r for r in rooms if r["x"] <= x <= r["x"] + r["w"] and r["y"] <= y <= r["y"] + r["h"]]
            return min(hits, key=lambda r: r["w"] * r["h"], default=None)

        counts = {}
        for obj in (spec.get("objects", []) if scale else []):
            min_short, max_short, min_long, max_long = obj["size"]
            per_room = Counter()
            for r in rects:
                short, long_ = sorted((r["w"] / scale, r["h"] / scale))
                cx, cy = r["x"] + r["w"] / 2, r["y"] + r["h"] / 2
                if obj.get("rounded") and not r["rx"]:
                    continue
                if min_short <= short <= max_short and min_long <= long_ <= max_long and within(cx, cy):
                    room = room_of(cx, cy)
                    if room:
                        per_room[id(room)] += 1
            for label in area_labels:
                room = room_of(label[1], label[2])
                if room and per_room[id(room)]:
                    counts.setdefault(label, []).append(f"{obj['name']}: {per_room[id(room)]}")

        unit = "m" if scale else "px"
        along = "west to east" if horizontal else "north to south"
        origin = "western" if horizontal else "northern"
        print(f"Plan of area {key} ({spec['areas'][key].get('name', '')}):")
        print(f"  distances in {unit} from the {origin} edge of the area, {along}")
        for side, group in sides.items():
            if not group:
                continue
            if side:
                print(f"  {side}:")
            for label in sorted(group, key=lambda l: l[1] if horizontal else l[2]):
                text, x, y = label
                dist = (x - west) if horizontal else (y - north)
                dist = f"{dist / scale:.0f} m" if scale else f"{dist:.0f} px"
                extra = "".join(f", {c}" for c in counts.get(label, []))
                print(f"    {text} ({dist}{extra})")


def build_player_map(svg_path, spec, state):
    tree = ET.parse(svg_path)
    root = tree.getroot()
    remove_ids(root, hidden_ids(spec, state))

    view = root.get("viewBox")
    if view:
        vx, vy, vw, vh = (float(v) for v in view.replace(",", " ").split())
    else:
        vx, vy = 0.0, 0.0
        vw, vh = float(root.get("width", "1000").rstrip("px")), float(root.get("height", "1000").rstrip("px"))

    polygons = []
    for key in state["areas"]:
        polygons.extend(spec["areas"][key]["polygons"])

    # Everything on the map goes under the mask; the background beneath is the "fog".
    content = [el for el in list(root) if el.tag not in (tag("title"), tag("style"), tag("defs"))]
    for el in content:
        root.remove(el)

    defs = ET.SubElement(root, tag("defs"))
    blur = ET.SubElement(defs, tag("filter"), id="fog-blur", x="-10%", y="-10%", width="120%", height="120%")
    ET.SubElement(blur, tag("feGaussianBlur"), stdDeviation="10")
    mask = ET.SubElement(defs, tag("mask"), id="fog-mask", maskUnits="userSpaceOnUse",
                         x=str(vx), y=str(vy), width=str(vw), height=str(vh))
    ET.SubElement(mask, tag("rect"), x=str(vx), y=str(vy), width=str(vw), height=str(vh), fill="#000")
    # Discovered areas get a soft edge, always visible areas (e.g. the legend) a sharp one.
    for group, shapes_list in (({"filter": "url(#fog-blur)"}, polygons), ({}, spec.get("always", []))):
        shapes = ET.SubElement(mask, tag("g"), fill="#fff", **group)
        for poly in shapes_list:
            ET.SubElement(shapes, tag("polygon"), points=" ".join(f"{x},{y}" for x, y in poly))

    ET.SubElement(root, tag("rect"), x=str(vx), y=str(vy), width=str(vw), height=str(vh), fill="#fff")
    veiled = ET.SubElement(root, tag("g"), mask="url(#fog-mask)")
    for el in content:
        veiled.append(el)
    return tree


def main():
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Player map with fog of war.")
    parser.add_argument("--campaign", required=True, help="name of the campaign folder in Campaigns/")
    parser.add_argument("--map", required=True, help="path to the SVG map with an .areas.json file next to it")
    parser.add_argument("--reveal", nargs="+", default=[], metavar="AREA", help="areas to reveal")
    parser.add_argument("--hide", nargs="+", default=[], metavar="AREA", help="areas to cover again (fixing a mistake)")
    parser.add_argument("--secret", nargs="+", default=[], metavar="SECRET", help="secrets to reveal")
    parser.add_argument("--name", help="name of the player map files (default: name of the map folder)")
    parser.add_argument("--list", action="store_true", help="print areas, secrets and discovery state")
    parser.add_argument("--open", action="store_true", help="open the player map preview in the browser")
    parser.add_argument("--plan", nargs="+", default=[], metavar="AREA",
                        help="print the layout of discovered areas for the GM: player map labels in order and with distances")
    args = parser.parse_args()

    folder = campaign_folder(args.campaign)
    svg_path = Path(args.map)
    if not svg_path.is_absolute():
        svg_path = (Path.cwd() / svg_path).resolve()
    if not svg_path.exists():
        sys.exit(f"Error: missing map {args.map}.")
    spec = load_json(svg_path.with_suffix(".areas.json"))
    folder_map = svg_path.parent.parent if svg_path.parent.name == "Maps" else svg_path.parent
    name = args.name or folder_map.name

    state_path = folder / f"{name}Map.json"
    state = load_json(state_path, default={"map": "", "areas": [], "secrets": []})
    state["map"] = svg_path.relative_to(ROOT).as_posix() if svg_path.is_relative_to(ROOT) else str(svg_path)

    areas = list(spec["areas"])
    secrets = list(spec.get("secrets", {}))
    check_ids(args.reveal + args.hide, areas, "areas")
    check_ids(args.secret, secrets, "secrets")
    check_ids(args.plan, areas, "areas")

    for key in args.reveal:
        if key not in state["areas"]:
            state["areas"].append(key)
    state["areas"] = [k for k in areas if k in state["areas"] and k not in args.hide]
    for key in args.secret:
        if key not in state["secrets"]:
            state["secrets"].append(key)
    state["secrets"] = [k for k in secrets if k in state["secrets"]]

    with state_path.open("w", encoding="utf-8", newline="\n") as fh:
        json.dump(state, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    svg_out = folder / f"{name}Map.svg"
    build_player_map(svg_path, spec, state).write(svg_out, encoding="utf-8", xml_declaration=False)
    html_out = folder / f"{name}Map.html"
    if not html_out.exists():
        html_out.write_text(HTML.format(title=f"{name}: player map", svg=svg_out.name), encoding="utf-8")

    if args.list:
        print("Areas:")
        for key in areas:
            mark = "x" if key in state["areas"] else " "
            print(f"  [{mark}] {key}: {spec['areas'][key].get('name', '')}")
        if secrets:
            print("Secrets:")
            for key in secrets:
                mark = "x" if key in state["secrets"] else " "
                print(f"  [{mark}] {key}: {spec['secrets'][key].get('name', '')}")
    print(f"Discovered areas: {', '.join(state['areas']) or 'none'}")
    print(f"Discovered secrets: {', '.join(state['secrets']) or 'none'}")
    print(f"Player map: {svg_out.relative_to(ROOT).as_posix()}")
    print(f"Preview: {html_out.relative_to(ROOT).as_posix()}")

    if args.plan:
        hidden_areas = [k for k in args.plan if k not in state["areas"]]
        if hidden_areas:
            sys.exit(f"Error: --plan shows only discovered areas, and these are undiscovered: {', '.join(hidden_areas)}. "
                     "Reveal them in the same command with --reveal.")
        print_plan(svg_path, spec, state, args.plan)

    if args.open:
        webbrowser.open(html_out.as_uri())


if __name__ == "__main__":
    main()
