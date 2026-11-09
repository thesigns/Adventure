"""Generator mapy wyspy Kaldara (styl czarno-białej, ręcznie kreskowanej mapy).

Narzędzie autora, nie do gry. Tworzy plik Settings/Kaldara/MapKaldara.svg.

Użycie:
    python Settings/Kaldara/tools/make_map.py [ścieżka do MapKaldara.svg]

Skala: 1 piksel SVG = 500 m (2 px na kilometr). Wyspa ma 500 km ze wschodu
na zachód (1000 px) i 300 km z północy na południe (600 px), północ u góry.
Generator jest deterministyczny (stałe ziarno losowania), więc bez zmian
w kodzie zawsze tworzy tę samą mapę. Kształt wyspy i krain jest zapisany
w punktach kontrolnych w pikselach w sekcji GEOGRAFIA.

Fonty (licencja SIL OFL 1.1, osadzane w SVG): tools/fonts/UnifrakturMaguntia.ttf
(tytuł) i tools/fonts/GrenzeGotisch.ttf (napisy, z polskimi znakami). Teksty
licencji z informacją o prawach autorskich leżą obok nich: OFL-*.txt.
"""
import base64
import math
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / "MapKaldara.svg"
R = random.Random(1205)

W, H = 1240, 900
INK = "#1b1a17"
PAPER = "#fbf8f0"
PX_PER_KM = 2.0


def f(v):
    return f"{v:.1f}"


def lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


# ------------------------------------------------------------ geometria
def displace(points, closed=True, min_len=3.0, rng=None):
    """Fraktalne przemieszczenie środków odcinków. Punkt: (x, y, r)."""
    rng = rng or R
    out = []
    n = len(points)
    last = n if closed else n - 1

    def rec(a, b, r, acc):
        dx, dy = b[0] - a[0], b[1] - a[1]
        L = math.hypot(dx, dy)
        if L < min_len:
            return
        nx, ny = -dy / L, dx / L
        k = rng.uniform(-1, 1) * L * r
        m = ((a[0] + b[0]) / 2 + nx * k, (a[1] + b[1]) / 2 + ny * k)
        rec(a, m, r, acc)
        acc.append(m)
        rec(m, b, r, acc)

    for i in range(last):
        a = points[i]
        b = points[(i + 1) % n]
        out.append((a[0], a[1]))
        rec((a[0], a[1]), (b[0], b[1]), a[2], out)
    if not closed:
        out.append((points[-1][0], points[-1][1]))
    return out


def fjord(mouth, head, width, bend=0.0, r=0.035, steps=7):
    """Fiord: punkty brzegu od ujścia do końca i z powrotem (ruch zgodny z ruchem wskazówek)."""
    dx, dy = head[0] - mouth[0], head[1] - mouth[1]
    L = math.hypot(dx, dy)
    nx, ny = -dy / L, dx / L
    centre = []
    for i in range(steps + 1):
        t = i / steps
        b = bend * math.sin(math.pi * t) + R.uniform(-1, 1) * 2.0 * (0 < t < 1)
        centre.append((mouth[0] + dx * t + nx * b, mouth[1] + dy * t + ny * b, t))
    left, right = [], []
    for i, (cx, cy, t) in enumerate(centre[:-1]):
        a = centre[i]
        b = centre[i + 1]
        ddx, ddy = b[0] - a[0], b[1] - a[1]
        ll = math.hypot(ddx, ddy)
        px, py = -ddy / ll, ddx / ll
        w = width * (1 - t) ** 0.8 / 2 + 0.8
        left.append((cx + px * w, cy + py * w, r))
        right.append((cx - px * w, cy - py * w, r))
    tip = centre[-1]
    return left + [(tip[0], tip[1], r)] + right[::-1]


def inside(p, poly):
    x, y = p
    res = False
    n = len(poly)
    j = n - 1
    for i in range(n):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if (yi > y) != (yj > y) and x < xi + (y - yi) * (xj - xi) / (yj - yi):
            res = not res
        j = i
    return res


def bbox(poly):
    xs = [p[0] for p in poly]
    ys = [p[1] for p in poly]
    return min(xs), min(ys), max(xs), max(ys)


class Grid:
    """Siatka punktów do szybkiego sprawdzania odległości."""

    def __init__(self, cell=16):
        self.cell = cell
        self.g = {}

    def add(self, p):
        k = (int(p[0] // self.cell), int(p[1] // self.cell))
        self.g.setdefault(k, []).append(p)

    def add_line(self, pts, step=2.5):
        for a, b in zip(pts, pts[1:]):
            n = max(1, int(dist(a, b) / step))
            for i in range(n):
                self.add(lerp(a, b, i / n))
        self.add(pts[-1])

    def near(self, p, d):
        c = self.cell
        r = int(d // c) + 1
        kx, ky = int(p[0] // c), int(p[1] // c)
        for i in range(kx - r, kx + r + 1):
            for j in range(ky - r, ky + r + 1):
                for q in self.g.get((i, j), ()):
                    if (q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2 < d * d:
                        return True
        return False


def path_d(pts, close=True):
    s = "M" + " L".join(f"{f(x)},{f(y)}" for x, y in pts)
    return s + (" Z" if close else "")


def smooth_d(pts):
    d = f"M{f(pts[0][0])},{f(pts[0][1])}"
    for i in range(len(pts) - 1):
        p0 = pts[i - 1] if i > 0 else pts[i]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[i + 2] if i + 2 < len(pts) else pts[i + 1]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{f(c1[0])},{f(c1[1])} {f(c2[0])},{f(c2[1])} {f(p2[0])},{f(p2[1])}"
    return d


def meander(pts, step=9.0, amp=2.2):
    out = [pts[0]]
    for a, b in zip(pts, pts[1:]):
        n = max(1, int(dist(a, b) / step))
        dx, dy = b[0] - a[0], b[1] - a[1]
        L = math.hypot(dx, dy) or 1
        nx, ny = -dy / L, dx / L
        for i in range(1, n + 1):
            p = lerp(a, b, i / n)
            k = R.uniform(-amp, amp) if i < n else 0
            out.append((p[0] + nx * k, p[1] + ny * k))
    return out


def blob(cx, cy, rx, ry, n=14, r=0.12, rot=0.0):
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n
        k = R.uniform(0.82, 1.12)
        x = math.cos(a) * rx * k
        y = math.sin(a) * ry * k
        pts.append((cx + x * math.cos(rot) - y * math.sin(rot),
                    cy + x * math.sin(rot) + y * math.cos(rot), r))
    return displace(pts, min_len=2.0)


# ------------------------------------------------------------ GEOGRAFIA
# Linia brzegowa zgodnie z ruchem wskazówek zegara, od północnego zachodu.
RC = 0.27  # chropowatość zwykłego brzegu
RS = 0.2  # gładszy brzeg południowy (czarne plaże)
coast_ctrl = [
    # półwysep zachodni (ramię), strona północna, i zatoka między nim a półwyspem północno-zachodnim
    (118, 386, RC), (132, 372, RC), (165, 366, RC), (196, 360, RC), (226, 352, RC),
    (242, 338, RC), (238, 318, RC), (214, 312, RC), (190, 316, RC), (160, 322, RC),
    (134, 320, RC), (122, 312, RC), (118, 292, RC),
    # półwysep północno-zachodni z fiordami
    (130, 276, RC),
    *fjord((128, 262), (172, 256), 11, bend=4),
    (126, 240, RC), (140, 222, RC),
    *fjord((144, 210), (184, 214), 10, bend=-4),
    (150, 196, RC), (170, 178, RC), (194, 168, RC),
    *fjord((214, 168), (222, 208), 11, bend=5),
    (236, 158, RC), (262, 152, RC),
    *fjord((282, 158), (288, 204), 11, bend=-4),
    (306, 168, RC), (318, 196, RC), (326, 226, RC),
    # pierwsza wielka zatoka północy
    (334, 250, RC), (356, 264, RC),
    *fjord((372, 262), (384, 286), 9, bend=2),
    (394, 248, RC), (406, 216, RC), (404, 186, RC), (416, 160, RC), (432, 138, RC),
    (444, 126, RC), (464, 122, RC), (478, 140, RC),
    # druga zatoka
    (488, 164, RC), (500, 194, RC),
    *fjord((508, 204), (516, 226), 9, bend=2),
    (528, 200, RC), (536, 172, RC), (548, 146, RC), (566, 128, RC), (584, 120, RC),
    *fjord((604, 120), (612, 212), 18, bend=9),
    (628, 116, RC), (648, 104, RC), (668, 98, RC), (688, 114, RC), (700, 138, RC),
    *fjord((712, 148), (726, 214), 15, bend=-7),
    (744, 148, RC), (760, 130, RC), (780, 124, RC), (796, 140, RC),
    # trzecia zatoka i półwysep północno-wschodni
    (806, 166, RC), (826, 188, RC), (850, 196, RC),
    *fjord((860, 194), (868, 220), 9, bend=2),
    (880, 186, RC), (892, 164, RC), (902, 140, RC), (916, 122, RC), (934, 116, RC),
    (952, 128, RC), (962, 150, RC), (982, 162, RC),
    # mierzeja
    (1004, 166, RC), (1032, 160, RC), (1058, 150, RC), (1074, 148, RC), (1068, 162, RC),
    (1042, 178, RC), (1024, 194, RC), (1032, 214, RC), (1054, 232, RC), (1078, 252, RC),
    # fiordy wschodu
    *fjord((1090, 288), (1028, 296), 14, bend=7),
    (1104, 308, RC), (1116, 322, RC),
    *fjord((1116, 348), (1046, 354), 13, bend=-7),
    (1122, 372, RC), (1128, 388, RC),
    *fjord((1124, 412), (1064, 412), 18, bend=5),
    (1126, 444, RC),
    *fjord((1114, 472), (1056, 481), 12, bend=-6),
    (1106, 500, RC), (1100, 514, RC),
    *fjord((1094, 534), (1046, 542), 12, bend=5),
    (1080, 566, RC), (1062, 586, RC), (1040, 598, RC), (1022, 620, RC), (996, 630, RC),
    (978, 646, RC), (962, 664, RC), (944, 676, RC), (930, 668, RS),
    # południe: czarne plaże, mierzeje i stożki napływowe rzek z lodowca
    (904, 676, RS), (884, 690, RC), (868, 704, RC), (852, 696, RS), (826, 702, RS),
    (796, 708, RS), (770, 724, RC), (750, 716, RS), (725, 722, RC), (702, 735, RC),
    (682, 724, RS), (660, 728, RS), (640, 722, RS), (612, 720, RS), (592, 717, RS),
    (560, 724, RC), (538, 732, RC), (516, 716, RS), (490, 702, RS), (462, 698, RS),
    (436, 704, RC), (414, 690, RS), (384, 671, RS), (340, 656, RC),
    # półwysep południowo-zachodni (hak) i zatoka Hofvik
    (300, 642, RC), (262, 628, RC), (230, 618, RC), (200, 612, RC), (172, 606, RC),
    (146, 596, RC), (124, 580, RC), (116, 560, RC), (128, 546, RC), (150, 548, RC),
    (168, 540, RC), (190, 526, RC), (214, 514, RC), (238, 502, RC), (256, 484, RC),
    (268, 460, RC), (262, 438, RC), (244, 422, RC), (220, 414, RC), (196, 408, RC),
    (168, 402, RC), (140, 398, RC),
]
COAST = displace(coast_ctrl)

ISLETS = []
for cx, cy, rr in [(98, 300, 4), (104, 342, 3), (96, 392, 5), (90, 409, 2.5), (110, 228, 3),
                   (176, 146, 3.5), (334, 148, 3), (448, 100, 4.5), (466, 94, 2), (812, 100, 3),
                   (868, 108, 4.5), (1092, 136, 3), (1148, 300, 3), (1152, 372, 4),
                   (1140, 505, 3), (585, 768, 6), (605, 779, 2.5), (566, 781, 2),
                   (182, 640, 3), (94, 566, 2.5), (1003, 690, 3), (520, 160, 2.5)]:
    if inside((cx, cy), COAST) or min(dist((cx, cy), q) for q in COAST) < rr + 9:
        continue
    ISLETS.append(blob(cx, cy, rr, rr * R.uniform(0.7, 1.0), n=9, r=0.1))


def noisy(ctrl, r=0.14):
    return displace([(x, y, r) for x, y in ctrl], min_len=4.0)


DVERGFJELL = noisy([(430, 330), (480, 302), (540, 296), (600, 292), (660, 296), (720, 291),
                    (790, 302), (850, 322), (880, 350), (872, 390), (832, 420), (782, 440),
                    (722, 455), (660, 459), (600, 457), (540, 450), (480, 440), (442, 410),
                    (422, 370)])
GLACIER = noisy([(520, 478), (570, 466), (640, 461), (720, 468), (792, 488), (814, 526),
                 (800, 556), (770, 572), (745, 596), (724, 590), (700, 584), (668, 596),
                 (645, 614), (622, 598), (596, 588), (568, 590), (548, 604), (530, 586),
                 (508, 550), (500, 510)], 0.08)
HRAUN = noisy([(400, 300), (440, 250), (530, 228), (590, 236), (640, 232), (720, 224),
               (800, 234), (870, 260), (930, 300), (955, 350), (945, 410), (910, 460),
               (850, 505), (805, 515), (700, 430), (560, 430), (505, 505), (470, 480),
               (432, 440), (414, 390), (416, 345)])
VALLEY = [(588, 200), (638, 200), (642, 300), (584, 300)]   # dolina Grimsfjord bez lawy
MARSH = noisy([(540, 632), (600, 618), (680, 622), (760, 630), (792, 660), (760, 690),
               (690, 700), (606, 699), (560, 690), (530, 664)])
FOREST = noisy([(320, 476), (362, 462), (410, 470), (440, 500), (436, 540), (402, 566),
                (352, 561), (318, 536), (304, 500)])
SANDUR = [(440, 600), (900, 560), (960, 650), (440, 700)]
# mniejsze lasy, resztki dawnych brzozowych lasów (osobne ziarno, żeby nie zmieniać reszty mapy)
_RF = random.Random(77)
ULFLUND = displace([(x, y, 0.14) for x, y in [(960, 372), (984, 360), (1008, 364), (1020, 384),
                                               (1008, 404), (982, 407), (962, 395)]], min_len=4.0, rng=_RF)
HVITLUND = displace([(x, y, 0.14) for x, y in [(788, 206), (812, 198), (838, 204), (853, 222),
                                                (846, 241), (822, 247), (798, 239), (785, 222)]], min_len=4.0, rng=_RF)
FORESTS = [FOREST, ULFLUND, HVITLUND]


def in_forest(p):
    return any(inside(p, f) for f in FORESTS)

LAKES = [blob(392, 410, 15, 8, n=12, r=0.1, rot=-0.5), blob(772, 254, 12, 9, n=12, r=0.12)]
# małe, bezimienne czapy lodowe: na zachodnim półwyspie i na wschodnich wyżynach
SMALL_GLACIERS = [blob(156, 379, 15, 8, n=12, r=0.1, rot=-0.15), blob(985, 470, 22, 12, n=14, r=0.1, rot=0.3),
                  blob(662, 150, 11, 7, n=12, r=0.1)]


def in_ice(p):
    return inside(p, GLACIER) or any(inside(p, g) for g in SMALL_GLACIERS)

CITIES = {
    "Hofvik": (283, 452),
    "Grimsfjord": (612, 222),
    "Austhavn": (1050, 413),
    "Myrvaka": (622, 706),
}
TINGVOLD = (382, 372)
BRENNFELL = (650, 392)
VOLCANOES = [(650, 392, 27), (538, 368, 15), (762, 382, 15), (588, 432, 12), (720, 330, 12),
             (880, 302, 11), (472, 264, 10), (930, 420, 10)]
SUBGLACIAL = (612, 515)

RIVERS = [
    [(612, 300), (606, 272), (614, 244), (612, 214), (612, 196)],
    [(470, 330), (446, 356), (416, 386), (398, 404)],
    [(384, 416), (356, 438), (322, 452), (290, 460), (250, 466)],
    [(545, 612), (540, 650), (529, 690), (522, 735)],
    [(642, 624), (649, 660), (645, 700), (650, 745)],
    [(730, 606), (746, 646), (760, 690), (768, 735)],
    [(800, 560), (850, 600), (890, 640), (915, 695)],
    [(872, 396), (920, 420), (980, 426), (1030, 416), (1062, 412), (1090, 412)],
    [(760, 300), (766, 270), (770, 258)],
    [(783, 250), (815, 240), (845, 232), (866, 222), (866, 205)],
    [(440, 300), (412, 292), (386, 284), (380, 266)],
    [(470, 456), (456, 510), (441, 570), (420, 622), (400, 700)],
    [(722, 294), (724, 250), (726, 220), (724, 200)],
    [(478, 300), (486, 262), (502, 240), (515, 226), (512, 210)],
    [(300, 300), (282, 268), (288, 236), (288, 200)],
    [(252, 300), (226, 262), (222, 230), (222, 200)],
    [(958, 345), (1000, 350), (1046, 352), (1080, 352)],
    [(930, 520), (990, 532), (1046, 541), (1080, 540)],
    [(930, 298), (980, 300), (1030, 296), (1070, 294)],
]
ROADS = [
    [(283, 452), (318, 426), (352, 398), (382, 372)],
    [(283, 452), (288, 410), (272, 360), (262, 312), (282, 278), (330, 284), (384, 302),
     (428, 280), (468, 256), (514, 244), (560, 232), (612, 222)],
    [(612, 222), (660, 232), (726, 238), (780, 234), (830, 238), (868, 240), (920, 236),
     (975, 262), (1013, 304), (1026, 352), (1040, 392), (1050, 413)],
    [(1050, 413), (1038, 450), (1040, 488), (1030, 520), (1028, 552), (1000, 592), (952, 630),
     (880, 668), (800, 688), (720, 700), (622, 706)],
    [(622, 706), (560, 698), (490, 684), (430, 664), (370, 640), (322, 612), (292, 562),
     (280, 508), (283, 452)],
]

# ------------------------------------------------------------ napisy
# (tekst, x, y, rozmiar, rozstrzelenie, klasa)
LABELS = [
    ("Hofvik", 283, 478, 19, 0.5, "city"),
    ("Grimsfjord", 612, 248, 19, 0.5, "city"),
    ("Austhavn", 1046, 440, 19, 0.5, "city"),
    ("Myrvaka", 622, 750, 19, 0.5, "city"),
    ("Tingvold", 380, 352, 15, 1.0, "place"),
    ("Brennfell", 650, 410, 14, 1.0, "place"),
    ("Dvergfjell", 640, 318, 28, 7, "region"),
    ("Pustkowia Hraun", 700, 284, 18, 4, "region"),
    ("Pustkowia Hraun", 895, 380, 14, 2, "region"),
    ("Lodowiec", 655, 513, 17, 4, "region"),
    ("Svartjokul", 655, 538, 24, 5, "region"),
    ("Bagna Svartmyr", 668, 663, 15, 2.5, "region"),
    ("Bjarkalund", 372, 520, 16, 2.5, "region"),
    ("Ulflund", 990, 422, 13, 1.5, "region"),
    ("Hvitlund", 820, 262, 13, 1.5, "region"),
    ("Nordstrand", 440, 190, 15, 2, "region"),
    ("Północny Ocean", 620, 66, 24, 9, "sea"),
    ("Kontynent", 1180, 600, 14, 1, "sea"),
]
LABEL_BOXES = []
for text, x, y, size, ls, cls in LABELS:
    w = len(text) * (size * 0.48 + ls)
    LABEL_BOXES.append((x - w / 2 - 4, y - size * 0.85, x + w / 2 + 4, y + size * 0.25))
LABEL_BOXES.append((40, 805, 360, 890))   # tytuł


def in_label(p, pad=0):
    return any(b[0] - pad < p[0] < b[2] + pad and b[1] - pad < p[1] < b[3] + pad
               for b in LABEL_BOXES)


# ------------------------------------------------------------ indeksy odległości
coast_grid = Grid(16)
coast_grid.add_line(COAST + [COAST[0]], step=3)
for isl in ISLETS:
    coast_grid.add_line(isl + [isl[0]], step=2)

RIVER_PTS = [meander(meander(r, step=15, amp=5.5), step=6, amp=1.2) for r in RIVERS]
ROAD_PTS = [meander(r, step=14, amp=1.5) for r in ROADS]
line_grid = Grid(12)
for r in RIVER_PTS + ROAD_PTS:
    line_grid.add_line(r)
for lk in LAKES:
    line_grid.add_line(lk + [lk[0]])

feature_grid = Grid(20)
for c in CITIES.values():
    feature_grid.add(c)
feature_grid.add(TINGVOLD)


def on_land(p, margin=0):
    return inside(p, COAST) and not coast_grid.near(p, margin)


def free(p, coast=4, line=3.5, feat=16, label_pad=2):
    return (on_land(p, coast) and not line_grid.near(p, line) and not feature_grid.near(p, feat)
            and not in_label(p, label_pad))


def scatter(region_bb, step, jitter=0.85):
    x0, y0, x1, y1 = region_bb
    pts = []
    y = y0
    row = 0
    while y <= y1:
        x = x0 + (step / 2 if row % 2 else 0)
        while x <= x1:
            pts.append((x + R.uniform(-jitter, jitter) * step / 2,
                        y + R.uniform(-jitter, jitter) * step / 2))
            x += step
        y += step * 0.87
        row += 1
    return pts


# ------------------------------------------------------------ glify
def mountain(x, y, s):
    h = s * R.uniform(0.85, 1.2)
    w = s * R.uniform(0.55, 0.75)
    px = x + R.uniform(-0.15, 0.15) * w
    left = (x - w, y)
    right = (x + w * R.uniform(0.85, 1.1), y)
    peak = (px, y - h)
    lk = lerp(left, peak, R.uniform(0.4, 0.6))
    lk = (lk[0] + R.uniform(-0.12, 0.08) * w, lk[1] + R.uniform(-0.05, 0.08) * h)
    rk = lerp(peak, right, R.uniform(0.35, 0.6))
    rk = (rk[0] + R.uniform(-0.05, 0.12) * w, rk[1] + R.uniform(-0.06, 0.06) * h)
    out = [left, lk, peak, rk, right]
    spine_end = (px + w * R.uniform(0.05, 0.3), y)
    parts = [f'<path d="{path_d(out)}" fill="{PAPER}" stroke="none"/>',
             f'<path d="{path_d(out, False)}" fill="none" stroke="{INK}" stroke-width="1.05" '
             f'stroke-linejoin="round" stroke-linecap="round"/>']
    hatch = [f"M{f(peak[0])},{f(peak[1])} L{f(spine_end[0])},{f(spine_end[1])}"]
    n = max(3, int(h / 2.2))
    for i in range(1, n):
        t = i / n
        a = lerp(peak, rk, t * 2) if t < 0.5 else lerp(rk, right, (t - 0.5) * 2)
        b = lerp(peak, spine_end, min(1.0, t + 0.06))
        hatch.append(f"M{f(a[0])},{f(a[1])} L{f(b[0])},{f(b[1])}")
    # krótkie kreski na stoku oświetlonym
    for i in range(R.randint(0, 2)):
        t = R.uniform(0.3, 0.8)
        a = lerp(peak, left, t)
        hatch.append(f"M{f(a[0] + 1.5)},{f(a[1] + 0.5)} l{f(w * 0.2)},{f(h * 0.12)}")
    parts.append(f'<path d="{" ".join(hatch)}" stroke="{INK}" stroke-width="0.55" fill="none"/>')
    return "".join(parts)


def volcano(x, y, s, big=False):
    h = s * 0.95
    w = s * 0.85
    tl = (x - w * 0.24, y - h)
    tr = (x + w * 0.24, y - h)
    left = (x - w, y)
    right = (x + w, y)
    mid = lerp(left, tl, 0.5)
    mid = (mid[0] - 1.2, mid[1])
    out = [left, mid, tl, tr, right]
    parts = [f'<path d="{path_d(out)}" fill="{PAPER}"/>',
             f'<path d="{path_d(out, False)}" fill="none" stroke="{INK}" stroke-width="1.15" '
             f'stroke-linejoin="round"/>',
             f'<ellipse cx="{f(x)}" cy="{f(y - h)}" rx="{f(w * 0.24)}" ry="{f(s * 0.07 + 0.6)}" '
             f'fill="{INK}"/>']
    hatch = []
    n = int(h / 1.9)
    for i in range(1, n):
        t = i / n
        a = lerp(tr, right, t)
        b = lerp((x + w * 0.05, y - h), (x + w * 0.25, y), t)
        hatch.append(f"M{f(a[0])},{f(a[1])} L{f(b[0])},{f(b[1])}")
    # żleby lawy na lewym stoku
    for i in range(2 if big else 1):
        a = lerp(tl, tr, 0.3 + 0.2 * i)
        hatch.append(f"M{f(a[0])},{f(a[1] + 1)} q{f(-w * 0.15)},{f(h * 0.4)} {f(-w * 0.35)},{f(h * 0.85)}")
    parts.append(f'<path d="{" ".join(hatch)}" stroke="{INK}" stroke-width="0.6" fill="none"/>')
    # dym
    sx, sy = x, y - h - 2
    smoke = []
    k = 1.6 if big else 1.0
    for i in range(4 if big else 3):
        r0 = (2.2 + i * 1.3) * k
        cx = sx + (i * 3.5 + R.uniform(-1, 1)) * k
        cy = sy - (i * 5.5 + 3) * k
        smoke.append(f"M{f(cx - r0)},{f(cy + r0 * 0.3)} a{f(r0)},{f(r0 * 0.8)} 0 1 1 {f(r0 * 1.6)},{f(-r0 * 0.4)}")
    parts.append(f'<path d="{" ".join(smoke)}" stroke="{INK}" stroke-width="0.8" fill="none" '
                 f'stroke-linecap="round"/>')
    return "".join(parts)


def hill(x, y, s):
    w = s * R.uniform(0.9, 1.2)
    h = s * R.uniform(0.45, 0.6)
    d = f"M{f(x - w)},{f(y)} C{f(x - w * 0.5)},{f(y - h * 1.35)} {f(x + w * 0.4)},{f(y - h * 1.35)} {f(x + w)},{f(y)}"
    hatch = []
    for i in range(3):
        t = 0.55 + i * 0.13
        hx = x - w + 2 * w * t
        hy = y - h * (1 - (2 * t - 1) ** 2) * 1.0
        hatch.append(f"M{f(hx)},{f(hy + 0.8)} l{f(-0.6)},{f(h * 0.55)}")
    return (f'<path d="{d} Z" fill="{PAPER}"/><path d="{d}" fill="none" stroke="{INK}" '
            f'stroke-width="0.9" stroke-linecap="round"/>'
            f'<path d="{" ".join(hatch)}" stroke="{INK}" stroke-width="0.5"/>')


def tree(x, y):
    if R.random() < 0.55:   # świerk
        h = R.uniform(6.5, 9)
        w = h * 0.33
        d = (f"M{f(x)},{f(y - h)} L{f(x - w * 0.6)},{f(y - h * 0.45)} L{f(x - w * 0.3)},{f(y - h * 0.47)} "
             f"L{f(x - w)},{f(y - h * 0.12)} L{f(x + w)},{f(y - h * 0.12)} L{f(x + w * 0.3)},{f(y - h * 0.47)} "
             f"L{f(x + w * 0.6)},{f(y - h * 0.45)} Z")
        return (f'<path d="{d}" fill="{PAPER}" stroke="{INK}" stroke-width="0.7" stroke-linejoin="round"/>'
                f'<path d="M{f(x)},{f(y - h * 0.12)} V{f(y)} M{f(x + 0.6)},{f(y - h * 0.8)} L{f(x + w * 0.5)},{f(y - h * 0.2)}" '
                f'stroke="{INK}" stroke-width="0.6"/>')
    r = R.uniform(2.6, 3.4)   # brzoza
    cy = y - r - 2.2
    return (f'<path d="M{f(x)},{f(cy)} V{f(y)}" stroke="{INK}" stroke-width="0.7"/>'
            f'<ellipse cx="{f(x)}" cy="{f(cy)}" rx="{f(r * 0.85)}" ry="{f(r)}" fill="{PAPER}" '
            f'stroke="{INK}" stroke-width="0.7"/>'
            f'<path d="M{f(x + r * 0.2)},{f(cy - r * 0.5)} l{f(r * 0.3)},{f(r * 0.4)} M{f(x + r * 0.15)},{f(cy)} '
            f'l{f(r * 0.4)},{f(r * 0.45)}" stroke="{INK}" stroke-width="0.5"/>')


def castle(x, y, k=1.0, cliff=False):
    """Ikona miasta: dwie wieże z blankami i mur z bramą. (x, y) to środek podstawy."""
    def T(px, py):
        return f"{f(x + px * k)},{f(y + py * k)}"
    tower = lambda cx: (f"M{T(cx - 3.5, 0)} V{f(y - 17 * k)} H{f(x + (cx - 2.3) * k)} V{f(y - 15.4 * k)} "
                        f"H{f(x + (cx - 0.6) * k)} V{f(y - 17 * k)} H{f(x + (cx + 0.6) * k)} V{f(y - 15.4 * k)} "
                        f"H{f(x + (cx + 2.3) * k)} V{f(y - 17 * k)} H{f(x + (cx + 3.5) * k)} V{f(y)} Z")
    wall = (f"M{T(-6.5, 0)} V{f(y - 9 * k)} H{f(x - 5 * k)} V{f(y - 10.4 * k)} H{f(x - 3 * k)} V{f(y - 9 * k)} "
            f"H{f(x - 1 * k)} V{f(y - 10.4 * k)} H{f(x + 1 * k)} V{f(y - 9 * k)} H{f(x + 3 * k)} "
            f"V{f(y - 10.4 * k)} H{f(x + 5 * k)} V{f(y - 9 * k)} H{f(x + 6.5 * k)} V{f(y)} Z")
    gate = f"M{T(-2, 0)} V{f(y - 3.5 * k)} A{f(2 * k)},{f(2 * k)} 0 0 1 {T(2, -3.5)} V{f(y)} Z"
    win = "".join(f'<rect x="{f(x + (cx - 0.6) * k)}" y="{f(y - 12.5 * k)}" width="{f(1.2 * k)}" '
                  f'height="{f(2.4 * k)}" fill="{INK}"/>' for cx in (-6.5, 6.5))
    s = f'stroke="{INK}" stroke-width="{f(0.9)}" stroke-linejoin="round"'
    base = ""
    if cliff:
        base = (f'<path d="M{T(-14, 0)} L{T(-11, 3)} L{T(-6, 2.5)} L{T(-2, 5)} L{T(4, 3.5)} L{T(9, 5)} '
                f'L{T(14, 2)} L{T(14, 0)} Z" fill="{PAPER}" {s}/>'
                f'<path d="M{T(-8, 1.5)} l{f(1.5 * k)},{f(2.5 * k)} M{T(0, 1.5)} l{f(1.2 * k)},{f(2.6 * k)} '
                f'M{T(7, 1.2)} l{f(1.3 * k)},{f(2.4 * k)}" stroke="{INK}" stroke-width="0.6"/>')
    return (base + f'<path d="{wall}" fill="{PAPER}" {s}/>'
            f'<path d="{tower(-6.5)}" fill="{PAPER}" {s}/><path d="{tower(6.5)}" fill="{PAPER}" {s}/>'
            f'<path d="{gate}" fill="{INK}"/>' + win)


def tingvold_icon(x, y):
    rock = (f"M{f(x - 5)},{f(y)} L{f(x - 4.5)},{f(y - 6)} L{f(x - 1.5)},{f(y - 9)} L{f(x + 2.5)},{f(y - 8)} "
            f"L{f(x + 5)},{f(y - 3)} L{f(x + 5.5)},{f(y)} Z")
    parts = [f'<path d="{rock}" fill="{PAPER}" stroke="{INK}" stroke-width="0.9" stroke-linejoin="round"/>',
             f'<path d="M{f(x + 1.5)},{f(y - 7.5)} L{f(x + 4)},{f(y - 1)} M{f(x + 0.2)},{f(y - 6.5)} '
             f'L{f(x + 2.3)},{f(y - 0.5)}" stroke="{INK}" stroke-width="0.55"/>']
    for dx, dy in ((-13, 3), (11, 2), (-7, 8), (7, 8)):
        tx, ty = x + dx, y + dy
        parts.append(f'<path d="M{f(tx - 3)},{f(ty)} L{f(tx)},{f(ty - 4.5)} L{f(tx + 3)},{f(ty)} Z" '
                     f'fill="{PAPER}" stroke="{INK}" stroke-width="0.7"/>'
                     f'<path d="M{f(tx)},{f(ty - 4.5)} V{f(ty)}" stroke="{INK}" stroke-width="0.5"/>')
    return "".join(parts)


# ------------------------------------------------------------ warstwy
svg = []
add = svg.append


def font_face(name, file):
    data = base64.b64encode((HERE / "fonts" / file).read_bytes()).decode()
    return f"@font-face {{ font-family: '{name}'; src: url(data:font/ttf;base64,{data}) format('truetype'); }}"


add(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">')
add("<!-- Osadzone fonty, licencja SIL Open Font License 1.1 (pełny tekst: tools/fonts/OFL-*.txt):\n"
    "     Grenze Gotisch, Copyright 2020 The Grenze Gotisch Project Authors\n"
    "     (https://github.com/Omnibus-Type/Grenze-Gotisch);\n"
    "     UnifrakturMaguntia, Copyright (c) 2010 j. 'mach' wust, Copyright (c) 2009 Peter Wiegel,\n"
    "     Reserved Font Name UnifrakturMaguntia. -->")
add("<title>Kaldara</title>")
add("<style>")
add(font_face("KaldaraTitle", "UnifrakturMaguntia.ttf"))
add(font_face("KaldaraText", "GrenzeGotisch.ttf"))
add(f"""  text {{ font-family: 'KaldaraText', 'Old English Text MT', serif; fill: {INK}; text-anchor: middle;
          paint-order: stroke; stroke: {PAPER}; stroke-linejoin: round; }}
  text {{ font-weight: 500; }}
  .city {{ stroke-width: 4px; font-weight: 800; }}
  .place {{ stroke-width: 3.5px; font-weight: 600; }}
  .region {{ stroke-width: 4px; font-weight: 700; }}
  .sea {{ stroke-width: 6px; font-weight: 600; }}
  .title {{ font-family: 'KaldaraTitle', 'Old English Text MT', serif; text-anchor: start; stroke-width: 6px; }}
  .leg {{ text-anchor: start; stroke-width: 0; }}""")
add("</style>")

# --- tło i morze
land_d = path_d(COAST)
islet_d = " ".join(path_d(i) for i in ISLETS)
add(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
add("<defs>")
add(f'<mask id="seamask"><rect width="{W}" height="{H}" fill="#fff"/>'
    f'<path d="{land_d}" fill="#000" stroke="#000" stroke-width="34" stroke-linejoin="round"/>'
    f'<path d="{islet_d}" fill="#000" stroke="#000" stroke-width="18" stroke-linejoin="round"/>')
for _ in range(40):   # nieregularne jasne plamy przy brzegu, jak na starych mapach
    p = R.choice(COAST)
    add(f'<ellipse cx="{f(p[0])}" cy="{f(p[1])}" rx="{f(R.uniform(15, 40))}" ry="{f(R.uniform(8, 18))}" fill="#000"/>')
add('<rect x="1000" y="700" width="232" height="190" fill="#000"/></mask>')
add(f'<clipPath id="landclip"><path d="{land_d}"/></clipPath>')
add("</defs>")

sea = []
y = 14.0
while y < H - 12:
    x = 12.0
    while x < W - 12:
        L = R.uniform(25, 150)
        x2 = min(W - 12, x + L)
        wy = R.uniform(-0.9, 0.9)
        sea.append(f"M{f(x)},{f(y)} Q{f((x + x2) / 2)},{f(y + wy)} {f(x2)},{f(y)}")
        x = x2 + R.uniform(2, 9)
    y += R.uniform(3.6, 4.6)
add(f'<path d="{" ".join(sea)}" stroke="{INK}" stroke-width="0.55" fill="none" mask="url(#seamask)"/>')

# --- linie echa brzegu i ląd
add(f'<path d="{land_d}" fill="none" stroke="{INK}" stroke-width="24" stroke-linejoin="round"/>')
add(f'<path d="{land_d}" fill="none" stroke="{PAPER}" stroke-width="22.9" stroke-linejoin="round"/>')
add(f'<path d="{land_d}" fill="none" stroke="{INK}" stroke-width="12" stroke-linejoin="round"/>')
add(f'<path d="{land_d}" fill="none" stroke="{PAPER}" stroke-width="10.8" stroke-linejoin="round"/>')
add(f'<path d="{islet_d}" fill="none" stroke="{INK}" stroke-width="7" stroke-linejoin="round" stroke-dasharray="2 1.5"/>')
add(f'<path d="{islet_d}" fill="none" stroke="{PAPER}" stroke-width="6.2" stroke-linejoin="round"/>')
add(f'<path id="land" d="{land_d}" fill="{PAPER}" stroke="{INK}" stroke-width="1.9" stroke-linejoin="round"/>')
add(f'<path d="{islet_d}" fill="{PAPER}" stroke="{INK}" stroke-width="1.3" stroke-linejoin="round"/>')

# --- lodowiec
gx, gy = sum(p[0] for p in GLACIER) / len(GLACIER), sum(p[1] for p in GLACIER) / len(GLACIER)
add(f'<path d="{path_d(GLACIER)}" fill="{PAPER}" stroke="{INK}" stroke-width="1.1" stroke-dasharray="5 1.5"/>')
for k, dash in ((0.8, "7 4"), (0.58, "5 5"), (0.36, "3 5")):
    ring = [(gx + (x - gx) * k, gy + (y - gy) * k) for x, y in GLACIER]
    add(f'<path d="{path_d(ring)}" fill="none" stroke="{INK}" stroke-width="0.45" stroke-dasharray="{dash}"/>')
crev = []
for p in scatter(bbox(GLACIER), 9):
    if not inside(p, GLACIER) or in_label(p, 3):
        continue
    ring = [(gx + (x - gx) * 0.8, gy + (y - gy) * 0.8) for x, y in GLACIER]
    if inside(p, ring) or dist(p, SUBGLACIAL) < 16:
        continue
    ang = math.atan2(p[1] - gy, p[0] - gx) + math.pi / 2
    dx, dy = math.cos(ang) * 2.2, math.sin(ang) * 2.2
    crev.append(f"M{f(p[0] - dx)},{f(p[1] - dy)} Q{f(p[0] + dy * 0.4)},{f(p[1] - dx * 0.4)} {f(p[0] + dx)},{f(p[1] + dy)}")
add(f'<path d="{" ".join(crev)}" stroke="{INK}" stroke-width="0.55" fill="none"/>')
for g in SMALL_GLACIERS:
    cgx, cgy = sum(p[0] for p in g) / len(g), sum(p[1] for p in g) / len(g)
    ring = [(cgx + (x - cgx) * 0.55, cgy + (y - cgy) * 0.55) for x, y in g]
    add(f'<path d="{path_d(g)}" fill="{PAPER}" stroke="{INK}" stroke-width="1" stroke-dasharray="4 1.5"/>'
        f'<path d="{path_d(ring)}" fill="none" stroke="{INK}" stroke-width="0.45" stroke-dasharray="3 3"/>')
sx, sy = SUBGLACIAL
add(f'<circle cx="{sx}" cy="{sy}" r="9" fill="none" stroke="{INK}" stroke-width="0.7" stroke-dasharray="2 2"/>'
    f'<circle cx="{sx}" cy="{sy}" r="3.5" fill="none" stroke="{INK}" stroke-width="0.7"/>')

# --- pola lawy, czarny piasek, bagna
lava = []
for p in scatter((380, 210, 970, 530), 6.2):
    if not inside(p, HRAUN) or inside(p, DVERGFJELL) or in_ice(p) or inside(p, VALLEY) or in_forest(p):
        continue
    if not free(p, coast=6, line=3.5, feat=14, label_pad=1):
        continue
    if any(dist(p, v[:2]) < v[2] * 0.9 for v in VOLCANOES):
        continue
    r = R.random()
    if r < 0.55:
        L = R.uniform(2.5, 6)
        lava.append(f"M{f(p[0])},{f(p[1])} h{f(L)}")
    elif r < 0.85:
        lava.append(f"M{f(p[0])},{f(p[1])} h0.1 M{f(p[0] + 2.2)},{f(p[1] + 1)} h0.1")
    else:
        lava.append(f"M{f(p[0])},{f(p[1])} l1.5,-1.5 l1.5,1.6 l1.6,-1")
add(f'<path d="{" ".join(lava)}" stroke="{INK}" stroke-width="0.85" stroke-linecap="round" fill="none"/>')

sand = []
for p in scatter((300, 560, 1000, 730), 7):
    if not inside(p, COAST) or in_ice(p) or inside(p, MARSH) or in_label(p, 1):
        continue
    near_beach = coast_grid.near(p, 14) and p[1] > 600 and 330 < p[0] < 990
    if not (inside(p, SANDUR) or near_beach):
        continue
    if line_grid.near(p, 3) or feature_grid.near(p, 14) or coast_grid.near(p, 2.5):
        continue
    if R.random() < (0.75 if near_beach else 0.45):
        sand.append(f"M{f(p[0])},{f(p[1])} h0.1")
add(f'<path d="{" ".join(sand)}" stroke="{INK}" stroke-width="1.1" stroke-linecap="round"/>')

marsh = []
for p in scatter(bbox(MARSH), 9.5):
    if not inside(p, MARSH) or not free(p, coast=5, line=3.5, feat=14, label_pad=1):
        continue
    x, y = p
    marsh.append(f"M{f(x - 3.5)},{f(y)} h7 M{f(x)},{f(y)} v-3.5 M{f(x - 0.4)},{f(y)} l-1.8,-2.6 "
                 f"M{f(x + 0.4)},{f(y)} l1.8,-2.6 M{f(x - 2)},{f(y + 2.6)} h3")
add(f'<path d="{" ".join(marsh)}" stroke="{INK}" stroke-width="0.6" fill="none" stroke-linecap="round"/>')

# łąki i pastwiska: rzadkie kępki trawy na nizinach
grass = []
for p in scatter((110, 140, 1130, 730), 11):
    if inside(p, HRAUN) or in_ice(p) or inside(p, DVERGFJELL) or inside(p, MARSH):
        continue
    if in_forest(p) or inside(p, SANDUR) or not free(p, coast=8, line=4, feat=16, label_pad=3):
        continue
    lowland = p[0] < 470 or (p[1] > 470 and p[0] > 800)
    if R.random() > (0.42 if lowland else 0.12):
        continue
    x, y = p
    grass.append(f"M{f(x - 2)},{f(y)} l-0.8,-2.2 M{f(x)},{f(y)} v-3 M{f(x + 2)},{f(y)} l0.8,-2.2")
add(f'<path d="{" ".join(grass)}" stroke="{INK}" stroke-width="0.5" fill="none" stroke-linecap="round"/>')

# --- rzeki i jeziora
add('<g clip-path="url(#landclip)">')
for r in RIVER_PTS:
    add(f'<path d="{smooth_d(r)}" fill="none" stroke="{INK}" stroke-width="1.15" stroke-linecap="round"/>')
add("</g>")
for lk in LAKES:
    bx = bbox(lk)
    add(f'<clipPath id="lake{int(bx[0])}"><path d="{path_d(lk)}"/></clipPath>')
    add(f'<path d="{path_d(lk)}" fill="{PAPER}"/>')
    hatch = []
    yy = bx[1] + 2.5
    while yy < bx[3]:
        hatch.append(f"M{f(bx[0])},{f(yy)} H{f(bx[2])}")
        yy += 2.6
    add(f'<path d="{" ".join(hatch)}" stroke="{INK}" stroke-width="0.45" clip-path="url(#lake{int(bx[0])})"/>')
    add(f'<path d="{path_d(lk)}" fill="none" stroke="{INK}" stroke-width="1"/>')

# --- rozpadliny Tingvold
rifts = []
for off in (-14, -5, 6, 15):
    a = (TINGVOLD[0] - 22 + off, TINGVOLD[1] + 30 + off * 0.4)
    b = (TINGVOLD[0] + 22 + off, TINGVOLD[1] - 34 + off * 0.4)
    pts = meander([a, b], step=4, amp=1.0)
    if any(dist(p, TINGVOLD) < 11 for p in pts):
        pts = [p for p in pts if dist(p, TINGVOLD) >= 11]
        if len(pts) < 3:
            continue
    rifts.append(path_d(pts, False))
    for p in pts[1:-1:2]:
        rifts.append(f"M{f(p[0])},{f(p[1])} l1.8,0.9")
add(f'<path d="{" ".join(rifts)}" stroke="{INK}" stroke-width="0.7" fill="none"/>')

# --- trakty
for r in ROAD_PTS:
    add(f'<path d="{smooth_d(r)}" fill="none" stroke="{INK}" stroke-width="0.8" stroke-dasharray="3.2 2.4" '
        f'clip-path="url(#landclip)"/>')

# --- glify z porządkiem od tyłu do przodu
glyphs = []   # (y podstawy, svg)
for x, y, s in VOLCANOES:
    glyphs.append((y, volcano(x, y, s, big=s > 20)))
volc_avoid = [(v[0], v[1] - v[2] * 0.4, v[2] * 1.1) for v in VOLCANOES]


def near_volcano(p, extra=0):
    return any(dist(p, (vx, vy)) < r + extra for vx, vy, r in volc_avoid)


# Dvergfjell
cl = [(430, 380), (540, 372), (650, 372), (760, 370), (870, 365)]
for p in scatter(bbox(DVERGFJELL), 10.5):
    if not inside(p, DVERGFJELL) or near_volcano(p, 4) or in_label(p, 4):
        continue
    if line_grid.near(p, 5) or feature_grid.near(p, 14):
        continue
    dcl = min(abs(p[1] - 372), 80)
    s = R.uniform(8, 12) + (80 - dcl) / 80 * 7
    glyphs.append((p[1], mountain(p[0], p[1], s)))

# góry nad fiordami północy i wschodu
for p in scatter((150, 130, 1125, 640), 11):
    north = p[1] < 262 or (p[0] < 320 and p[1] < 318)
    east = p[0] > 940
    if not (north or east):
        continue
    if not on_land(p, 7) or inside(p, HRAUN) or in_ice(p) or inside(p, VALLEY) or in_forest(p):
        continue
    if line_grid.near(p, 5) or feature_grid.near(p, 22) or in_label(p, 4) or near_volcano(p, 3):
        continue
    if not coast_grid.near(p, 60):
        continue
    if R.random() < 0.55:
        glyphs.append((p[1], mountain(p[0], p[1], R.uniform(6.5, 9.5))))
    elif R.random() < 0.6:
        glyphs.append((p[1], hill(p[0], p[1], R.uniform(4.5, 6.5))))

# wzgórza zachodu, południa i pogórza
for p in scatter((120, 180, 1000, 700), 13):
    if p[1] < 262 or (p[0] < 320 and p[1] < 318) or p[0] > 940:
        continue
    if inside(p, HRAUN) or in_ice(p) or inside(p, DVERGFJELL) or inside(p, MARSH):
        continue
    if in_forest(p) or inside(p, SANDUR) or not free(p, coast=10, line=5, feat=22, label_pad=4):
        continue
    if near_volcano(p, 3) or dist(p, TINGVOLD) < 40:
        continue
    near_hills = any(dist(p, q) < 70 for q in [(330, 260), (190, 370), (230, 560), (470, 560),
                                                  (880, 560), (420, 470), (900, 470)])
    if R.random() < (0.75 if near_hills else 0.18):
        glyphs.append((p[1], hill(p[0], p[1], R.uniform(4.5, 7))))

# Bjarkalund, Ulflund i Hvitlund
for forest in FORESTS:
    for p in scatter(bbox(forest), 5.6, jitter=0.7):
        if inside(p, forest) and free(p, coast=6, line=3.5, feat=14, label_pad=2):
            glyphs.append((p[1], tree(p[0], p[1])))
# kępy drzew w ciepłych dolinach zachodu
for cx, cy, rr in ((300, 300, 14), (226, 548, 12), (470, 600, 11), (340, 600, 10)):
    for p in scatter((cx - rr, cy - rr, cx + rr, cy + rr), 5.6, jitter=0.7):
        if dist(p, (cx, cy)) < rr * R.uniform(0.7, 1.0) and free(p, coast=6, line=3.5, feat=14):
            glyphs.append((p[1], tree(p[0], p[1])))

# Osad na mapie nie ma: jest ich dużo wzdłuż wybrzeża i traktów, a MG umieszcza je według potrzeb scenariusza.

glyphs.sort(key=lambda g: g[0])
for _, g in glyphs:
    add(g)

# --- miasta i Tingvold
add(tingvold_icon(*TINGVOLD))
for name, (x, y) in CITIES.items():
    add(castle(x, y, k=1.15 if name == "Austhavn" else 1.0, cliff=name == "Grimsfjord"))

# --- napisy
for text, x, y, size, ls, cls in LABELS:
    extra = ""
    if text == "Kontynent":
        continue
    add(f'<text x="{f(x)}" y="{f(y)}" class="{cls}" font-size="{size}" letter-spacing="{ls}">{text}</text>')
add(f'<text x="45" y="575" class="sea" font-size="22" letter-spacing="9" '
    f'transform="rotate(-90 45 575)">Otwarty Ocean</text>')
add('<text x="1180" y="596" class="sea" font-size="15" letter-spacing="1">ku</text>'
    '<text x="1180" y="614" class="sea" font-size="15" letter-spacing="1">Kontynentowi</text>')
add(f'<path d="M1150,624 H1208 M1201,619 L1210,624 L1201,629" stroke="{INK}" stroke-width="1.1" fill="none"/>')

# --- róża wiatrów
cx, cy = 78, 82
rose = []
for i, ln in enumerate((40, 22, 40, 22, 40, 22, 40, 22)):
    a = -math.pi / 2 + i * math.pi / 4
    tip = (cx + math.cos(a) * ln, cy + math.sin(a) * ln)
    l = (cx + math.cos(a - math.pi / 2) * 5.5, cy + math.sin(a - math.pi / 2) * 5.5)
    r = (cx + math.cos(a + math.pi / 2) * 5.5, cy + math.sin(a + math.pi / 2) * 5.5)
    rose.append((ln, tip, l, r))
rose.sort(key=lambda t: t[0])
add(f'<circle cx="{cx}" cy="{cy}" r="28" fill="{PAPER}" stroke="{INK}" stroke-width="0.8"/>')
add(f'<circle cx="{cx}" cy="{cy}" r="25" fill="none" stroke="{INK}" stroke-width="0.5"/>')
for ln, tip, l, r in rose:
    add(f'<path d="M{f(cx)},{f(cy)} L{f(l[0])},{f(l[1])} L{f(tip[0])},{f(tip[1])} Z" fill="{PAPER}" '
        f'stroke="{INK}" stroke-width="0.8" stroke-linejoin="round"/>'
        f'<path d="M{f(cx)},{f(cy)} L{f(r[0])},{f(r[1])} L{f(tip[0])},{f(tip[1])} Z" fill="{INK}" '
        f'stroke="{INK}" stroke-width="0.8" stroke-linejoin="round"/>')
add(f'<text x="{cx}" y="{cy - 46}" class="place" font-size="16">N</text>')

# --- tytuł
add('<text x="42" y="872" class="title" font-size="96">Kaldara</text>')

# --- legenda
lx, ly, lw, lh = 1000, 700, 228, 188
add(f'<rect x="{lx}" y="{ly}" width="{lw}" height="{lh}" fill="{PAPER}" stroke="{INK}" stroke-width="2.4"/>')
add(f'<rect x="{lx + 4}" y="{ly + 4}" width="{lw - 8}" height="{lh - 8}" fill="none" stroke="{INK}" stroke-width="0.8"/>')
rows = ["Góry", "Wulkany", "Wzgórza", "Lodowce", "Pola lawy", "Czarny piasek",
        "Bagna", "Lasy", "Wody", "Miasta", "Trakty"]
for i, name in enumerate(rows):
    col, row = divmod(i, 6)
    sx = lx + 22 + col * 110
    sy = ly + 26 + row * 19
    if name == "Góry":
        R.seed(3)
        add(mountain(sx - 4, sy + 4, 9) + mountain(sx + 5, sy + 4, 7))
    elif name == "Wulkany":
        add(volcano(sx, sy + 5, 9))
    elif name == "Wzgórza":
        add(hill(sx - 4, sy + 3, 5) + hill(sx + 5, sy + 4, 4.5))
    elif name == "Lodowce":
        add(f'<path d="M{sx - 10},{sy + 4} Q{sx},{sy - 9} {sx + 10},{sy + 4} Z" fill="{PAPER}" stroke="{INK}" '
            f'stroke-width="0.9" stroke-dasharray="5 1.5"/><path d="M{sx - 5},{sy + 2} q1.5,-1 3,0 M{sx + 2},{sy} q1.5,-1 3,0" '
            f'stroke="{INK}" stroke-width="0.55" fill="none"/>')
    elif name == "Pola lawy":
        add(f'<path d="M{sx - 10},{sy - 2} h5 M{sx - 1},{sy - 3} h0.1 M{sx + 3},{sy - 2} h6 M{sx - 7},{sy + 2} h0.1 '
            f'M{sx - 4},{sy + 3} l1.5,-1.5 l1.5,1.6 l1.6,-1 M{sx + 4},{sy + 2} h5" stroke="{INK}" stroke-width="0.85" '
            f'stroke-linecap="round" fill="none"/>')
    elif name == "Czarny piasek":
        add(f'<path d="' + " ".join(f"M{sx + dx},{sy + dy} h0.1" for dx, dy in
                                        ((-9, -2), (-4, 1), (1, -3), (5, 2), (9, -1), (-6, 4), (3, 4))) +
            f'" stroke="{INK}" stroke-width="1.1" stroke-linecap="round"/>')
    elif name == "Bagna":
        add(f'<path d="M{sx - 10},{sy + 2} h7 M{sx - 6.5},{sy + 2} v-3.5 M{sx - 7},{sy + 2} l-1.8,-2.6 M{sx - 6},{sy + 2} '
            f'l1.8,-2.6 M{sx + 2},{sy + 3} h7 M{sx + 5.5},{sy + 3} v-3.5 M{sx + 5},{sy + 3} l-1.8,-2.6 M{sx + 6},{sy + 3} l1.8,-2.6" '
            f'stroke="{INK}" stroke-width="0.6" fill="none"/>')
    elif name == "Lasy":
        R.seed(5)
        add(tree(sx - 6, sy + 5) + tree(sx, sy + 5) + tree(sx + 6, sy + 5))
    elif name == "Wody":
        add(f'<rect x="{sx - 10}" y="{sy - 5}" width="20" height="10" fill="{PAPER}" stroke="{INK}" stroke-width="0.8"/>'
            f'<path d="M{sx - 9},{sy - 2.4} h18 M{sx - 9},{sy} h18 M{sx - 9},{sy + 2.4} h18" stroke="{INK}" stroke-width="0.45"/>')
    elif name == "Miasta":
        add(castle(sx, sy + 6, 0.62))
    elif name == "Trakty":
        add(f'<path d="M{sx - 11},{sy + 1} q11,-6 22,0" fill="none" stroke="{INK}" stroke-width="0.8" '
            f'stroke-dasharray="3.2 2.4"/>')
    add(f'<text x="{sx + 17}" y="{sy + 5}" class="leg" font-size="14">{name}</text>')

# podziałka: 100 km = 200 px
bx, by = lx + 14, ly + 152
add(f'<text x="{lx + lw / 2}" y="{by - 6}" class="leg" font-size="12" style="text-anchor: middle">'
    f'1 piksel = 500 m</text>')
seg = 25 * PX_PER_KM
for i in range(4):
    add(f'<rect x="{f(bx + i * seg)}" y="{by}" width="{f(seg)}" height="5" fill="{INK if i % 2 == 0 else PAPER}" '
        f'stroke="{INK}" stroke-width="0.8"/>')
for i, lab in enumerate(("0", "25", "50", "75", "100 km")):
    anchor = "middle" if i < 4 else "end"
    xx = bx + i * seg + (8 if i == 4 else 0)
    add(f'<text x="{f(xx)}" y="{by + 18}" class="leg" font-size="12" style="text-anchor: {anchor}">{lab}</text>')

# --- ramka
add(f'<rect x="5" y="5" width="{W - 10}" height="{H - 10}" fill="none" stroke="{INK}" stroke-width="2.6"/>')
add(f'<rect x="10" y="10" width="{W - 20}" height="{H - 20}" fill="none" stroke="{INK}" stroke-width="0.8"/>')
add("</svg>")

OUT.write_text("\n".join(svg), encoding="utf-8")
print(f"Zapisano {OUT} ({OUT.stat().st_size // 1024} KB)")
