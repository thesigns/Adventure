"""Inn map generator for the scenario The String of Sausages (hand-drawn RPG map style).

An author's tool, not for play. Creates two files in the scenario folder:
    MapInn.svg         full map for the GM
    MapInn.areas.json  areas and secrets for Scripts/fogmap.py

Usage:
    python Scenarios/TheStringOfSausages/Tools/make_map.py [path to MapInn.svg]

The style follows Scenarios/TheCrypt/Tools/make_map.py. The generator is
deterministic (fixed random seed). The plan is in metres (1 square = 1 m,
north up): the ground floor with the yard, the barn and the fields on the
left, and smaller panels for the upper floor, the hayloft and the cellar on
the right. After changing the plan, fix the areas at the end of the file too.
"""
import json
import math
import random
import sys
from pathlib import Path

OUT = sys.argv[1] if len(sys.argv) > 1 else str(Path(__file__).resolve().parent.parent / "Maps" / "MapInn.svg")
rnd = random.Random(11)

S = 22.0                 # px per metre
XMIN, YMIN = -10.0, -10.0
XMAX, YMAX = 59.0, 27.0
MAP_W = (XMAX - XMIN) * S
MAP_H = (YMAX - YMIN) * S
LEG_H = 300
W, H = MAP_W, MAP_H + LEG_H
WALL = 0.28              # wall half-thickness (m)


def X(x): return (x - XMIN) * S
def Y(y): return (y - YMIN) * S
def f(v): return f"{v:.1f}"


# ---------------------------------------------------------------- plan (metres)
# ground floor of the inn
TAPROOM = (0, 0, 11, 10)
KITCHEN = (11, 0, 16, 6.5)
PANTRY = (13.6, 0, 16, 2.4)
EDRIC = (11, 6.5, 16, 10)
STAIRS_DOWN = (9.2, 6.6, 11, 10)
# outbuildings
STABLE = (22, -8, 32, -3)
PRIVY = (32.5, -2.9, 33.6, -1.8)
BARN = (22, 10, 32, 18)
# right-hand panels: upper floor, hayloft, cellar
UP_DWARVES = (40, -8, 48, -4)
UP_WIZARD = (48, -8, 56, -4)
UP_CORRIDOR = (40, -4, 56, -2)
UP_MERCHANT = (40, -2, 49.2, 2)
UP_STAIRS = (49.2, -2, 51, 2)
UP_GNOME = (51, -2, 56, 2)
LOFT = (40, 8, 50, 16)
CELLAR = (52, 8, 57, 14.5)

rooms = [TAPROOM, KITCHEN, PANTRY, EDRIC, STABLE, PRIVY, BARN,
         UP_DWARVES, UP_WIZARD, UP_CORRIDOR, UP_MERCHANT, UP_STAIRS, UP_GNOME, LOFT, CELLAR]

# doors: (x0, y0, x1, y1) of the gap in the wall; drawn as a white leaf
doors = [
    (-0.3, 4.4, 0.3, 5.6),        # front door, taproom west wall
    (10.7, 2.8, 11.3, 3.8),       # taproom - kitchen
    (14.3, 2.1, 15.1, 2.7),       # kitchen - pantry
    (12.9, 6.2, 13.7, 6.8),       # kitchen - Edric's room
    (15.7, 4.0, 16.3, 5.0),       # back door, kitchen - yard
    (26.2, -3.3, 27.8, -2.7),     # stable door
    (32.75, -2.1, 33.35, -1.5),   # privy door, south wall
    (25.4, 9.7, 28.6, 10.3),      # barn double door
    (43.6, -4.3, 44.4, -3.7),     # dwarves
    (51.6, -4.3, 52.4, -3.7),     # wizard
    (44.2, -2.3, 45.0, -1.7),     # merchant
    (52.6, -2.3, 53.4, -1.7),     # gnome
]


def wobble(pts, step=0.9, amp=0.03):
    out = []
    n = len(pts)
    for i in range(n):
        a, b = pts[i], pts[(i + 1) % n]
        L = math.hypot(b[0] - a[0], b[1] - a[1])
        k = max(1, int(L / step))
        for j in range(k):
            t = j / k
            out.append((a[0] + (b[0] - a[0]) * t + rnd.uniform(-amp, amp),
                        a[1] + (b[1] - a[1]) * t + rnd.uniform(-amp, amp)))
    return out


def rect_svg(r, jitter=True):
    x0, y0, x1, y1 = r
    pts = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    if jitter:
        pts = wobble(pts)
    return '<polygon points="' + " ".join(f"{f(X(x))},{f(Y(y))}" for x, y in pts) + '"/>'


# ---------------------------------------------------------------- drawing helpers
def line(x1, y1, x2, y2, w=2.0, color="#111", extra=""):
    return (f'<line x1="{f(X(x1))}" y1="{f(Y(y1))}" x2="{f(X(x2))}" y2="{f(Y(y2))}" stroke="{color}" '
            f'stroke-width="{w}" stroke-linecap="round" {extra}/>')


def box(x0, y0, x1, y1, fill="#fff", w=2.4, rx=0, extra=""):
    stroke = "none" if w == 0 else "#111"
    return (f'<rect x="{f(X(x0))}" y="{f(Y(y0))}" width="{f((x1 - x0) * S)}" height="{f((y1 - y0) * S)}" '
            f'rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{w}" {extra}/>')


def shadowed(x0, y0, x1, y1, fill="#fff", w=2.6, rx=0):
    return box(x0 + 0.08, y0 + 0.08, x1 + 0.08, y1 + 0.08, fill="#8c8c8c", w=0, rx=rx) + box(x0, y0, x1, y1, fill, w, rx)


def circle(x, y, r, fill="#fff", w=2.2):
    return f'<circle cx="{f(X(x))}" cy="{f(Y(y))}" r="{f(r * S)}" fill="{fill}" stroke="#111" stroke-width="{w}"/>'


def stairs(x0, y0, x1, y1, horizontal, n):
    s = ""
    for i in range(1, n):
        if horizontal:
            x = x0 + (x1 - x0) * i / n
            s += line(x, y0 + 0.05, x, y1 - 0.05, w=1.8)
        else:
            y = y0 + (y1 - y0) * i / n
            s += line(x0 + 0.05, y, x1 - 0.05, y, w=1.8)
    return s


def ladder(x0, y0, x1, y1):
    s = line(x0, y0, x0, y1, w=2.2) + line(x1, y0, x1, y1, w=2.2)
    n = int((y1 - y0) / 0.4)
    for i in range(1, n):
        y = y0 + (y1 - y0) * i / n
        s += line(x0, y, x1, y, w=1.6)
    return s


def table(x0, y0, x1, y1):
    """Trestle table with a bench along each long side."""
    s = shadowed(x0, y0, x1, y1, w=2.4)
    if x1 - x0 >= y1 - y0:
        s += box(x0 + 0.1, y0 - 0.45, x1 - 0.1, y0 - 0.2, w=1.8) + box(x0 + 0.1, y1 + 0.2, x1 - 0.1, y1 + 0.45, w=1.8)
    else:
        s += box(x0 - 0.45, y0 + 0.1, x0 - 0.2, y1 - 0.1, w=1.8) + box(x1 + 0.2, y0 + 0.1, x1 + 0.45, y1 - 0.1, w=1.8)
    return s


def bed(x0, y0, x1, y1):
    s = shadowed(x0, y0, x1, y1, w=2.4, rx=3)
    s += box(x0 + 0.12, y0 + 0.12, x1 - 0.12, y0 + 0.5, w=1.6, rx=3)          # pillow at the north end
    s += line(x0 + 0.05, y0 + 0.9, x1 - 0.05, y0 + 0.9, w=1.4)               # turned-down blanket
    return s


def cask(x, y, r=0.38):
    return (f'<circle cx="{f(X(x) + 3)}" cy="{f(Y(y) + 3)}" r="{f(r * S)}" fill="#8c8c8c"/>'
            + circle(x, y, r, w=2.4) + circle(x, y, r * 0.55, w=1.4) + f'<circle cx="{f(X(x))}" cy="{f(Y(y))}" r="1.8" fill="#111"/>')


def hay(x0, y0, x1, y1, n):
    """Loose hay: short random strokes."""
    s = []
    for _ in range(n):
        hx, hy = rnd.uniform(x0, x1), rnd.uniform(y0, y1)
        a = rnd.uniform(0, math.pi)
        l = rnd.uniform(0.15, 0.32)
        s.append(f"M{f(X(hx - l * math.cos(a)))} {f(Y(hy - l * math.sin(a)))}L{f(X(hx + l * math.cos(a)))} {f(Y(hy + l * math.sin(a)))}")
    return f'<path d="{"".join(s)}" stroke="#555" stroke-width="1.3" stroke-linecap="round" fill="none"/>'


def wagon(x0, y0, x1, y1, canvas=True):
    """Wagon seen from above, long axis north-south, wheels at the sides, shaft to the north."""
    s = ""
    for wy in (y0 + 0.5, y1 - 0.5):
        s += box(x0 - 0.25, wy - 0.45, x0 + 0.05, wy + 0.45, fill="#111", w=0) + box(x1 - 0.05, wy - 0.45, x1 + 0.25, wy + 0.45, fill="#111", w=0)
    s += line((x0 + x1) / 2 - 0.3, y0, (x0 + x1) / 2 - 0.3, y0 - 1.3, w=2.2) + line((x0 + x1) / 2 + 0.3, y0, (x0 + x1) / 2 + 0.3, y0 - 1.3, w=2.2)
    s += shadowed(x0, y0, x1, y1, w=2.6, rx=3 if canvas else 0)
    if canvas:
        for i in range(1, 5):
            yy = y0 + (y1 - y0) * i / 5
            s += line(x0 + 0.1, yy, x1 - 0.1, yy, w=1.4)
    return s


def fence(points, gaps=()):
    """Wooden fence: a thin line with square posts every 2 m, open in the given gaps."""
    s = ""
    for (ax, ay), (bx, by) in zip(points, points[1:]):
        L = math.hypot(bx - ax, by - ay)
        n = max(1, int(L / 2))
        for i in range(n):
            t0, t1 = i / n, (i + 1) / n
            px, py = ax + (bx - ax) * t0, ay + (by - ay) * t0
            qx, qy = ax + (bx - ax) * t1, ay + (by - ay) * t1
            mx, my = (px + qx) / 2, (py + qy) / 2
            if any(g0 <= mx <= g1 and g2 <= my <= g3 for g0, g2, g1, g3 in gaps):
                continue
            s += line(px, py, qx, qy, w=2.0)
            s += box(px - 0.12, py - 0.12, px + 0.12, py + 0.12, fill="#111", w=0)
    return s


def hedge(x0, x1, y):
    s = ""
    x = x0
    while x < x1:
        r = rnd.uniform(0.45, 0.75)
        cx, cy = x + r, y + rnd.uniform(-0.15, 0.15)
        s += (f'<circle cx="{f(X(cx) + 3)}" cy="{f(Y(cy) + 3)}" r="{f(r * S)}" fill="#8c8c8c"/>'
              + circle(cx, cy, r, w=2.4))
        for _ in range(3):
            a = rnd.uniform(0, 2 * math.pi)
            s += line(cx + 0.2 * math.cos(a), cy + 0.2 * math.sin(a), cx + 0.45 * math.cos(a), cy + 0.45 * math.sin(a), w=1.3)
        x += r * 1.5
    return s


def tufts(x0, y0, x1, y1, n):
    s = []
    for _ in range(n):
        tx, ty = rnd.uniform(x0, x1), rnd.uniform(y0, y1)
        s.append(f"M{f(X(tx) - 4)} {f(Y(ty) - 5)}L{f(X(tx))} {f(Y(ty) + 2)}L{f(X(tx) + 4)} {f(Y(ty) - 5)}")
    return f'<path d="{"".join(s)}" stroke="#555" stroke-width="1.4" fill="none" stroke-linejoin="round"/>'


def stipple(x0, y0, x1, y1, n, avoid=()):
    s = []
    while len(s) < n:
        px, py = rnd.uniform(x0, x1), rnd.uniform(y0, y1)
        if any(a0 - 0.4 <= px <= a1 + 0.4 and b0 - 0.4 <= py <= b1 + 0.4 for a0, b0, a1, b1 in avoid):
            continue
        s.append(f'<circle cx="{f(X(px))}" cy="{f(Y(py))}" r="{f(rnd.uniform(0.9, 1.9))}"/>')
    return f'<g fill="#555">{"".join(s)}</g>'


def num_label(n, x, y):
    return (f'<text x="{f(X(x))}" y="{f(Y(y))}" class="num" stroke="#fff" stroke-width="6" stroke-linejoin="round">{n}</text>'
            f'<text x="{f(X(x))}" y="{f(Y(y))}" class="num">{n}</text>')


def name_label(t, x, y, cls="name", anchor="middle"):
    return (f'<text x="{f(X(x))}" y="{f(Y(y))}" class="{cls}" text-anchor="{anchor}" stroke="#fff" stroke-width="5" stroke-linejoin="round">{t}</text>'
            f'<text x="{f(X(x))}" y="{f(Y(y))}" class="{cls}" text-anchor="{anchor}">{t}</text>')


# ---------------------------------------------------------------- outside: road, lane, yard, garden, fields
ground = []
# the highway, north-south, west of the inn
ROAD = (-8, YMIN, -3, 26)
ground.append(line(-8, YMIN, -8, 26, w=2.4) + line(-3, YMIN, -3, -3.4, w=2.4) + line(-3, 0.3, -3, 26, w=2.4))
for rx in (-6.6, -4.4):
    yy = YMIN
    while yy < 26:
        l = rnd.uniform(1.0, 2.6)
        ground.append(line(rx + rnd.uniform(-0.1, 0.1), yy, rx + rnd.uniform(-0.1, 0.1), min(yy + l, 26), w=1.5, color="#666"))
        yy += l + rnd.uniform(0.3, 1.0)
ground.append(stipple(-7.8, YMIN, -3.2, 26, 120))
# lane from the road to the yard gate, north of the house
ground.append(stipple(-3, -3, 16, 0, 40))
# yard: mud
DUNG = (29.6, -2.7, 31.6, -1.5)    # dung heap by the stable, next to the privy
buildings = [TAPROOM, KITCHEN, EDRIC, STABLE, PRIVY, BARN]
ground.append(stipple(16, -3, 34, 18.4, 230, avoid=buildings + [(18, 1, 20.2, 5), (26, 3.5, 27.8, 6.5), DUNG]))
# fences: lane north side, yard east and south sides, with the gate and the wicket
ground.append(fence([(-3, -3.3), (22, -3.3)]))
ground.append(fence([(32, -3.3), (34, -3.3), (34, 18.6), (32, 18.6)]))
ground.append(fence([(16, 10), (16, 18.6), (22, 18.6)], gaps=[(17.5, 18, 19.5, 19)]))
# kitchen garden south of the house: furrows
for gy in range(11, 19):
    ground.append(line(0.6, gy + 0.3, 15.2, gy + 0.3, w=1.3, color="#777", extra='stroke-dasharray="5 4"'))
ground.append(fence([(0, 10), (0, 18.6), (16, 18.6)]))
# hedge and ditch along the fields
ground.append(hedge(-2.6, 36, 19.7))
ground.append(line(-2.6, 20.9, 36, 20.9, w=1.6, extra='stroke-dasharray="7 4"') + line(-2.6, 21.5, 36, 21.5, w=1.6, extra='stroke-dasharray="7 4"'))
ground.append(tufts(-2.6, 22.2, 37, 26.3, 140))

# ---------------------------------------------------------------- features
feat = []
# 2 taproom: fireplace, counter, tables, stairs up
feat.append(shadowed(3.8, 0.0, 7.2, 0.9, fill="#bdbdbd"))
for i in range(5):
    feat.append(line(4.1 + i * 0.7, 0.15, 4.4 + i * 0.7, 0.75, w=1.6))
feat.append(f'<path d="M{f(X(4.6))} {f(Y(0.9))}Q{f(X(5.5))} {f(Y(1.8))} {f(X(6.4))} {f(Y(0.9))}" fill="none" stroke="#111" stroke-width="1.8" stroke-dasharray="3 3"/>')
feat.append(shadowed(8.2, 0.6, 8.8, 5.6))                     # counter
for cy in (1.2, 2.1):
    feat.append(cask(9.9, cy, 0.34))
for tx, ty in ((1.2, 2.4), (4.6, 3.6), (1.2, 6.4), (4.6, 7.4)):
    feat.append(table(tx, ty, tx + 2.4, ty + 0.9))
feat.append(stairs(*STAIRS_DOWN, False, 9))
feat.append(f'<path d="M{f(X(10.1))} {f(Y(9.3))}L{f(X(10.1))} {f(Y(7.2))}M{f(X(9.8))} {f(Y(7.6))}L{f(X(10.1))} {f(Y(7.2))}L{f(X(10.4))} {f(Y(7.6))}" stroke="#111" stroke-width="2" fill="none" stroke-linecap="round"/>')
# 3 kitchen: hearth, long table, chopping block, trapdoor; pantry with hanging sausages
feat.append(shadowed(11.3, 0.0, 13.0, 0.8, fill="#bdbdbd"))
feat.append(shadowed(11.6, 1.6, 12.4, 4.4))
feat.append(circle(15.0, 3.6, 0.32, w=2.4))
feat.append(line(14.85, 3.45, 15.2, 3.75, w=2.2))
feat.append(box(13.2, 4.9, 14.1, 5.8, w=2.4) + line(13.2, 4.9, 14.1, 5.8, w=1.2) + line(14.1, 4.9, 13.2, 5.8, w=1.2))
feat.append(box(13.75, 0.2, 15.9, 0.5, w=1.6) + box(13.75, 1.9, 15.9, 2.2, w=1.6))
for sx in (14.1, 14.6, 15.1, 15.6):
    feat.append(f'<path d="M{f(X(sx))} {f(Y(0.8))}q4 6 0 12q-4 6 0 12" fill="none" stroke="#111" stroke-width="2"/>')
# 4 Edric's room
feat.append(bed(14.4, 7.0, 15.7, 9.4))
feat.append(shadowed(11.4, 8.9, 12.4, 9.6))
# 5 yard: jugglers' wagon, prison cart with the broken chain, well
feat.append(wagon(18, 1, 20.2, 5))
feat.append(wagon(26, 3.5, 27.8, 6.5, canvas=False))
for i in range(4):
    feat.append(f'<ellipse cx="{f(X(27.9 + i * 0.22))}" cy="{f(Y(4.2 + i * 0.3))}" rx="3.2" ry="2.2" fill="none" stroke="#111" stroke-width="1.4"/>')
feat.append(circle(21.0, 8.0, 0.6, w=3) + circle(21.0, 8.0, 0.35, fill="#2a2a2a", w=1.6))
# privy: a plank seat with a hole; dung heap beside it
feat.append(box(32.75, -2.75, 33.45, -2.35, w=1.6) + circle(33.1, -2.55, 0.12, fill="#2a2a2a", w=1.2))
feat.append(f'<ellipse cx="{f(X(30.6))}" cy="{f(Y(-2.1))}" rx="{f(1.0 * S)}" ry="{f(0.6 * S)}" fill="#d9d9d9" stroke="#111" stroke-width="2.2"/>')
feat.append(hay(29.9, -2.5, 31.3, -1.7, 18))
# 6 stable: stalls
for sx in (24, 26, 28, 30):
    feat.append(line(sx, -8, sx, -5.4, w=2.4))
for sx in (23, 25, 27, 29, 31):
    feat.append(box(sx - 0.4, -7.9, sx + 0.4, -7.5, w=1.6))
feat.append(hay(22.2, -7.8, 31.8, -5.6, 50))
# 7 barn: hay on the floor, ladder to the hayloft, tools and anvil block
feat.append(hay(22.3, 12.0, 31.7, 17.7, 260))
feat.append(hay(22.3, 10.3, 25.0, 12.0, 40))
feat.append(ladder(23.0, 10.6, 23.8, 12.8))
feat.append(shadowed(30.4, 16.5, 31.7, 17.6))
feat.append(line(30.6, 16.8, 31.4, 17.3, w=1.6) + line(30.7, 17.35, 31.5, 16.9, w=1.6))
feat.append(shadowed(29.3, 16.9, 29.9, 17.5, fill="#bdbdbd"))
# 9 hayloft: heaps of hay, the ladder hole, the loading hatch
feat.append(hay(40.3, 8.3, 49.7, 15.7, 330))
feat.append(box(41.0, 10.6, 41.8, 12.8, fill="#2a2a2a", w=2.4) + ladder(41.1, 10.7, 41.7, 12.7))
feat.append(box(43.4, 7.7, 46.6, 8.3, w=2.4))
# 10-14 upper floor: stairs, beds, the dwarves' chest
feat.append(stairs(*UP_STAIRS, False, 7))
for bx in (41.0, 43.3):
    feat.append(bed(bx, -7.6, bx + 1.2, -5.4))
feat.append(shadowed(45.6, -7.4, 47.3, -6.5, fill="#bdbdbd"))
feat.append(bed(54.4, -7.6, 55.6, -5.4))
feat.append(shadowed(49.0, -7.5, 50.6, -6.7))
for bx in (40.6, 42.6):
    feat.append(bed(bx, -1.6, bx + 1.2, 0.6))
feat.append(bed(54.4, -1.6, 55.6, 0.6))
feat.append(shadowed(54.3, 1.0, 55.7, 1.7))
# 15 cellar: casks along the walls, ladder up
for cx, cy in ((52.7, 8.7), (53.6, 8.7), (54.5, 8.7), (52.7, 9.6), (56.3, 8.7), (56.3, 9.6), (56.3, 10.5), (52.7, 13.7)):
    feat.append(cask(cx, cy))
feat.append(box(54.2, 12.9, 55.1, 13.8, fill="#2a2a2a", w=2.4) + ladder(54.35, 13.0, 54.95, 13.7))

# doors
door_svg = []
for x0, y0, x1, y1 in doors:
    door_svg.append(box(x0, y0, x1, y1, fill="#fff", w=0))
    if x1 - x0 < y1 - y0:
        door_svg.append(box((x0 + x1) / 2 - 0.13, y0, (x0 + x1) / 2 + 0.13, y1, w=2.2))
    else:
        door_svg.append(box(x0, (y0 + y1) / 2 - 0.13, x1, (y0 + y1) / 2 + 0.13, w=2.2))
# the loft hatch and the trapdoor shafts are not doors; the barn has no south door

# ---------------------------------------------------------------- labels
numbers = [num_label(1, -5.5, -6.0), num_label(2, 2.8, 5.6), num_label(3, 13.2, 3.4), num_label(4, 13.4, 9.7),
           num_label(5, 24.0, 2.4), num_label(6, 27.0, -4.0), num_label(7, 27.0, 14.6), num_label(8, 8.0, 24.6),
           num_label(9, 45.0, 12.6), num_label(10, 47.5, -2.35), num_label(11, 46.4, -4.3), num_label(12, 52.0, -4.3),
           num_label(13, 46.5, 1.5), num_label(14, 52.7, 1.4), num_label(15, 54.6, 11.6)]
names = [
    f'<g transform="rotate(-90 {f(X(-5.2))} {f(Y(10))})">' + name_label("the highway", -5.2, 10, cls="note") + "</g>",
    name_label("to Kingsbridge", -5.5, -9.2, cls="tiny"),
    name_label("to Crossholt", -5.5, 25.6, cls="tiny"),
    name_label("Taproom", 5.5, 9.2), name_label("Kitchen", 12.4, 1.4, cls="tiny"),
    name_label("Room", 12.7, 7.5, cls="tiny"),
    name_label("Yard", 30.0, 1.0), name_label("Stable", 27.0, -5.0, cls="tiny"), name_label("Barn", 27.0, 11.4),
    name_label("Garden", 8.0, 14.9), name_label("hedge and ditch", 30.0, 22.6, cls="tiny"), name_label("Fields", 20.0, 24.2),
    # features, so that fogmap.py --plan lists them
    name_label("front door", -3.3, 5.3, cls="tiny", anchor="end"),
    name_label("fireplace", 5.5, 2.6, cls="tiny"), name_label("counter", 8.0, 5.6, cls="tiny", anchor="end"),
    name_label("stairs up", 9.0, 6.6, cls="tiny", anchor="end"),
    name_label("pantry", 15.9, 3.05, cls="tiny", anchor="end"), name_label("back door", 15.6, 4.6, cls="tiny", anchor="end"),
    name_label("well", 21.0, 9.3, cls="tiny"), name_label("wagon", 19.1, 5.9, cls="tiny"),
    name_label("prison cart", 26.9, 7.4, cls="tiny"), name_label("wicket", 18.5, 18.1, cls="tiny"),
    name_label("privy", 33.05, -0.2, cls="tiny"), name_label("dung heap", 30.4, -0.6, cls="tiny"),
    name_label("ladder", 24.1, 11.9, cls="tiny", anchor="start"), name_label("tools", 31.0, 16.2, cls="tiny"),
    name_label("anvil", 29.2, 17.4, cls="tiny", anchor="end"),
    name_label("ladder", 41.4, 13.5, cls="tiny"), name_label("loading hatch", 45.0, 9.0, cls="tiny"),
    name_label("ladder", 54.65, 14.35, cls="tiny"), name_label("casks", 54.6, 10.3, cls="tiny"),
    name_label("Upper floor", 48.0, -8.6, cls="panel"), name_label("Hayloft", 45.0, 7.2, cls="panel"),
    name_label("Cellar", 54.5, 7.2, cls="panel"),
    name_label("Guest room", 46.4, -5.7, cls="tiny"), name_label("Guest room", 52.0, -5.7, cls="tiny"),
    name_label("Guest room", 46.5, -0.6, cls="tiny"), name_label("Guest room", 52.7, -0.4, cls="tiny"),
]

legend_rooms = [
    "1  Highway and front door", "2  Taproom", "3  Kitchen and pantry", "4  Edric's room", "5  Yard",
    "6  Stable", "7  Barn", "8  Garden and fields", "9  Hayloft", "10  Upper corridor",
    "11  Dwarves' room", "12  Wizard's room", "13  Merchant's room", "14  Gnome's room", "15  Cellar (Edric's casks)",
]


def legend():
    top = MAP_H + 10
    s = [f'<line x1="40" y1="{f(top)}" x2="{f(W - 40)}" y2="{f(top)}" stroke="#111" stroke-width="2.5"/>']
    s.append(f'<text x="40" y="{f(top + 52)}" class="title">The String of Sausages</text>')
    s.append(f'<text x="42" y="{f(top + 82)}" class="sub">the highway south of Kingsbridge</text>')
    sx, sy = 42, top + 128
    for i in range(5):
        s.append(f'<rect x="{f(sx + i * S * 2)}" y="{f(sy)}" width="{f(S * 2)}" height="9" fill="{"#111" if i % 2 == 0 else "#fff"}" stroke="#111" stroke-width="1.5"/>')
    for i, t in ((0, "0"), (5, "10 m")):
        s.append(f'<text x="{f(sx + i * S * 2)}" y="{f(sy + 30)}" class="small" text-anchor="{"start" if i == 0 else "middle"}">{t}</text>')
    s.append(f'<text x="{f(sx)}" y="{f(sy + 54)}" class="small">1 square = 1 m</text>')
    cx, cy = 330, top + 150
    s.append(f'<path d="M{cx} {cy - 34}L{cx + 10} {cy}L{cx} {cy - 6}L{cx - 10} {cy}Z" fill="#111"/>')
    s.append(f'<path d="M{cx} {cy + 34}L{cx + 10} {cy}L{cx} {cy + 6}L{cx - 10} {cy}Z" fill="#fff" stroke="#111" stroke-width="1.5"/>')
    s.append(f'<text x="{cx}" y="{cy - 42}" class="small" text-anchor="middle" font-weight="bold">N</text>')
    colx = [600, 830, 1080]
    s.append('<g id="legend-rooms">')
    for i, t in enumerate(legend_rooms):
        c, r = divmod(i, 5)
        n, name = t.split("  ", 1)
        y = top + 130 + r * 34 - 90
        s.append(f'<text x="{colx[c]}" y="{f(y)}" class="lnum">{n}</text>')
        s.append(f'<text x="{colx[c] + 32}" y="{f(y)}" class="ltext">{name}</text>')
    s.append('</g>')
    kx, ky = 1330, top + 26
    items = [
        (f'<rect x="{kx}" y="{ky}" width="28" height="9" fill="#fff" stroke="#111" stroke-width="2.2"/>', "door"),
        (''.join(f'<line x1="{kx + i * 5}" y1="{ky - 4}" x2="{kx + i * 5}" y2="{ky + 13}" stroke="#111" stroke-width="1.8"/>' for i in range(6)), "stairs"),
        (f'<line x1="{kx}" y1="{ky - 4}" x2="{kx}" y2="{ky + 13}" stroke="#111" stroke-width="2"/><line x1="{kx + 12}" y1="{ky - 4}" x2="{kx + 12}" y2="{ky + 13}" stroke="#111" stroke-width="2"/>'
         + ''.join(f'<line x1="{kx}" y1="{ky - 1 + i * 5}" x2="{kx + 12}" y2="{ky - 1 + i * 5}" stroke="#111" stroke-width="1.4"/>' for i in range(3)), "ladder"),
        (f'<line x1="{kx}" y1="{ky + 4}" x2="{kx + 28}" y2="{ky + 4}" stroke="#111" stroke-width="2"/><rect x="{kx - 2}" y="{ky + 2}" width="5" height="5" fill="#111"/><rect x="{kx + 24}" y="{ky + 2}" width="5" height="5" fill="#111"/>', "fence"),
        (f'<rect x="{kx}" y="{ky - 3}" width="28" height="14" fill="#2a2a2a" stroke="#111" stroke-width="2.4"/>', "trapdoor, hole"),
        (''.join(f'<line x1="{kx + rnd.uniform(0, 24)}" y1="{ky + rnd.uniform(-4, 12)}" x2="{kx + rnd.uniform(4, 28)}" y2="{ky + rnd.uniform(-4, 12)}" stroke="#555" stroke-width="1.3"/>' for _ in range(9)), "hay"),
    ]
    for i, (g, t) in enumerate(items):
        dy = i * 34
        dx = 0
        s.append(f'<g transform="translate({dx},{dy})">{g}<text x="{kx + 40}" y="{ky + 10}" class="ltext" font-size="17">{t}</text></g>')
    return "\n".join(s)


# ---------------------------------------------------------------- assemble
floors_svg = "".join(rect_svg(r) for r in rooms)
full = f'x="0" y="0" width="{f(MAP_W)}" height="{f(MAP_H)}"'
grid = []
for gx in range(int(XMIN), int(XMAX) + 1):
    grid.append(f"M{f(X(gx))} 0V{f(MAP_H)}")
for gy in range(int(YMIN), int(YMAX) + 1):
    grid.append(f"M0 {f(Y(gy))}H{f(MAP_W)}")
grid_d = "".join(grid)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {f(W)} {f(H)}" width="{f(W)}" height="{f(H)}">
<title>The String of Sausages</title>
<style>
  .num {{ font: bold 28px Georgia, 'Times New Roman', serif; text-anchor: middle; fill: #111; }}
  .name {{ font: italic 20px Georgia, 'Times New Roman', serif; fill: #111; }}
  .tiny {{ font: italic 15px Georgia, 'Times New Roman', serif; fill: #111; }}
  .panel {{ font: bold 21px Georgia, 'Times New Roman', serif; fill: #111; letter-spacing: 1px; }}
  .title {{ font: bold 40px Georgia, 'Times New Roman', serif; fill: #111; letter-spacing: 2px; }}
  .sub {{ font: italic 19px Georgia, 'Times New Roman', serif; fill: #333; }}
  .small {{ font: 15px Georgia, 'Times New Roman', serif; fill: #111; }}
  .lnum {{ font: bold 22px Georgia, 'Times New Roman', serif; fill: #111; }}
  .ltext {{ font: 18px Georgia, 'Times New Roman', serif; fill: #111; }}
  .note {{ font: italic 17px Georgia, 'Times New Roman', serif; fill: #111; }}
</style>
<defs>
  <g id="floors">{floors_svg}</g>
  <mask id="floormask" maskUnits="userSpaceOnUse" {full}>
    <rect {full} fill="#000"/><use href="#floors" fill="#fff"/>
  </mask>
  <mask id="outsidemask" maskUnits="userSpaceOnUse" {full}>
    <rect {full} fill="#fff"/><use href="#floors" fill="#000" stroke="#000" stroke-width="{f(2 * WALL * S)}"/>
  </mask>
  <mask id="shadowmask" maskUnits="userSpaceOnUse" {full}>
    <rect {full} fill="#000"/><use href="#floors" fill="#fff"/><use href="#floors" fill="#000" transform="translate(7,7)"/>
  </mask>
</defs>
<rect x="0" y="0" width="{f(W)}" height="{f(H)}" fill="#fff"/>
<g id="outside" mask="url(#outsidemask)">
  <path d="{grid_d}" stroke="#b5b5b5" stroke-width="1" stroke-dasharray="3 4" fill="none"/>
  {"".join(ground)}
</g>
<g id="building-shadow" transform="translate(8,8)"><use href="#floors" fill="#8c8c8c" stroke="#8c8c8c" stroke-width="{f(2 * WALL * S)}" stroke-linejoin="round"/></g>
<g id="walls"><use href="#floors" fill="#111" stroke="#111" stroke-width="{f(2 * WALL * S)}" stroke-linejoin="round"/></g>
<use href="#floors" fill="#fff"/>
<g mask="url(#floormask)">
  <path d="{grid_d}" stroke="#a6a6a6" stroke-width="1" fill="none"/>
</g>
<rect {full} fill="#8f8f8f" mask="url(#shadowmask)"/>
<g id="walls-inner" fill="none" stroke="#111" stroke-width="{f(WALL * S)}">{"".join(rect_svg(r, jitter=False) for r in rooms)}</g>
<g id="doors">{"".join(door_svg)}</g>
<g id="features">{"".join(feat)}</g>
<g id="names">{"".join(names)}</g>
<g id="labels">{"".join(numbers)}</g>
<g id="legend">{legend()}</g>
</svg>
'''


def px_rect(x0, y0, x1, y1):
    return [[round(X(x0), 1), round(Y(y0), 1)], [round(X(x1), 1), round(Y(y0), 1)],
            [round(X(x1), 1), round(Y(y1), 1)], [round(X(x0), 1), round(Y(y1), 1)]]


areas = {
    "map": "MapInn.svg",
    "gm_only": ["labels", "legend-rooms"],
    "scale": S,
    "always": [[[0, round(MAP_H + 8, 1)], [round(W, 1), round(MAP_H + 8, 1)], [round(W, 1), round(H, 1)], [0, round(H, 1)]]],
    "areas": {
        "1": {"name": "Highway and front door", "polygons": [px_rect(-9.6, YMIN, -2.6, 26.6), px_rect(-2.6, -3.6, 16.0, -0.3),
                                                             px_rect(-2.6, -0.3, -0.5, 10.5)]},
        "2": {"name": "Taproom", "polygons": [px_rect(-0.5, -0.5, 11.0, 10.5)]},
        "3": {"name": "Kitchen and pantry", "polygons": [px_rect(11.0, -0.5, 16.5, 6.5)]},
        "4": {"name": "Edric's room", "polygons": [px_rect(11.0, 6.5, 16.5, 10.5)]},
        "5": {"name": "Yard", "polygons": [px_rect(16.5, -3.6, 34.6, 9.7), px_rect(16.0, 9.7, 21.7, 19.0), px_rect(32.3, 9.7, 34.6, 19.0)]},
        "6": {"name": "Stable", "polygons": [px_rect(21.6, -8.6, 32.4, -3.6)]},
        "7": {"name": "Barn", "polygons": [px_rect(21.6, 9.7, 32.4, 18.4)]},
        "8": {"name": "Garden and fields", "polygons": [px_rect(-2.6, 10.5, 16.0, 19.0), px_rect(-2.6, 18.4, 37.6, 26.6)]},
        "9": {"name": "Hayloft", "polygons": [px_rect(39.5, 6.4, 50.5, 16.5)]},
        "10": {"name": "Upper corridor", "polygons": [px_rect(39.5, -4.0, 56.5, -2.0), px_rect(49.2, -2.0, 51.0, 2.5), px_rect(39.5, -9.6, 56.5, -8.3)]},
        "11": {"name": "Dwarves' room", "polygons": [px_rect(39.5, -8.5, 48.0, -4.0)]},
        "12": {"name": "Wizard's room", "polygons": [px_rect(48.0, -8.5, 56.5, -4.0)]},
        "13": {"name": "Merchant's room", "polygons": [px_rect(39.5, -2.0, 49.2, 2.5)]},
        "14": {"name": "Gnome's room", "polygons": [px_rect(51.0, -2.0, 56.5, 2.5)]},
        "15": {"name": "Cellar", "polygons": [px_rect(51.5, 6.4, 57.5, 15.0)]},
    },
    "secrets": {},
}


def dump(o, ind=0):
    """JSON with every polygon (list of points) or list of strings kept on a single line."""
    pad = "  " * (ind + 1)
    if isinstance(o, dict):
        if not o:
            return "{}"
        items = [f"{pad}{json.dumps(k, ensure_ascii=False)}: {dump(v, ind + 1)}" for k, v in o.items()]
        return "{\n" + ",\n".join(items) + "\n" + "  " * ind + "}"
    if isinstance(o, list) and o and not (isinstance(o[0], list) and isinstance(o[0][0], list)):
        return json.dumps(o, ensure_ascii=False)
    if isinstance(o, list):
        return "[\n" + ",\n".join(pad + dump(v, ind + 1) for v in o) + "\n" + "  " * ind + "]"
    return json.dumps(o, ensure_ascii=False)


Path(OUT).parent.mkdir(parents=True, exist_ok=True)
with open(OUT.replace(".svg", ".areas.json"), "w", encoding="utf-8", newline="\n") as fh:
    fh.write(dump(areas) + "\n")
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(svg)
print(OUT, len(svg) // 1024, "KB")
