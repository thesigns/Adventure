"""Crypt map generator for the scenario The Crypt (hand-drawn dungeon map style).

An author's tool, not for play. Creates two files in the scenario folder:
    MapCrypt.svg         full map for the GM
    MapCrypt.areas.json  areas and secrets for Scripts/fogmap.py

Usage:
    python Scenarios/TheCrypt/Tools/make_map.py [path to MapCrypt.svg]

The generator is deterministic (fixed random seed), so without code changes
it always creates the same map. The crypt plan is in metres (1 square = 1 m,
north up) in the lists `floors`/`core` and in the crack data; after changing
the plan, the areas in the `areas` dict at the end of the file must be fixed
too.
"""
import math
import random
import sys
from pathlib import Path

OUT = sys.argv[1] if len(sys.argv) > 1 else str(Path(__file__).resolve().parent.parent / "Maps" / "MapCrypt.svg")
rnd = random.Random(7)

S = 22.0                 # px per metre
XMIN, YMIN = -3.0, -8.0
XMAX, YMAX = 64.0, 39.0
MAP_W = (XMAX - XMIN) * S
MAP_H = (YMAX - YMIN) * S
LEG_H = 300
W, H = MAP_W, MAP_H + LEG_H

D = 2.3                  # rock thickness around rooms (m)
WALL = 0.32              # wall half-thickness (m)


def X(x): return (x - XMIN) * S
def Y(y): return (y - YMIN) * S
def f(v): return f"{v:.1f}"


# ---------------------------------------------------------------- geometry
def rect(x0, y0, x1, y1): return ("rect", (x0, y0, x1, y1))
def circ(cx, cy, r): return ("circle", (cx, cy, r))


def crack_poly(pts, widths):
    left, right = [], []
    for i, (x, y) in enumerate(pts):
        a = pts[max(i - 1, 0)]
        b = pts[min(i + 1, len(pts) - 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]
        L = math.hypot(dx, dy) or 1
        nx, ny = -dy / L, dx / L
        w = widths[i] / 2
        left.append((x + nx * w, y + ny * w))
        right.append((x - nx * w, y - ny * w))
    return ("poly", left + right[::-1])


crack_pts = [(47.9, 21.0), (50.0, 20.2), (51.6, 21.4), (53.0, 20.6), (54.4, 21.9), (55.0, 23.8),
             (54.2, 25.4), (55.2, 27.0), (56.8, 27.8), (57.4, 29.6), (56.6, 31.2), (57.8, 32.8),
             (59.4, 33.6), (60.4, 35.0), (61.4, 36.2), (62.2, 37.2)]
crack_w = [0.9, 0.6, 0.75, 0.55, 0.7, 0.6, 0.75, 0.6, 0.7, 0.55, 0.7, 0.65, 0.8, 0.9, 1.1, 1.3]
CUT = 12  # crack points that lie inside the rock

STAIRS_OUT = rect(19, -5.2, 21, 4.3)
STAIRS_IN = rect(19, -1.2, 21, 4.3)

core = [
    rect(17, 4, 23, 10),            # 2 chapel
    rect(19, 9.8, 21, 20.2),        # 3 corridor
    rect(12.8, 20, 25.2, 22),       # 3 fork
    rect(3, 19, 13, 23),            # 4 ossuary
    rect(25, 17, 33, 25),           # 5 hall of graves
    rect(28.5, 24.8, 29.5, 25.9),   # door 5-6
    rect(27.5, 25.8, 30.5, 29.8),   # 6 storeroom
    rect(32.8, 20, 37.2, 22),       # stairs 5-7
    rect(37, 19.5, 42, 22.5),       # 7 antechamber
    rect(41.8, 20.4, 43.2, 21.6),   # door 7-8
    circ(45.6, 21, 3.0),            # 8 tomb
]
for ax in (4.0, 6.6, 9.2):          # ossuary niches
    core.append(rect(ax, 18.25, ax + 1.2, 19.05))
    core.append(rect(ax, 22.95, ax + 1.2, 23.75))

floors = [STAIRS_OUT] + core + [crack_poly(crack_pts, crack_w)]
rockbase = [STAIRS_IN] + core + [crack_poly(crack_pts[:CUT + 1], crack_w[:CUT + 1])]


def seg_dist(px, py, ax, ay, bx, by):
    dx, dy = bx - ax, by - ay
    t = ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy or 1)
    t = max(0, min(1, t))
    return math.hypot(px - ax - t * dx, py - ay - t * dy)


def inside_poly(px, py, pts):
    c = False
    n = len(pts)
    for i in range(n):
        (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % n]
        if (y1 > py) != (y2 > py) and px < (x2 - x1) * (py - y1) / (y2 - y1) + x1:
            c = not c
    return c


def sdist(px, py, shape):
    kind, g = shape
    if kind == "rect":
        x0, y0, x1, y1 = g
        dx = max(x0 - px, 0, px - x1)
        dy = max(y0 - py, 0, py - y1)
        if dx == 0 and dy == 0:
            return -min(px - x0, x1 - px, py - y0, y1 - py)
        return math.hypot(dx, dy)
    if kind == "circle":
        cx, cy, r = g
        return math.hypot(px - cx, py - cy) - r
    pts = g
    d = min(seg_dist(px, py, *pts[i], *pts[(i + 1) % len(pts)]) for i in range(len(pts)))
    return -d if inside_poly(px, py, pts) else d


def field(px, py, shapes):
    return min(sdist(px, py, s) for s in shapes)


def wobble(pts, step=0.9, amp=0.035):
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


def shape_svg(shape, jitter=True):
    kind, g = shape
    if kind == "circle":
        cx, cy, r = g
        pts = [(cx + r * math.cos(t * 2 * math.pi / 48), cy + r * math.sin(t * 2 * math.pi / 48)) for t in range(48)]
        if jitter:
            pts = [(x + rnd.uniform(-0.03, 0.03), y + rnd.uniform(-0.03, 0.03)) for x, y in pts]
    elif kind == "rect":
        x0, y0, x1, y1 = g
        pts = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
        if jitter:
            pts = wobble(pts)
    else:
        pts = g
    return '<polygon points="' + " ".join(f"{f(X(x))},{f(Y(y))}" for x, y in pts) + '"/>'


# ---------------------------------------------------------------- rock lumps
lumps = []
tries = 0
while len(lumps) < 60 and tries < 20000:
    tries += 1
    px, py = rnd.uniform(XMIN, XMAX), rnd.uniform(YMIN, YMAX)
    d = field(px, py, rockbase)
    if D - 0.9 < d < D - 0.1:
        r = rnd.uniform(0.6, 1.5)
        k = rnd.randint(4, 6)
        a0 = rnd.uniform(0, math.pi)
        lumps.append([(px + r * rnd.uniform(0.6, 1.0) * math.cos(a0 + 2 * math.pi * i / k),
                       py + r * rnd.uniform(0.6, 1.0) * math.sin(a0 + 2 * math.pi * i / k)) for i in range(k)])


def region(width_m, fill):
    """Union of rock base shapes grown by width_m metres."""
    sw = f(2 * width_m * S)
    lw = f(2 * max(width_m - D + 0.6, 0.05) * S)
    return (f'<use href="#rockbase" fill="{fill}" stroke="{fill}" stroke-width="{sw}" stroke-linejoin="miter" stroke-miterlimit="3"/>'
            + f'<g fill="{fill}" stroke="{fill}" stroke-width="{lw}" stroke-linejoin="miter" stroke-miterlimit="3">'
            + "".join('<polygon points="' + " ".join(f"{f(X(x))},{f(Y(y))}" for x, y in L) + '"/>' for L in lumps)
            + "</g>")


# ---------------------------------------------------------------- hatching
highlights = [(rnd.uniform(XMIN, XMAX), rnd.uniform(YMIN, YMAX), rnd.uniform(0.8, 1.8)) for _ in range(70)]


def hatch_lines():
    out = []
    step = 0.8
    y = YMIN
    while y < YMAX:
        x = XMIN
        while x < XMAX:
            cx, cy = x + rnd.uniform(-0.25, 0.25), y + rnd.uniform(-0.25, 0.25)
            x += step
            d = field(cx, cy, rockbase)
            if d < -0.1 or d > D + 1.3:
                continue
            if any(math.hypot(cx - hx, cy - hy) < hr for hx, hy, hr in highlights) and rnd.random() < 0.85:
                continue
            ang = rnd.uniform(0, math.pi)
            n = rnd.randint(3, 5)
            L = rnd.uniform(0.9, 1.4)
            gap = 0.19
            ux, uy = math.cos(ang), math.sin(ang)
            nx, ny = -uy, ux
            for k in range(n):
                o = (k - (n - 1) / 2) * gap
                l2 = L * rnd.uniform(0.75, 1.0) / 2
                mx, my = cx + nx * o, cy + ny * o
                out.append(f"M{f(X(mx - ux * l2))} {f(Y(my - uy * l2))}L{f(X(mx + ux * l2))} {f(Y(my + uy * l2))}")
        y += step
    return out


# ---------------------------------------------------------------- outside band details (dots, dashed grid)
def stipple(n, dmin, dmax):
    out = []
    while len(out) < n:
        px, py = rnd.uniform(XMIN, XMAX), rnd.uniform(YMIN, YMAX)
        d = field(px, py, rockbase)
        if dmin < d < dmax:
            out.append(f'<circle cx="{f(X(px))}" cy="{f(Y(py))}" r="{f(rnd.uniform(1.0, 2.2))}"/>')
    return out


def loose_rocks(n):
    out = []
    placed = 0
    while placed < n:
        px, py = rnd.uniform(XMIN + 1, XMAX - 1), rnd.uniform(YMIN + 1, YMAX - 1)
        d = field(px, py, rockbase)
        if not (D + 1.6 < d < D + 2.6):
            continue
        if field(px, py, floors) < 1.5:
            continue
        r = rnd.uniform(0.35, 0.7)
        k = rnd.randint(6, 8)
        pts = [(px + r * rnd.uniform(0.7, 1.15) * math.cos(2 * math.pi * i / k),
                py + r * rnd.uniform(0.7, 1.15) * math.sin(2 * math.pi * i / k)) for i in range(k)]
        poly = " ".join(f"{f(X(x))},{f(Y(y))}" for x, y in pts)
        lines = []
        ang = rnd.uniform(0, math.pi)
        for j in range(-2, 3):
            o = j * 0.13
            ux, uy = math.cos(ang), math.sin(ang)
            mx, my = px - uy * o, py + ux * o
            l2 = r * 0.6
            lines.append(f"M{f(X(mx - ux * l2))} {f(Y(my - uy * l2))}L{f(X(mx + ux * l2))} {f(Y(my + uy * l2))}")
        out.append(f'<polygon points="{poly}" fill="#8c8c8c" transform="translate(4,4)"/>'
                   f'<polygon points="{poly}" fill="#fff" stroke="#111" stroke-width="3.2" stroke-linejoin="round"/>'
                   f'<path d="{"".join(lines)}" stroke="#111" stroke-width="1.6" stroke-linecap="round"/>')
        placed += 1
    return out


# ---------------------------------------------------------------- features
def line(x1, y1, x2, y2, w=2.0, color="#111", extra=""):
    return f'<line x1="{f(X(x1))}" y1="{f(Y(y1))}" x2="{f(X(x2))}" y2="{f(Y(y2))}" stroke="{color}" stroke-width="{w}" stroke-linecap="round" {extra}/>'


def box(x0, y0, x1, y1, fill="#fff", w=2.4, rx=0, extra=""):
    stroke = "none" if w == 0 else "#111"
    return (f'<rect x="{f(X(x0))}" y="{f(Y(y0))}" width="{f((x1 - x0) * S)}" height="{f((y1 - y0) * S)}" '
            f'rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{w}" {extra}/>')


def column(x, y):
    return (f'<circle cx="{f(X(x) + 3)}" cy="{f(Y(y) + 3)}" r="{f(0.42 * S)}" fill="#8c8c8c"/>'
            f'<circle cx="{f(X(x))}" cy="{f(Y(y))}" r="{f(0.42 * S)}" fill="#fff" stroke="#111" stroke-width="4"/>'
            f'<circle cx="{f(X(x))}" cy="{f(Y(y))}" r="{f(0.17 * S)}" fill="#111"/>')


def sarcophagus(x0, y0, x1, y1, open_lid=False):
    s = box(x0 + 0.06, y0 + 0.06, x1 + 0.06, y1 + 0.06, fill="#8c8c8c", w=0)
    s += box(x0, y0, x1, y1, w=3, rx=5)
    if open_lid:
        s += f'<g transform="rotate(-24 {f(X(x0) + 4)} {f(Y(y0) + 4)})">' + box(x0 + 0.5, y0 + 0.25, x1 + 0.5, y1 - 0.15, w=2.4, rx=4) + "</g>"
        for _ in range(7):
            bx, by = rnd.uniform(x0 - 0.9, x1 + 1.2), rnd.uniform(y1 - 0.2, y1 + 1.3)
            a = rnd.uniform(0, math.pi)
            s += line(bx, by, bx + 0.32 * math.cos(a), by + 0.32 * math.sin(a), w=2.4)
    else:
        s += box(x0 + 0.17, y0 + 0.2, x1 - 0.17, y1 - 0.2, w=1.6, rx=3)
    return s


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


def bones(cx, cy, n, spread):
    s = ""
    for _ in range(n):
        bx, by = cx + rnd.uniform(-spread, spread), cy + rnd.uniform(-spread, spread)
        if rnd.random() < 0.35:
            s += f'<circle cx="{f(X(bx))}" cy="{f(Y(by))}" r="{f(rnd.uniform(2.4, 3.6))}" fill="#fff" stroke="#111" stroke-width="1.6"/>'
        else:
            a = rnd.uniform(0, math.pi)
            l = rnd.uniform(0.15, 0.3)
            s += line(bx - l * math.cos(a), by - l * math.sin(a), bx + l * math.cos(a), by + l * math.sin(a), w=2.2)
    return s


def label(n, x, y, disc=False):
    bg = f'<circle cx="{f(X(x))}" cy="{f(Y(y) - 10)}" r="17" fill="#fff" stroke="#111" stroke-width="2"/>' if disc else ""
    return (bg + f'<text x="{f(X(x))}" y="{f(Y(y))}" class="num" stroke="#fff" stroke-width="6" stroke-linejoin="round">{n}</text>'
            f'<text x="{f(X(x))}" y="{f(Y(y))}" class="num">{n}</text>')


feat = []
# 1 entrance: stairs down from the portico and the forced door
feat.append(stairs(19, -5.0, 21, 3.9, False, 22))
feat.append(f'<g transform="rotate(32 {f(X(19.15))} {f(Y(-0.95))})">' + box(19.15, -1.1, 20.6, -0.8, w=2.2) + "</g>")
feat.append(box(20.65, -1.1, 21.0, -0.8, w=2.2))
for _ in range(6):
    sx, sy = rnd.uniform(19.4, 20.8), rnd.uniform(-0.6, 0.4)
    feat.append(line(sx, sy, sx + 0.18, sy + rnd.uniform(-0.1, 0.1), w=1.6))
# 2 chapel: altar with offering bowl, frescoes (wavy marks) on side walls
feat.append(box(19.06, 6.06, 21.06, 7.06, fill="#8c8c8c", w=0))
feat.append(box(19, 6, 21, 7, w=3))
feat.append(f'<circle cx="{f(X(20))}" cy="{f(Y(6.5))}" r="{f(0.2 * S)}" fill="#fff" stroke="#111" stroke-width="2"/>')
for yy in (5.3, 7.0, 8.7):
    for xx, sgn in ((17.18, 1), (22.82, -1)):
        d = f"M{f(X(xx))} {f(Y(yy - 0.5))}"
        for k in range(4):
            d += f" q{f(sgn * 5)} {f(0.125 * S)} 0 {f(0.25 * S)}"
        feat.append(f'<path d="{d}" fill="none" stroke="#111" stroke-width="1.6"/>')
# 3 corridor: open pit with stakes, ledge along the west wall
feat.append(box(19.5, 14, 21, 16, fill="#2a2a2a", w=3))
for i in range(5):
    for j in range(3):
        px, py = 19.75 + j * 0.5, 14.25 + i * 0.38
        feat.append(line(px - 0.09, py - 0.09, px + 0.09, py + 0.09, w=1.4, color="#fff"))
        feat.append(line(px - 0.09, py + 0.09, px + 0.09, py - 0.09, w=1.4, color="#fff"))
for k in range(5):
    yy = 14.1 + k * 0.45
    feat.append(line(19.62, yy, 19.86, yy + 0.25, w=1.4))   # rotten planks at the edge
# 4 ossuary: bone piles in niches and along the walls, mould in the far west corner
for ax in (4.0, 6.6, 9.2):
    feat.append(bones(ax + 0.6, 18.75, 6, 0.4))
    feat.append(bones(ax + 0.6, 23.3, 6, 0.4))
feat.append(bones(8, 21, 10, 3.5))
for _ in range(150):
    mx, my = rnd.uniform(3.05, 4.6), rnd.uniform(21.3, 22.95)
    feat.append(f'<circle cx="{f(X(mx))}" cy="{f(Y(my))}" r="{f(rnd.uniform(0.8, 1.8))}" fill="#555"/>')
# 5 hall of graves: 4 columns, 4 sarcophagi (NW one opened), stairs down to the east
for cx, cy in ((27.7, 19.7), (30.3, 19.7), (27.7, 22.3), (30.3, 22.3)):
    feat.append(column(cx, cy))
feat.append(sarcophagus(25.6, 17.3, 26.6, 19.3, open_lid=True))
feat.append(sarcophagus(31.4, 17.3, 32.4, 19.3))
feat.append(sarcophagus(25.6, 22.7, 26.6, 24.7))
feat.append(sarcophagus(31.4, 22.7, 32.4, 24.7))
feat.append(stairs(33.0, 20, 37.0, 22, True, 11))
feat.append(f'<path d="M{f(X(34.6))} {f(Y(21))}L{f(X(35.8))} {f(Y(21))}M{f(X(35.4))} {f(Y(20.7))}L{f(X(35.8))} {f(Y(21))}L{f(X(35.4))} {f(Y(21.3))}" '
            f'stroke="#111" stroke-width="2" fill="none" stroke-linecap="round"/>')
# door 5-6 (barricaded) and storeroom contents
feat.append(box(28.55, 25.2, 29.45, 25.5, w=2.4))
feat.append(box(28.4, 26.0, 29.6, 26.9, w=2.4))
feat.append(line(28.4, 26.0, 29.6, 26.9, w=1.6) + line(29.6, 26.0, 28.4, 26.9, w=1.6))
feat.append(f'<g transform="rotate(-8 {f(X(29))} {f(Y(27.2))})">' + box(27.9, 27.05, 30.1, 27.3, w=2.2) + "</g>")
for bx0, by0 in ((27.75, 28.7), (29.7, 28.6), (29.75, 26.1)):
    feat.append(box(bx0, by0, bx0 + 0.6, by0 + 0.8, w=2))
feat.append(f'<circle cx="{f(X(28.3))}" cy="{f(Y(29.2))}" r="{f(0.18 * S)}" fill="#fff" stroke="#111" stroke-width="2"/>')
# 7 antechamber: chains, dog bones, pressure plate (3rd plate before the door), broken seal
for xx in (38.0, 40.5):
    for yy, sgn in ((19.62, 1), (22.38, -1)):
        for k in range(3):
            feat.append(f'<ellipse cx="{f(X(xx + k * 0.22))}" cy="{f(Y(yy + sgn * 0.08))}" rx="3.2" ry="2.2" fill="none" stroke="#111" stroke-width="1.4"/>')
feat.append(bones(37.6, 20.1, 9, 0.35))
feat.append('<g id="secret-plate">' + box(39.08, 20.58, 39.92, 21.42, fill="none", w=2, extra='stroke-dasharray="4 3"')
            + f'<text x="{f(X(39.5))}" y="{f(Y(21.22))}" class="sym">T</text></g>')
feat.append(f'<path d="M{f(X(41.2))} {f(Y(21.85))} a7 7 0 0 1 14 0z" fill="#fff" stroke="#111" stroke-width="1.8"/>')
feat.append(f'<path d="M{f(X(40.9))} {f(Y(22.15))} a7 7 0 0 0 14 0z" fill="#fff" stroke="#111" stroke-width="1.8"/>')
# stone door 7-8, slightly ajar
feat.append(f'<g transform="rotate(14 {f(X(42.05))} {f(Y(20.45))})">' + box(41.9, 20.45, 42.35, 21.55, fill="#bdbdbd", w=2.6) + "</g>")
# 8 tomb: dais, black sarcophagus with lid pushed aside, blood stains
feat.append(f'<circle cx="{f(X(45.6))}" cy="{f(Y(21))}" r="{f(1.75 * S)}" fill="none" stroke="#111" stroke-width="2" stroke-dasharray="6 4"/>')
feat.append(box(44.55, 20.45, 46.75, 21.65, fill="#8c8c8c", w=0))
feat.append(box(44.45, 20.35, 46.65, 21.55, fill="#3a3a3a", w=3, rx=6))
feat.append(f'<g transform="rotate(11 {f(X(45.0))} {f(Y(20.2))})">' + box(44.8, 20.0, 46.9, 21.05, fill="#fff", w=2.6, rx=6) + "</g>")
for _ in range(9):
    bx, by = rnd.uniform(43.3, 47.8), rnd.uniform(18.6, 23.4)
    if math.hypot(bx - 45.6, by - 21) < 2.7 and not (44.2 < bx < 47 and 20 < by < 22):
        feat.append(f'<ellipse cx="{f(X(bx))}" cy="{f(Y(by))}" rx="{f(rnd.uniform(3, 6))}" ry="{f(rnd.uniform(2, 4))}" fill="#9a9a9a"/>')
# 9 crack: a few pebbles along the way
for i in range(1, len(crack_pts) - 1, 2):
    px, py = crack_pts[i]
    feat.append(f'<circle cx="{f(X(px) + rnd.uniform(-3, 3))}" cy="{f(Y(py) + rnd.uniform(-3, 3))}" r="2" fill="#111"/>')

labels = [label(1, 20, 2.3), label(2, 20.0, 9.45), label(3, 20.0, 12.2), label(4, 11.4, 21.6),
          label(5, 29.0, 21.6), label(6, 29.0, 28.6), label(7, 38.15, 22.3), label(8, 46.8, 23.5),
          label(9, 52.4, 23.5, disc=True)]

notes = [
    (20.0, -5.8, "to the top of Birch Hill", "middle"),
    (60.9, 37.9, "to the ravine", "end"),
]

# ---------------------------------------------------------------- legend
legend_rooms = [
    "1  Entrance", "2  Chapel", "3  Corridor with a pit", "4  Ossuary", "5  Hall of graves",
    "6  Storeroom (Corwin's barricade)", "7  Tomb antechamber", "8  Malric's tomb", "9  Crack to the ravine",
]


def legend():
    top = MAP_H + 10
    s = [f'<line x1="40" y1="{f(top)}" x2="{f(W - 40)}" y2="{f(top)}" stroke="#111" stroke-width="2.5"/>']
    s.append(f'<text x="40" y="{f(top + 52)}" class="title">Crypt of House Varn</text>')
    s.append(f'<text x="42" y="{f(top + 82)}" class="sub">scenario “The Crypt”, Birch Hill</text>')
    # scale bar
    sx, sy = 42, top + 128
    for i in range(5):
        s.append(f'<rect x="{f(sx + i * S * 2)}" y="{f(sy)}" width="{f(S * 2)}" height="9" fill="{"#111" if i % 2 == 0 else "#fff"}" stroke="#111" stroke-width="1.5"/>')
    for i, t in ((0, "0"), (5, "10 m")):
        s.append(f'<text x="{f(sx + i * S * 2)}" y="{f(sy + 30)}" class="small" text-anchor="{"start" if i == 0 else "middle"}">{t}</text>')
    s.append(f'<text x="{f(sx)}" y="{f(sy + 54)}" class="small">1 square = 1 m</text>')
    # compass
    cx, cy = 330, top + 150
    s.append(f'<path d="M{cx} {cy - 34}L{cx + 10} {cy}L{cx} {cy - 6}L{cx - 10} {cy}Z" fill="#111"/>')
    s.append(f'<path d="M{cx} {cy + 34}L{cx + 10} {cy}L{cx} {cy + 6}L{cx - 10} {cy}Z" fill="#fff" stroke="#111" stroke-width="1.5"/>')
    s.append(f'<text x="{cx}" y="{cy - 42}" class="small" text-anchor="middle" font-weight="bold">N</text>')
    # rooms
    colx = [520, 800]
    s.append('<g id="legend-rooms">')
    for i, t in enumerate(legend_rooms):
        c = 0 if i < 5 else 1
        r = i if i < 5 else i - 5
        num, name = t.split("  ", 1)
        y = top + 44 + r * 40
        s.append(f'<text x="{colx[c]}" y="{f(y)}" class="lnum">{num}</text>')
        s.append(f'<text x="{colx[c] + 34}" y="{f(y)}" class="ltext">{name}</text>')
    s.append('</g>')
    # symbols
    kx, ky = 1090, top + 30
    items = []
    items.append((f'<rect x="{kx}" y="{ky}" width="28" height="9" fill="#fff" stroke="#111" stroke-width="2.2"/>', "door"))
    items.append((f'<rect x="{kx}" y="{ky}" width="28" height="9" fill="#bdbdbd" stroke="#111" stroke-width="2.6"/>', "stone door"))
    items.append((''.join(f'<line x1="{kx + i * 5}" y1="{ky - 4}" x2="{kx + i * 5}" y2="{ky + 13}" stroke="#111" stroke-width="1.8"/>' for i in range(6)), "stairs"))
    items.append((f'<rect x="{kx}" y="{ky - 5}" width="28" height="18" fill="#2a2a2a" stroke="#111" stroke-width="2.4"/>', "pit"))
    items.append((f'<rect x="{kx}" y="{ky - 3}" width="28" height="14" rx="5" fill="#fff" stroke="#111" stroke-width="3"/>', "sarcophagus"))
    items.append((f'<rect x="{kx + 4}" y="{ky - 6}" width="20" height="20" fill="none" stroke="#111" stroke-width="2" stroke-dasharray="4 3"/><text x="{kx + 14}" y="{ky + 9}" class="sym">T</text>', "pressure plate"))
    out = []
    for i, (g, t) in enumerate(items):
        dy = (i % 3) * 44
        dx = (i // 3) * 190
        gid = ' id="secret-plate-legend"' if t == "pressure plate" else ""
        out.append(f'<g{gid} transform="translate({dx},{dy})">{g}<text x="{kx + 40}" y="{ky + 10}" class="ltext" font-size="17">{t}</text></g>')
    s.extend(out)
    return "\n".join(s)


# ---------------------------------------------------------------- assemble
floors_svg = "".join(shape_svg(s) for s in floors)
rock_svg = "".join(shape_svg(s, jitter=False) for s in rockbase)
hatch = hatch_lines()

full = f'x="{f(X(XMIN))}" y="{f(Y(YMIN))}" width="{f(MAP_W)}" height="{f(MAP_H)}"'
grid = []
for gx in range(int(XMIN), int(XMAX) + 1):
    grid.append(f"M{f(X(gx))} 0V{f(MAP_H)}")
for gy in range(int(YMIN), int(YMAX) + 1):
    grid.append(f"M0 {f(Y(gy))}H{f(MAP_W)}")
grid_d = "".join(grid)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {f(W)} {f(H)}" width="{f(W)}" height="{f(H)}">
<title>Crypt of House Varn</title>
<style>
  .num {{ font: bold 30px Georgia, 'Times New Roman', serif; text-anchor: middle; fill: #111; }}
  .sym {{ font: bold 13px Georgia, serif; text-anchor: middle; fill: #111; }}
  .title {{ font: bold 40px Georgia, 'Times New Roman', serif; fill: #111; letter-spacing: 2px; }}
  .sub {{ font: italic 19px Georgia, 'Times New Roman', serif; fill: #333; }}
  .small {{ font: 15px Georgia, 'Times New Roman', serif; fill: #111; }}
  .lnum {{ font: bold 24px Georgia, 'Times New Roman', serif; fill: #111; }}
  .ltext {{ font: 19px Georgia, 'Times New Roman', serif; fill: #111; }}
  .note {{ font: italic 17px Georgia, 'Times New Roman', serif; fill: #111; }}
</style>
<defs>
  <g id="floors">{floors_svg}</g>
  <g id="rockbase">{rock_svg}</g>
  <mask id="rockmask" maskUnits="userSpaceOnUse" {full}>
    <rect {full} fill="#000"/>{region(D, "#fff")}
  </mask>
  <mask id="bandmask" maskUnits="userSpaceOnUse" {full}>
    <rect {full} fill="#000"/>{region(D + 1.5, "#fff")}{region(D + 0.15, "#000")}
  </mask>
  <mask id="floormask" maskUnits="userSpaceOnUse" {full}>
    <rect {full} fill="#000"/><use href="#floors" fill="#fff"/>
  </mask>
  <mask id="shadowmask" maskUnits="userSpaceOnUse" {full}>
    <rect {full} fill="#000"/><use href="#floors" fill="#fff"/><use href="#floors" fill="#000" transform="translate(7,7)"/>
  </mask>
</defs>
<rect x="0" y="0" width="{f(W)}" height="{f(H)}" fill="#fff"/>
<g id="outer-contours">
  {region(D + 1.62, "#111")}{region(D + 1.5, "#fff")}
  {region(D + 0.84, "#111")}{region(D + 0.75, "#fff")}
</g>
<g id="outer-band" mask="url(#bandmask)">
  <path d="{grid_d}" stroke="#9a9a9a" stroke-width="1" stroke-dasharray="3 4" fill="none"/>
  <g fill="#111">{"".join(stipple(170, D + 0.2, D + 1.4))}</g>
</g>
<g id="loose-rocks">{"".join(loose_rocks(9))}</g>
<g id="rock-shadow" transform="translate(7,7)">{region(D + 0.17, "#8c8c8c")}</g>
<g id="rock-border">{region(D + 0.17, "#111")}{region(D, "#fff")}</g>
<g id="rock-hatch" mask="url(#rockmask)">
  <path d="{"".join(hatch)}" stroke="#111" stroke-width="2.1" stroke-linecap="round" fill="none"/>
</g>
<g id="walls"><use href="#floors" fill="#111" stroke="#111" stroke-width="{f(2 * WALL * S)}" stroke-linejoin="round"/></g>
<use href="#floors" fill="#fff"/>
<g mask="url(#floormask)">
  <path d="{grid_d}" stroke="#a6a6a6" stroke-width="1" fill="none"/>
</g>
<rect {full} fill="#8f8f8f" mask="url(#shadowmask)"/>
<g id="features">{"".join(feat)}</g>
<g id="labels">{"".join(labels)}</g>
<g id="notes">{"".join(f'<text x="{f(X(x))}" y="{f(Y(y))}" class="note" text-anchor="{a}" stroke="#fff" stroke-width="5" stroke-linejoin="round">{t}</text><text x="{f(X(x))}" y="{f(Y(y))}" class="note" text-anchor="{a}">{t}</text>' for x, y, t, a in notes)}</g>
<g id="legend">{legend()}</g>
</svg>
'''
import json


def px_rect(x0, y0, x1, y1):
    return [[round(X(x0), 1), round(Y(y0), 1)], [round(X(x1), 1), round(Y(y0), 1)],
            [round(X(x1), 1), round(Y(y1), 1)], [round(X(x0), 1), round(Y(y1), 1)]]


def px_circle(cx, cy, r, n=16):
    return [[round(X(cx + r * math.cos(2 * math.pi * i / n)), 1), round(Y(cy + r * math.sin(2 * math.pi * i / n)), 1)]
            for i in range(n)]


crack_area = crack_poly(crack_pts, [w + 3.0 for w in crack_w])[1]
areas = {
    "map": "MapCrypt.svg",
    "gm_only": ["labels", "legend-rooms"],
    "always": [[[0, round(MAP_H + 8, 1)], [round(W, 1), round(MAP_H + 8, 1)], [round(W, 1), round(H, 1)], [0, round(H, 1)]]],
    "areas": {
        "1": {"name": "Entrance", "polygons": [px_rect(14.0, -7.6, 26.0, -4.6), px_rect(17.4, -4.6, 22.6, 4.3)]},
        "2": {"name": "Chapel", "polygons": [px_rect(15.6, 2.6, 24.4, 10.3)]},
        "3": {"name": "Corridor with a pit", "polygons": [px_rect(17.6, 9.8, 22.4, 19.6), px_rect(13.6, 18.6, 25.0, 23.4)]},
        "4": {"name": "Ossuary", "polygons": [px_rect(1.6, 16.9, 13.4, 25.1)]},
        "5": {"name": "Hall of graves", "polygons": [px_rect(23.6, 15.6, 34.4, 25.3), px_rect(33.0, 18.6, 36.6, 23.4)]},
        "6": {"name": "Storeroom", "polygons": [px_rect(26.2, 24.6, 31.8, 31.2)]},
        "7": {"name": "Tomb antechamber", "polygons": [px_rect(36.6, 18.1, 42.6, 23.9)]},
        "8": {"name": "Tomb", "polygons": [px_circle(45.6, 21, 4.4)]},
        "9": {"name": "Crack", "polygons": [[[round(X(x), 1), round(Y(y), 1)] for x, y in crack_area], px_rect(56.4, 36.6, 61.6, 38.4)]},
    },
    "secrets": {
        "plate": {"name": "pressure plate in the antechamber (room 7)", "ids": ["secret-plate", "secret-plate-legend"]},
    },
}
def dump(o, ind=0):
    """JSON with every polygon (list of points) or list of strings kept on a single line."""
    pad = "  " * (ind + 1)
    if isinstance(o, dict):
        items = [f"{pad}{json.dumps(k, ensure_ascii=False)}: {dump(v, ind + 1)}" for k, v in o.items()]
        return "{\n" + ",\n".join(items) + "\n" + "  " * ind + "}"
    if isinstance(o, list) and o and not (isinstance(o[0], list) and isinstance(o[0][0], list)):
        return json.dumps(o, ensure_ascii=False)
    if isinstance(o, list):
        return "[\n" + ",\n".join(pad + dump(v, ind + 1) for v in o) + "\n" + "  " * ind + "]"
    return json.dumps(o, ensure_ascii=False)


with open(OUT.replace(".svg", ".areas.json"), "w", encoding="utf-8", newline="\n") as fh:
    fh.write(dump(areas) + "\n")

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(svg)
print(OUT, len(svg) // 1024, "KB", len(hatch), "hatch strokes")
