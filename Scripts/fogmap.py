"""Mapa gracza z mgłą wojny: odsłania tylko te obszary mapy, które postać odkryła.

Przykłady:
    python Scripts/fogmap.py --kampania Randuvil --mapa Scenarios/Krypta/MapCrypt.svg --odkryj 1 2
    python Scripts/fogmap.py --kampania Randuvil --mapa Scenarios/Krypta/MapCrypt.svg --sekret plyta
    python Scripts/fogmap.py --kampania Randuvil --mapa Scenarios/Krypta/MapCrypt.svg --lista
    python Scripts/fogmap.py --kampania Randuvil --mapa Scenarios/Krypta/MapCrypt.svg --otworz

Obok mapy SVG musi leżeć plik obszarów o tej samej nazwie z rozszerzeniem
.areas.json (np. MapCrypt.areas.json). Opisuje on obszary do odsłaniania,
sekrety i elementy widoczne tylko dla MG (format: zob. AGENTS.md, rozdział Mapy).

Stan odkrycia jest zapisywany w folderze kampanii, w pliku
<nazwa>-mapa.json, a mapa gracza w <nazwa>-mapa.svg razem z podglądem
<nazwa>-mapa.html, który sam się odświeża. Nazwą domyślnie jest nazwa folderu
scenariusza albo settingu, w którym leży mapa (np. Krypta).
"""

import argparse
import copy
import json
import sys
import webbrowser
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAMPAIGNS = ROOT / "Campaigns"
SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")

HTML = """<!doctype html>
<html lang="pl">
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
  // Mapa przeładowuje się co 2 sekundy, więc odsłonięte obszary pojawiają się same.
  setInterval(function () {{
    var img = new Image();
    img.onload = function () {{ document.getElementById("map").src = img.src; }};
    img.src = "{svg}?t=" + Date.now();
  }}, 2000);
</script>
</body>
</html>
"""


def campaign_folder(name):
    if not name or name in (".", "..") or any(c in name for c in "/\\"):
        sys.exit(f"Błąd: '{name}' nie jest poprawną nazwą kampanii.")
    folder = CAMPAIGNS / name
    if not folder.is_dir():
        known = sorted(p.name for p in CAMPAIGNS.iterdir() if p.is_dir()) if CAMPAIGNS.is_dir() else []
        hint = f" Istniejące kampanie: {', '.join(known)}." if known else " Nie ma jeszcze żadnej kampanii."
        sys.exit(f"Błąd: kampania '{name}' nie istnieje (brak folderu Campaigns/{name}).{hint}")
    return folder


def load_json(path, default=None):
    if not path.exists():
        if default is not None:
            return default
        sys.exit(f"Błąd: brak pliku {path}.")
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def check_ids(given, known, kind):
    bad = [g for g in given if g not in known]
    if bad:
        sys.exit(f"Błąd: nieznane {kind}: {', '.join(bad)}. Dostępne: {', '.join(known)}.")


def remove_ids(root, ids):
    parents = {child: parent for parent in root.iter() for child in parent}
    for el in list(root.iter()):
        if el.get("id") in ids and el in parents:
            parents[el].remove(el)


def tag(name):
    return f"{{{SVG_NS}}}{name}"


def hidden_ids(spec, state):
    """Elementy, których nie ma na mapie gracza: tylko dla MG i nieodkryte sekrety."""
    hidden = set(spec.get("mg_only", []))
    for key, secret in spec.get("secrets", {}).items():
        if key not in state["secrets"]:
            hidden.update(secret["ids"])
    return hidden


def inside(x, y, poly):
    """Czy punkt leży w wielokącie (metoda promienia)."""
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
    """Napisy i prostokąty z mapy gracza (bez elementów ukrytych), we współrzędnych SVG.

    Pomija elementy z atrybutem transform u siebie albo u przodka, bo ich
    współrzędne nie są bezwzględne (np. legenda).
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
    """Układ odkrytych obszarów dla MG: napisy z mapy gracza w kolejności i z odległościami.

    Pokazuje tylko to, co jest na mapie gracza, więc nie zdradza niczego
    nieodkrytego. Opcjonalnie korzysta z pól pliku obszarów: "skala" (pikseli
    na metr), "korytarz" (kolor wypełnienia korytarzy, dzieli napisy na strony
    korytarza) i "obiekty" (prostokąty do policzenia w pomieszczeniach, np.
    łóżka: {"nazwa": "łóżka", "wymiary": [min_krótszy, max_krótszy,
    min_dłuższy, max_dłuższy] w metrach, "zaokraglone": true}).
    """
    labels, rects = player_shapes(svg_path, spec, state)
    scale = spec.get("skala")
    corridor_fill = spec.get("korytarz")

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
                return "Strona północna" if y < top else "Strona południowa" if y > bottom else "Korytarz"
            left, right = corridor["x"], corridor["x"] + corridor["w"]
            return "Strona zachodnia" if x < left else "Strona wschodnia" if x > right else "Korytarz"

        names = [""] if corridor is None else (
            ["Strona północna", "Korytarz", "Strona południowa"] if horizontal
            else ["Strona zachodnia", "Korytarz", "Strona wschodnia"])
        sides = {name: [l for l in area_labels if side_of(l[1], l[2]) == name] for name in names}

        # Pomieszczenie to prostokąt z obrysem i bez wypełnienia (ściany).
        # Obiekty z pola "obiekty" (np. łóżka) to prostokąty o podanych
        # wymiarach w metrach. Liczą się w najmniejszym pomieszczeniu, które
        # je zawiera, przy napisie leżącym w tym samym pomieszczeniu.
        rooms = [r for r in rects if r["fill"] == "none" and r["stroke"] != "none"]

        def room_of(x, y):
            hits = [r for r in rooms if r["x"] <= x <= r["x"] + r["w"] and r["y"] <= y <= r["y"] + r["h"]]
            return min(hits, key=lambda r: r["w"] * r["h"], default=None)

        counts = {}
        for obj in (spec.get("obiekty", []) if scale else []):
            min_short, max_short, min_long, max_long = obj["wymiary"]
            per_room = Counter()
            for r in rects:
                short, long_ = sorted((r["w"] / scale, r["h"] / scale))
                cx, cy = r["x"] + r["w"] / 2, r["y"] + r["h"] / 2
                if obj.get("zaokraglone") and not r["rx"]:
                    continue
                if min_short <= short <= max_short and min_long <= long_ <= max_long and within(cx, cy):
                    room = room_of(cx, cy)
                    if room:
                        per_room[id(room)] += 1
            for label in area_labels:
                room = room_of(label[1], label[2])
                if room and per_room[id(room)]:
                    counts.setdefault(label, []).append(f"{obj['nazwa']}: {per_room[id(room)]}")

        unit = "m" if scale else "px"
        along = "z zachodu na wschód" if horizontal else "z północy na południe"
        origin = "zachodniej" if horizontal else "północnej"
        print(f"Plan obszaru {key} ({spec['areas'][key].get('name', '')}):")
        print(f"  odległości w {unit} od {origin} krawędzi obszaru, {along}")
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

    # Wszystko, co było na mapie, trafia pod maskę; tło pod spodem to "mgła".
    content = [el for el in list(root) if el.tag not in (tag("title"), tag("style"), tag("defs"))]
    for el in content:
        root.remove(el)

    defs = ET.SubElement(root, tag("defs"))
    blur = ET.SubElement(defs, tag("filter"), id="fog-blur", x="-10%", y="-10%", width="120%", height="120%")
    ET.SubElement(blur, tag("feGaussianBlur"), stdDeviation="10")
    mask = ET.SubElement(defs, tag("mask"), id="fog-mask", maskUnits="userSpaceOnUse",
                         x=str(vx), y=str(vy), width=str(vw), height=str(vh))
    ET.SubElement(mask, tag("rect"), x=str(vx), y=str(vy), width=str(vw), height=str(vh), fill="#000")
    # Odkryte obszary mają miękką krawędź, a obszary zawsze widoczne (np. legenda) ostrą.
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

    parser = argparse.ArgumentParser(description="Mapa gracza z mgłą wojny.")
    parser.add_argument("--kampania", required=True, help="nazwa folderu kampanii w Campaigns/")
    parser.add_argument("--mapa", required=True, help="ścieżka do mapy SVG z plikiem .areas.json obok")
    parser.add_argument("--odkryj", nargs="+", default=[], metavar="OBSZAR", help="obszary do odsłonięcia")
    parser.add_argument("--zakryj", nargs="+", default=[], metavar="OBSZAR", help="obszary do ponownego zakrycia (poprawka pomyłki)")
    parser.add_argument("--sekret", nargs="+", default=[], metavar="SEKRET", help="sekrety do odsłonięcia")
    parser.add_argument("--nazwa", help="nazwa plików mapy gracza (domyślnie nazwa folderu mapy)")
    parser.add_argument("--lista", action="store_true", help="wypisz obszary, sekrety i stan odkrycia")
    parser.add_argument("--otworz", action="store_true", help="otwórz podgląd mapy gracza w przeglądarce")
    parser.add_argument("--plan", nargs="+", default=[], metavar="OBSZAR",
                        help="wypisz dla MG układ odkrytych obszarów: napisy z mapy gracza w kolejności i z odległościami")
    args = parser.parse_args()

    folder = campaign_folder(args.kampania)
    svg_path = Path(args.mapa)
    if not svg_path.is_absolute():
        svg_path = (Path.cwd() / svg_path).resolve()
    if not svg_path.exists():
        sys.exit(f"Błąd: brak mapy {args.mapa}.")
    spec = load_json(svg_path.with_suffix(".areas.json"))
    name = args.nazwa or svg_path.parent.name

    state_path = folder / f"{name}-mapa.json"
    state = load_json(state_path, default={"map": "", "areas": [], "secrets": []})
    state["map"] = svg_path.relative_to(ROOT).as_posix() if svg_path.is_relative_to(ROOT) else str(svg_path)

    areas = list(spec["areas"])
    secrets = list(spec.get("secrets", {}))
    check_ids(args.odkryj + args.zakryj, areas, "obszary")
    check_ids(args.sekret, secrets, "sekrety")
    check_ids(args.plan, areas, "obszary")

    for key in args.odkryj:
        if key not in state["areas"]:
            state["areas"].append(key)
    state["areas"] = [k for k in areas if k in state["areas"] and k not in args.zakryj]
    for key in args.sekret:
        if key not in state["secrets"]:
            state["secrets"].append(key)
    state["secrets"] = [k for k in secrets if k in state["secrets"]]

    with state_path.open("w", encoding="utf-8", newline="\n") as fh:
        json.dump(state, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    svg_out = folder / f"{name}-mapa.svg"
    build_player_map(svg_path, spec, state).write(svg_out, encoding="utf-8", xml_declaration=False)
    html_out = folder / f"{name}-mapa.html"
    if not html_out.exists():
        html_out.write_text(HTML.format(title=f"{name}: mapa gracza", svg=svg_out.name), encoding="utf-8")

    if args.lista:
        print("Obszary:")
        for key in areas:
            mark = "x" if key in state["areas"] else " "
            print(f"  [{mark}] {key}: {spec['areas'][key].get('name', '')}")
        if secrets:
            print("Sekrety:")
            for key in secrets:
                mark = "x" if key in state["secrets"] else " "
                print(f"  [{mark}] {key}: {spec['secrets'][key].get('name', '')}")
    print(f"Odkryte obszary: {', '.join(state['areas']) or 'brak'}")
    print(f"Odkryte sekrety: {', '.join(state['secrets']) or 'brak'}")
    print(f"Mapa gracza: {svg_out.relative_to(ROOT).as_posix()}")
    print(f"Podgląd: {html_out.relative_to(ROOT).as_posix()}")

    if args.plan:
        hidden_areas = [k for k in args.plan if k not in state["areas"]]
        if hidden_areas:
            sys.exit(f"Błąd: --plan pokazuje tylko odkryte obszary, a nieodkryte są: {', '.join(hidden_areas)}. "
                     "Odkryj je w tym samym poleceniu opcją --odkryj.")
        print_plan(svg_path, spec, state, args.plan)

    if args.otworz:
        webbrowser.open(html_out.as_uri())


if __name__ == "__main__":
    main()
