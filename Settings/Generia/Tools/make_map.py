"""Map generator for the Generia setting.

An author's tool, not for play. Writes Settings/Generia/Maps/ElandriaMap.svg.

Usage:
    python Settings/Generia/Tools/make_map.py

The map uses 1 SVG pixel = 1 km, north up, x grows east and y grows south.

The coastline is the COAST outline broken up by fractal midpoint displacement
with a fixed seed, so the same data always gives the same map. The vertices
of COAST stay in place, so features placed on them later stay on the shore.

The map is being built step by step: for now it has only the coastline and
islands. Mountains, forests, rivers, roads and places come next.
"""

import math
import random
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "Maps" / "ElandriaMap.svg"
W, H = 3500, 2500          # map area in km
M = 400                    # sea margin around the map area
MS = 600                   # sea margin in the south, wider to keep the southern islands clear of the legend
LEGEND_H = 260             # legend strip below the map
LAND = "#f6f0e1"
SEA = "#cfe2f1"
SHALLOW = "#e2eef7"
SHORE = "#4f7fa8"
INK = "#2b2620"

# Main outline, clockwise from the western cape; proportions loosely after Borneo
COAST = [
    # north-west coast running north-east
    (235, 1127), (470, 1216), (706, 1216), (840, 1039), (1100, 980), (1344, 884), (1520, 760),
    (1680, 619), (1915, 552), (2117, 486), (2218, 575), (2386, 265), (2654, 44), (2722, 0),
    # north-eastern peninsula
    (2957, 177), (3091, 309), (3494, 420), (3259, 508), (3125, 641), (2957, 685),
    # east coast with its central bulge
    (2923, 840), (3024, 1149), (3360, 1370), (3394, 1392), (2890, 1547), (2822, 1768),
    (2654, 1901), (2554, 2033), (2486, 2254), (2386, 2387),
    # south coast
    (1915, 2497), (1714, 2343), (1378, 2298), (1150, 2380), (974, 2365), (840, 2254), (437, 2254),
    # western lobe
    (403, 2033), (336, 1856), (34, 1547), (0, 1414), (120, 1250),
]

ISLANDS = [
    [(500, 500), (640, 460), (680, 550), (570, 620), (480, 580)],
    [(1000, 250), (1100, 220), (1130, 290), (1040, 320)],
    [(150, 800), (240, 760), (270, 840), (190, 890)],
    [(3500, 900), (3600, 860), (3640, 950), (3540, 990)],
    [(3000, 2000), (3140, 1950), (3190, 2050), (3070, 2120), (2990, 2080)],
    [(2900, 2400), (2990, 2380), (3010, 2450), (2930, 2480)],
    [(-200, 1900), (-80, 1870), (-50, 1950), (-160, 1990)],
]

# Rough line of the southern coast, for placing islands off it: Silverhaven to Port Seravel, Brenwick to Silverhaven
SOUTH_SHORE = [(1400, 2330), (1500, 2360), (1550, 2405), (1650, 2380), (1750, 2380), (1850, 2425), (1900, 2480),
               (2000, 2482), (2100, 2468), (2150, 2425), (2250, 2385), (2400, 2400), (2450, 2325), (2520, 2260)]
WEST_SHORE = [(740, 2265), (900, 2275), (950, 2340), (1000, 2390), (1150, 2400), (1200, 2345), (1300, 2335),
              (1390, 2325)]


def archipelago(seed, count, line, xs, ys, sizes, clusters, chains, strays):
    """Small islands off a stretch of coast `line`, placed unevenly: clusters, chains and a few strays.

    `sizes` lists (number of islands, smallest radius, largest radius) from the biggest down;
    clusters are (centre, spread x, spread y, weight), chains (from, to, jitter, weight)."""
    rng = random.Random(seed)
    placed, out = [], []

    def shore(x):
        for (x1, y1), (x2, y2) in zip(line, line[1:]):
            if x1 <= x <= x2:
                return y1 + (y2 - y1) * (x - x1) / (x2 - x1)
        return line[-1][1]

    def radius(n):
        for k, lo, hi in sizes:
            if n < k:
                return rng.uniform(lo, hi)
            n -= k
        return rng.uniform(lo, hi)

    tries = 0
    while len(out) < count and tries < 40000:
        tries += 1
        n = len(out)
        r = radius(n)
        pick = rng.uniform(0, sum(c[-1] for c in clusters + chains) + strays)
        for c in clusters + chains:
            pick -= c[-1]
            if pick < 0:
                break
        if pick >= 0:  # a stray anywhere
            x, y = rng.uniform(*xs), rng.uniform(*ys)
        elif len(c) == 4 and isinstance(c[1], tuple):  # a chain
            (ax, ay), (bx, by), jit, _ = c
            f = rng.random()
            x, y = ax + (bx - ax) * f + rng.gauss(0, jit), ay + (by - ay) * f + rng.gauss(0, jit)
        else:
            (cx, cy), sx, sy, _ = c
            x, y = rng.gauss(cx, sx), rng.gauss(cy, sy)
        if not (xs[0] - 20 < x < xs[1] + 20 and shore(x) + 25 + r < y < ys[1] - r):
            continue
        if any(math.dist((x, y), q) < r + qr + 5 for q, qr in placed):
            continue
        placed.append(((x, y), r))
        angle, stretch = rng.uniform(0, math.pi), rng.uniform(1.0, 1.9)
        sides = rng.randint(6, 10)
        poly = []
        for k in range(sides):
            t = 2 * math.pi * k / sides
            d = r * rng.uniform(0.65, 1.15)
            dx, dy = math.cos(t) * d * stretch, math.sin(t) * d / stretch
            poly.append((round(x + dx * math.cos(angle) - dy * math.sin(angle)),
                         round(y + dx * math.sin(angle) + dy * math.cos(angle))))
        out.append(poly)
    return out


# Between Silverhaven and Port Seravel: some seventy islands in uneven groups, like the Aegean
ISLANDS += archipelago(
    7, 72, SOUTH_SHORE, (1440, 2500), (2350, 2860), [(5, 20, 32), (17, 9, 16), (99, 4, 8)],
    [((1600, 2470), 30, 40, 9), ((1990, 2620), 70, 50, 16), ((2060, 2560), 25, 20, 7),
     ((2380, 2480), 35, 25, 7), ((1720, 2790), 50, 35, 6), ((2300, 2780), 20, 20, 4)],
    [((1470, 2560), (1700, 2650), 18, 7), ((2200, 2470), (2450, 2620), 15, 8), ((1850, 2860), (2150, 2700), 22, 6)],
    4)
# Between Brenwick and Silverhaven: a handful of islets
ISLANDS += archipelago(
    11, 9, WEST_SHORE, (780, 1360), (2300, 2650), [(1, 14, 20), (3, 7, 11), (99, 4, 7)],
    [((1060, 2480), 40, 25, 5), ((1270, 2420), 20, 15, 3)],
    [((870, 2330), (980, 2440), 12, 3)],
    1)


# Mountain ranges: main ridge, spurs branching off it, width of the range in km.
# Ironpeaks are young, high and jagged; the Crookback Mountains old and worn.
# A valley separates the two ranges.
RANGES = [
    ("ironpeaks", "Ironpeaks", "peak", 95, 20,
     [(375, 1425), (550, 1462), (675, 1500), (800, 1537), (950, 1462), (1100, 1400), (1300, 1325),
      (1400, 1300), (1500, 1150), (1600, 1050), (1750, 1037), (1900, 1025), (2000, 1050), (2100, 950),
      (2200, 825), (2275, 700), (2325, 650)],
     [[(550, 1462), (550, 1575)], [(775, 1525), (787, 1662)], [(1000, 1437), (1075, 1625)],
      [(987, 1400), (975, 1337)], [(1287, 1275), (1275, 1200)], [(1387, 1325), (1387, 1387)],
      [(1575, 1037), (1575, 975)], [(1887, 1050), (1787, 1387)], [(2087, 850), (2075, 775)],
      [(2212, 800), (2312, 900)]]),
    ("crookback", "Crookback Mountains", "hump", 150, 22,
     [(2200, 1160), (2290, 1215), (2400, 1225), (2550, 1300), (2675, 1400), (2825, 1500)],
     [[(2300, 1200), (2300, 1275)], [(2560, 1290), (2587, 1200)], [(2470, 1260), (2475, 1400)],
      [(2620, 1360), (2625, 1500)]]),
]

GLYPHS = """
  <symbol id="g-peak" overflow="visible"><path d="M-24 0L0 -42L24 0Z" fill="#fff"/><path d="M0 -42L24 0L5 0Z" fill="#cfc4b0"/><path d="M-24 0L0 -42L24 0" fill="none" stroke="#6b604f" stroke-width="3" stroke-linejoin="round"/></symbol>
  <symbol id="g-peak2" overflow="visible"><path d="M-18 0L0 -30L18 0Z" fill="#fff"/><path d="M0 -30L18 0L4 0Z" fill="#cfc4b0"/><path d="M-18 0L0 -30L18 0" fill="none" stroke="#6b604f" stroke-width="3" stroke-linejoin="round"/></symbol>
  <symbol id="g-ash" overflow="visible"><circle cx="-7" r="3" fill="#a8937a"/><circle cx="5" cy="-4" r="2.5" fill="#a8937a"/><circle cx="3" cy="6" r="2" fill="#a8937a"/></symbol>
  <symbol id="g-pine" overflow="visible"><path d="M0 0v6" stroke="#5f6f4c" stroke-width="3"/><path d="M0 -26L12 2H-12Z" fill="#8aa877" stroke="#55704a" stroke-width="2.5" stroke-linejoin="round"/></symbol>
  <symbol id="g-tree" overflow="visible"><path d="M0 0v12" stroke="#6f7f55" stroke-width="3"/><circle cy="-4" r="12" fill="#a9c28d" stroke="#6f8a55" stroke-width="2.5"/></symbol>
  <symbol id="g-reed" overflow="visible"><path d="M-13 0h26M0 0v-15M-7 0l-5 -10M7 0l5 -10" fill="none" stroke="#6f9a86" stroke-width="2.5" stroke-linecap="round"/></symbol>
  <symbol id="g-hill" overflow="visible"><path d="M-24 0Q0 -22 24 0" fill="none" stroke="#7f9a55" stroke-width="3"/></symbol>
  <symbol id="g-hump" overflow="visible"><path d="M-32 0L0 -24L32 0Z" fill="#fff"/><path d="M0 -24L32 0L7 0Z" fill="#d8cfbf"/><path d="M-32 0L0 -24L32 0" fill="none" stroke="#7d7262" stroke-width="3" stroke-linejoin="round"/></symbol>
  <symbol id="g-hump2" overflow="visible"><path d="M-24 0L0 -17L24 0Z" fill="#fff"/><path d="M0 -17L24 0L5 0Z" fill="#d8cfbf"/><path d="M-24 0L0 -17L24 0" fill="none" stroke="#7d7262" stroke-width="3" stroke-linejoin="round"/></symbol>"""


def along(line, step):
    """Points every `step` km along a polyline, with the direction of the segment."""
    out, carry = [], 0.0
    for a, b in zip(line, line[1:]):
        length = math.dist(a, b)
        d = carry
        while d < length:
            t = d / length
            out.append((a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t,
                        (b[0] - a[0]) / length, (b[1] - a[1]) / length))
            d += step
        carry = d - length
    return out


def bend(line, rng, rough=0.14, min_len=40):
    """Open line with gentle random bends; endpoints and vertices stay put."""
    out = []

    def split(a, b):
        length = math.dist(a, b)
        if length < min_len:
            return []
        nx, ny = (a[1] - b[1]) / length, (b[0] - a[0]) / length
        off = rng.uniform(-rough, rough) * length
        mid = ((a[0] + b[0]) / 2 + nx * off, (a[1] + b[1]) / 2 + ny * off)
        return split(a, mid) + [mid] + split(mid, b)

    for a, b in zip(line, line[1:]):
        out.append(a)
        out.extend(split(a, b))
    out.append(line[-1])
    return out


# Map labels: (text, x, y, rotation in degrees, font size)
LABELS = [
    ("IRONPEAKS", 1120, 1280, -20, 28),
    ("CROOKBACK MOUNTAINS", 2490, 1460, 28, 26),
]
KINGDOM_LABEL = ("KINGDOM OF", "VALDREN", 1700, 1800)

REGION_TILT = {"frostmarch": ' transform="rotate(-27 1290 935)"'}

# Regions without a drawn border: (id, name, label x, label y, rough outline for reference only)
REGIONS = [
    ("fenmarch", "THE FENMARCH", 1060, 2075,
     [(980, 1480), (1250, 1480), (1330, 1600), (1290, 1760), (1330, 1950), (1390, 2050), (1400, 2300),
      (1150, 2380), (900, 2330), (800, 2250), (900, 2050), (960, 1800)]),
    ("frostmarch", "FROSTMARCH", 1290, 935,
     [(250, 1150), (470, 1230), (706, 1230), (840, 1060), (1100, 1000), (1344, 900), (1520, 780), (1680, 640),
      (1915, 570), (2117, 500), (2218, 590), (2250, 700), (2100, 900), (1950, 1000), (1600, 1020), (1450, 1180),
      (1150, 1350), (900, 1440), (600, 1420), (350, 1380)]),
    ("harrowlands", "THE HARROWLANDS", 2560, 1660,
     [(1960, 1150), (2200, 1100), (2350, 1280), (2550, 1370), (2700, 1470), (2880, 1550), (2820, 1770),
      (2650, 1900), (2554, 2033), (2480, 1890), (2290, 1830), (2220, 1640), (2100, 1390), (1980, 1300)]),
]


def label_svg(text, x, y, angle, size):
    return (f'<text x="{x}" y="{y}" font-size="{size}" letter-spacing="8" text-anchor="middle" fill="#5e5345" '
            f'stroke="{LAND}" stroke-width="7" paint-order="stroke" transform="rotate({angle} {x} {y})">{text}</text>')


def ragged_band(line, width, rng):
    """Irregular outline around a line: its width wanders along the way and the edge is jagged."""
    samples = along(line, 18) + [(*line[-1], *along(line[-2:], 1e9)[0][2:])]
    left, right = [], []
    wl = wr = 1.0
    for x, y, dx, dy in samples:
        wl = min(1.25, max(0.55, wl + rng.uniform(-0.22, 0.22)))
        wr = min(1.25, max(0.55, wr + rng.uniform(-0.22, 0.22)))
        left.append((x - dy * width / 2 * wl, y + dx * width / 2 * wl))
        right.append((x + dy * width / 2 * wr, y - dx * width / 2 * wr))
    (sx, sy, sdx, sdy), (ex, ey, edx, edy) = samples[0], samples[-1]
    start = (sx - sdx * width * 0.35, sy - sdy * width * 0.35)
    end = (ex + edx * width * 0.35, ey + edy * width * 0.35)
    outline = [start] + left + [end] + right[::-1]
    return [(round(x), round(y)) for x, y in jagged(outline, rng, rough=0.3, min_len=16)]


def range_svg(rid, name, kind, width, step, ridge, spurs, rng):
    ridge = bend(ridge, rng)
    lines = [(ridge, width)] + [(bend(sp, rng), width * 0.7) for sp in spurs]
    base = "".join(f'<polygon points="{pts(ragged_band(l, w * 1.15, rng))}"/>' for l, w in lines)
    marks = []
    for line, w in lines:
        for x, y, dx, dy in along(line, step):
            off = rng.uniform(-0.38, 0.38) * w
            px, py = x - dy * off, y + dx * off
            small = rng.random() < 0.4
            marks.append((py, f'<use href="#g-{kind}{"2" if small else ""}" x="{px:.0f}" y="{py + 18:.0f}"/>'))
    marks.sort()
    ridge_attr = pts(ridge)
    return (f'<g id="range-{rid}" data-name="{name}" data-ridge="{ridge_attr}">'
            f'<g fill="#e6dcc8" stroke="none">{base}</g>'
            + "".join(m for _, m in marks) + "</g>")


# Lakes: one large and two smaller, at the southern foot of the Ironpeaks
LAKES = [
    ("lake-1", [(1150, 1675), (1225, 1612), (1350, 1600), (1450, 1612), (1425, 1675), (1400, 1750),
                (1437, 1812), (1387, 1862), (1375, 1937), (1325, 1950), (1287, 1912), (1325, 1825),
                (1325, 1737), (1250, 1725), (1162, 1712)]),
    ("lake-2", [(912, 1850), (962, 1800), (1050, 1775), (1062, 1850), (1037, 1950), (1000, 1975),
                (962, 1925), (920, 1880)]),
    ("lake-3", [(1100, 1775), (1162, 1762), (1212, 1800), (1230, 1875), (1200, 1900), (1162, 1925),
                (1130, 1887), (1112, 1837)]),
]

# Rivers, from source to mouth (sea or lake); (id, stroke width, points).
# A river whose last point is near the sea is snapped to the nearest point of the coastline.
RIVERS = [
    # north of the Ironpeaks
    ("river-1", 4, [(850, 1450), (825, 1362), (775, 1325), (700, 1275), (620, 1216)]),
    ("river-2", 4, [(1637, 975), (1675, 887), (1750, 862), (1787, 825), (1800, 725), (1790, 590)]),
    # into the lakes
    ("river-3", 4, [(987, 1512), (975, 1662), (1045, 1712), (1040, 1800)]),
    ("river-4", 3, [(1045, 1712), (1110, 1745), (1130, 1800)]),
    ("river-5", 4, [(1075, 1462), (1175, 1525), (1250, 1537), (1262, 1625)]),
    ("river-6", 5, [(1800, 1075), (1712, 1150), (1625, 1237), (1612, 1350), (1562, 1412), (1550, 1500),
                    (1430, 1625)]),
    # out of the lakes to the southern sea
    ("river-7", 5, [(1000, 1960), (962, 2025), (887, 2062), (825, 2112), (720, 2254)]),
    ("river-8", 5, [(1162, 1915), (1137, 2025), (1162, 2100), (1225, 2175), (1250, 2340)]),
    ("river-9", 6, [(1350, 1940), (1400, 2025), (1475, 2100), (1450, 2150), (1425, 2225), (1378, 2298)]),
    # east, from the Ironpeaks to the eastern coast
    ("river-10", 6, [(1937, 1112), (1962, 1200), (1962, 1300), (2012, 1362), (2100, 1387), (2212, 1475),
                     (2225, 1600), (2212, 1675), (2287, 1750), (2287, 1825), (2375, 1887), (2475, 1900),
                     (2537, 1875), (2554, 2033)]),
    # west, from the Ironpeaks through the great elven forest to the south-western coast
    # tributary of the Vael through Kingsbridge; its mouth is snapped onto the Vael (see TRIBUTARIES)
    ("river-12", 4, [(1790, 1420), (1840, 1470), (1900, 1505), (1930, 1530), (1990, 1560), (2060, 1580),
                     (2140, 1605), (2215, 1640)]),
    ("river-11", 5, [(675, 1590), (655, 1655), (585, 1690), (500, 1700), (455, 1745), (430, 1820), (455, 1885),
                     (530, 1915), (590, 1965), (585, 2030), (520, 2075), (470, 2120), (455, 2190), (440, 2250)]),
]

# Land cover: (kind, id, outline). Kinds: forest, marsh, hills.
AREAS = [
    ("forest", "forest-1", [(237, 1350), (275, 1500), (400, 1550), (500, 1625), (600, 1600), (650, 1625),
                            (775, 1675), (950, 1700), (987, 1750), (925, 1800), (900, 1925), (850, 2000),
                            (775, 2037), (675, 2125), (612, 2175), (525, 2087), (450, 1950), (400, 1800),
                            (350, 1650), (225, 1575), (180, 1525), (200, 1425)]),
    ("forest", "forest-2", [(1200, 1462), (1300, 1437), (1425, 1400), (1500, 1325), (1525, 1250), (1587, 1200),
                            (1600, 1250), (1562, 1350), (1500, 1450), (1425, 1537), (1325, 1562), (1250, 1525),
                            (1200, 1487)]),
    ("forest", "forest-3", [(1675, 1350), (1662, 1450), (1650, 1575), (1700, 1625), (1687, 1725), (1625, 1800),
                            (1600, 1862), (1537, 1862), (1487, 1800), (1462, 1700), (1512, 1575), (1600, 1525),
                            (1637, 1425), (1662, 1362)]),
    ("forest", "forest-4", [(1875, 1262), (1912, 1300), (1937, 1387), (1987, 1437), (1962, 1475), (1900, 1462),
                            (1880, 1375)]),
    ("forest", "forest-5", [(1987, 1562), (2037, 1637), (2087, 1700), (2087, 1762), (2050, 1762), (2012, 1700),
                            (1970, 1625)]),
    ("forest", "forest-6", [(2175, 1775), (2212, 1770), (2237, 1825), (2212, 1855), (2175, 1837)]),
    ("forest", "forest-7", [(2412, 2025), (2462, 2025), (2450, 2055), (2420, 2050)]),
    ("forest", "forest-8", [(1837, 1912), (1887, 1912), (1912, 1987), (1887, 2030), (1825, 2012), (1812, 1962)]),
    ("forest", "forest-9", [(2075, 1962), (2125, 1970), (2162, 2012), (2137, 2037), (2087, 2020)]),
    ("forest", "forest-10", [(1237, 1762), (1275, 1775), (1287, 1900), (1350, 2000), (1437, 2075), (1437, 2125),
                             (1387, 2225), (1325, 2237), (1300, 2175), (1350, 2100), (1275, 2000), (1250, 1900),
                             (1237, 1825)]),
    ("forest", "forest-11", [(1412, 1887), (1462, 1900), (1480, 2000), (1450, 2020), (1420, 1962)]),
    ("forest", "forest-12", [(850, 2130), (925, 2137), (1012, 2200), (1000, 2245), (900, 2225), (837, 2175)]),
    ("forest", "forest-13", [(1075, 1695), (1105, 1690), (1100, 1725)]),
    ("marsh", "marsh-1", [(1050, 1937), (1100, 1937), (1125, 2000), (1112, 2087), (1175, 2150), (1187, 2237),
                          (1137, 2225), (1087, 2200), (1025, 2125), (937, 2087), (925, 2062), (1000, 2025),
                          (1045, 1987)]),
    ("marsh", "marsh-2", [(1175, 1962), (1212, 1962), (1237, 2037), (1275, 2125), (1262, 2155), (1225, 2137),
                          (1187, 2062)]),
    # coniferous forests north of the Ironpeaks, between the mountains and the coast
    ("taiga", "taiga-1", [(420, 1300), (600, 1290), (760, 1290), (880, 1125), (1000, 1095), (1100, 1065),
                          (1100, 1120), (1000, 1230), (900, 1270), (800, 1390), (650, 1380), (480, 1350), (420, 1330)]),
    ("taiga", "taiga-2", [(1180, 1040), (1350, 980), (1500, 910), (1650, 780), (1800, 710), (1930, 670), (2010, 660),
                          (2000, 720), (1940, 860), (1850, 920), (1700, 890), (1620, 860), (1520, 870), (1430, 1000),
                          (1350, 1060), (1270, 1080), (1180, 1090)]),
    # blasted wastes beyond the Crookback Mountains, up to the north-eastern coast
    ("ash", "ashlands", [(2250, 700), (2300, -200), (3700, -200), (3700, 1450), (2859, 1438), (2709, 1338),
                         (2584, 1238), (2434, 1163), (2324, 1153), (2234, 1098), (2240, 900)]),
    ("hills", "hills-1", [(1612, 2200), (1775, 2087), (1862, 2075), (1950, 1937), (2000, 1937), (2037, 2062),
                          (2150, 2062), (2250, 2012), (2300, 2020), (2375, 2150), (2250, 2175), (2125, 2250),
                          (2000, 2237), (1875, 2200), (1750, 2225), (1625, 2225)]),
]

# Names of land cover areas; big ones get spaced capitals, the rest small italics
AREA_NAMES = {
    "forest-1": ("ELENWOOD", True), "forest-2": ("Highwood", False), "forest-3": ("Blackwood", False),
    "forest-4": ("Fernwood", False), "forest-5": ("Hartwood", False), "forest-6": ("Elmwood", False),
    "forest-7": ("Birchwood", False), "forest-8": ("Bramblewood", False), "forest-9": ("Hazelwood", False),
    "forest-10": ("Silverwood", False), "forest-11": ("Alderwood", False), "forest-12": ("Southwood", False),
    "forest-13": ("Mistwood", False), "taiga-1": ("Coldpines", False), "taiga-2": ("Frostwood", False),
    "hills-1": ("GREENHOLLOW", True), "ashlands": ("ASHLANDS", True),
}
# Label positions where the middle of the outline is a poor spot; None hides the label of a tiny area
AREA_LABEL_AT = {"ashlands": (2790, 760), "hills-1": (2150, 2150), "forest-5": (2060, 1795), "forest-6": (2205, 1890), "taiga-1": (600, 1345), "taiga-2": (1640, 850), "forest-13": None}

# (fill, glyph, spacing in km)
COVER = {"ash": ("#ebe4da", "ash", 62), "taiga": ("#dce6d6", "pine", 30), "forest": ("#dbe7c9", "tree", 34), "marsh": ("#dde7de", "reed", 34), "hills": ("#e3edcc", "hill", 40)}

# Names of lakes and rivers, with where along the river its label sits (0-100%)
LAKE_NAMES = {"lake-1": ("Silvermere", 1330, 1690, 30), "lake-2": ("Mistmere", 990, 1880, 22),
              "lake-3": ("Reedmere", 1170, 1850, 20)}
RIVER_NAMES = {
    "river-1": ("Coldwater", 50), "river-2": ("Frostrun", 55), "river-3": ("Mistbrook", 45),
    "river-4": ("Reedbrook", 50), "river-5": ("Highrun", 45), "river-6": ("Aldwater", 50),
    "river-7": ("Brenna", 55), "river-8": ("Wend", 60), "river-9": ("Silverrun", 50),
    "river-10": ("Vael", 50), "river-11": ("Aelwen", 45), "river-12": ("Kingswater", 62),
}

# Places: (id, name, kind, x, y, label anchor, label dx, label dy). Kinds: capital, city, town, hold, fort.
PLACES = [
    ("kingsbridge", "Kingsbridge", "capital", 1930, 1530, "middle", 0, -32),
    ("mereton", "Mereton", "city", 1468, 1598, "start", 20, -16),
    ("hollowbury", "Hollowbury", "town", 2020, 2000, "end", -16, 8),
    # town where the Mereton road meets the road south from Kingsbridge, at the western edge of Hartwood
    ("crossholt", "Crossholt", "town", 1912, 1640, "end", -16, -14),
    # market town at the crossroads where the Port Seravel road meets the Hollowbury road
    ("hartwell", "Hartwell", "town", 1928, 1760, "end", -16, 8),
    # halfling town in western Greenhollow, halfway along the road from Hollowbury to Silverhaven
    ("applecombe", "Applecombe", "town", 1700, 2165, "start", 16, 28),
    # lake port on the eastern shore of Silvermere, west of the northern tip of Alderwood
    ("alderwick", "Alderwick", "town", 1385, 1885, "end", -16, -12),
    # frontier towns beyond Valdren
    ("twinbrook", "Twinbrook", "town", 1078, 1760, "end", -18, 26),
    ("harrowford", "Harrowford", "town", 2240, 1580, "start", 16, 8),
    ("rimehaven", "Rimehaven", "town", 1850, 630, "start", 16, 14),
    # ports on the southern coast
    ("silverhaven", "Silverhaven", "city", 1378, 2298, "start", 20, -12),
    ("port-seravel", "Port Seravel", "city", 2554, 2033, "end", -20, 34),
    ("brenwick", "Brenwick", "town", 739, 2248, "end", -16, -10),
    ("aelindor", "Aelindor", "city", 488, 1810, "start", 20, 8),
    # dwarven holds in the Ironpeaks
    ("khaz-dorun", "Khaz Dorun", "hold", 1690, 1045, "middle", 0, 46),
    ("durnhold", "Durnhold", "hold", 1010, 1365, "end", -20, -12),
    # the gnomes' home in the western Ironpeaks, north of Elenwood
    ("brasshollow", "Brasshollow", "town", 470, 1455, "middle", 0, -22),
    # the way into the Ashlands: the valley between the ranges and a pass over the Crookback Mountains
    ("ashgate", "Ashgate", "fort", 2175, 1110, "end", -20, 8),
    ("crows-pass", "Crow's Pass", "pass", 2515, 1262, "start", 18, -16),
    # the pass over the Ironpeaks under Khaz Dorun, between Valdren and the Frostmarch
    ("thanes-pass", "Thane's Pass", "pass", 1780, 1030, "start", 18, 8),
    # ruins of the Empire of Aurelion
    ("aurelion", "Aurelion", "ruin", 3200, 1370, "start", 20, 8),
    ("drowned-spires", "Drowned Spires", "ruin", 1075, 2115, "start", 18, 8),
    ("hollow-crown", "Hollow Crown", "ruin", 380, 1270, "middle", 0, 38),
    ("lonely-tower", "Lonely Tower", "ruin", 2958, 2430, "middle", 0, -24),
    ("sunstone", "Sunstone", "ruin", 2620, 1700, "start", 18, 8),
]

# Roads: (id, from, to, points); drawn as dotted brown lines, with their length in km.
# Only the broad highways of Valdren are drawn; beyond the kingdom there are only tracks and paths.
ROADS = [
    # branches off the Hollowbury road at Crossholt, so every main road meets one trunk road before Kingsbridge
    ("road-crossholt-mereton", "Crossholt", "Mereton",
     [(1912, 1640), (1820, 1652), (1730, 1645), (1620, 1655), (1530, 1630), (1468, 1598)]),
    ("road-kingsbridge-hollowbury", "Kingsbridge", "Hollowbury",
     [(1930, 1530), (1912, 1640), (1928, 1760), (1965, 1880), (2020, 2000)]),
    # branches off the Hollowbury road at Hartwell, level with Hartwood, runs between Hazelwood and Elmwood
    ("road-hartwell-seravel", "Hartwell", "Port Seravel",
     [(1928, 1760), (2010, 1805), (2095, 1860), (2165, 1908), (2270, 1928), (2380, 1945), (2480, 1995),
      (2554, 2033)]),
    ("road-hollowbury-silverhaven", "Hollowbury", "Silverhaven",
     [(2020, 2000), (1850, 2075), (1700, 2165), (1520, 2225), (1378, 2298)]),
    # east between Alderwood and Blackwood, then north-east to Hartwell
    ("road-hartwell-alderwick", "Hartwell", "Alderwick",
     [(1928, 1760), (1850, 1852), (1760, 1882), (1640, 1885), (1530, 1880), (1450, 1878), (1385, 1885)]),
    # straight east north of the Kingswater, then south-east to the ford over the Vael at Harrowford
    ("road-kingsbridge-harrowford", "Kingsbridge", "Harrowford",
     [(1930, 1530), (1990, 1520), (2080, 1518), (2160, 1522), (2240, 1580)]),
]

# Rivers that end in another river: their last point is moved onto that river's course
TRIBUTARIES = {"river-12": "river-10"}

WATER = "#bcd6ec"
RIVER = "#3b78b5"


def to_coast(line, coast, reach=120):
    """Move the river's last point onto the nearest coastline point, if the coast is close."""
    end = line[-1]
    near = min(coast, key=lambda c: math.dist(c, end))
    if math.dist(near, end) > reach:
        return line
    return line[:-1] + [(round(near[0]), round(near[1]))]


def inside(x, y, poly):
    result = False
    for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1]):
        if (y1 > y) != (y2 > y) and x < x1 + (y - y1) * (x2 - x1) / (y2 - y1):
            result = not result
    return result


def seg_dist(p, a, b):
    ax, ay, bx, by, px, py = *a, *b, *p
    dx, dy = bx - ax, by - ay
    t = max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy or 1)))
    return math.dist(p, (ax + t * dx, ay + t * dy))


def smooth(points):
    """Closed Catmull-Rom curve through all vertices, as cubic Bezier segments."""
    n = len(points)
    d = [f"M{points[0][0]} {points[0][1]}"]
    for i in range(n):
        p0, p1, p2, p3 = (points[(i + k) % n] for k in (-1, 0, 1, 2))
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d.append(f"C{c1[0]:.0f} {c1[1]:.0f} {c2[0]:.0f} {c2[1]:.0f} {p2[0]} {p2[1]}")
    return "".join(d) + "Z"


def cover_svg(kind, aid, poly, rng, rivers, lakes):
    """Land cover area: soft outline fill plus scattered symbols, kept off rivers and lakes."""
    fill, sym, spacing = COVER[kind]
    shape = [(round(x), round(y)) for x, y in jagged(poly, rng, rough=0.18, min_len=40)]
    xs, ys = [x for x, _ in shape], [y for _, y in shape]
    marks = []
    y, row = min(ys) + spacing / 2, 0
    while y < max(ys):
        x = min(xs) + spacing / 2 + (spacing / 2 if row % 2 else 0)
        while x < max(xs):
            px, py = x + rng.uniform(-0.3, 0.3) * spacing, y + rng.uniform(-0.3, 0.3) * spacing
            if inside(px, py, shape) and inside(px, py, LAND_SHAPE) and not any(inside(px, py, l) for l in lakes) \
                    and all(seg_dist((px, py), a, b) > 22 for r in rivers for a, b in zip(r, r[1:])):
                marks.append((py, f'<use href="#g-{sym}" x="{px:.0f}" y="{py:.0f}"/>'))
            x += spacing
        y += spacing * 0.8
        row += 1
    marks.sort()
    name = AREA_NAMES.get(aid, ("", False))[0].title() if aid in AREA_NAMES else ""
    data_name = f' data-name="{name}"' if name else ""
    return (f'<g id="{aid}" data-kind="{kind}"{data_name}><path d="{smooth(shape)}" fill="{fill}"/>'
            + "".join(m for _, m in marks) + "</g>")


def cross(a, b, c, d):
    """Intersection point of segments ab and cd, or None."""
    r = (b[0] - a[0], b[1] - a[1])
    q = (d[0] - c[0], d[1] - c[1])
    den = r[0] * q[1] - r[1] * q[0]
    if den == 0:
        return None
    t = ((c[0] - a[0]) * q[1] - (c[1] - a[1]) * q[0]) / den
    u = ((c[0] - a[0]) * r[1] - (c[1] - a[1]) * r[0]) / den
    if 0 <= t <= 1 and 0 <= u <= 1:
        return (a[0] + t * r[0], a[1] + t * r[1])
    return None


def clip_to_land(line, coast):
    """Cut a river where it first leaves the land, so its mouth lies exactly on the shore."""
    edges = list(zip(coast, coast[1:] + coast[:1]))
    for i, (a, b) in enumerate(zip(line, line[1:])):
        if inside(*a, coast) and not inside(*b, coast):
            hits = [h for c, d in edges if (h := cross(a, b, c, d))]
            mouth = min(hits, key=lambda h: math.dist(a, h)) if hits else b
            return line[:i + 1] + [(round(mouth[0]), round(mouth[1]))]
    return line


def open_curve(points):
    """Open Catmull-Rom curve through all points, as a path for text to follow."""
    ext = [points[0]] + list(points) + [points[-1]]
    d = [f"M{points[0][0]} {points[0][1]}"]
    for i in range(1, len(ext) - 2):
        p0, p1, p2, p3 = ext[i - 1], ext[i], ext[i + 1], ext[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d.append(f"C{c1[0]:.0f} {c1[1]:.0f} {c2[0]:.0f} {c2[1]:.0f} {p2[0]} {p2[1]}")
    return "".join(d)


def point_at(line, frac):
    """Point at a fraction of a polyline's length."""
    total = sum(math.dist(a, b) for a, b in zip(line, line[1:]))
    goal = total * frac
    for a, b in zip(line, line[1:]):
        length = math.dist(a, b)
        if goal <= length and length:
            t = goal / length
            return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
        goal -= length
    return line[-1]


def river_label(rid, line):
    """River name in small italics beside its course, turned along the river and never upside down."""
    name, offset = RIVER_NAMES[rid]
    total = sum(math.dist(a, b) for a, b in zip(line, line[1:]))
    span = min(0.08, 45 / total)
    a, b = point_at(line, offset / 100 - span), point_at(line, offset / 100 + span)
    x, y = point_at(line, offset / 100)
    angle = math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))
    if angle > 90:
        angle -= 180
    elif angle < -90:
        angle += 180
    nx, ny = -math.sin(math.radians(angle)), math.cos(math.radians(angle))
    x, y = x - nx * 16, y - ny * 16
    return (f'<text x="{x:.0f}" y="{y:.0f}" font-size="20" font-style="italic" letter-spacing="2" fill="#2f5f8a" '
            f'stroke="{LAND}" stroke-width="6" paint-order="stroke" text-anchor="middle" '
            f'transform="rotate({angle:.0f} {x:.0f} {y:.0f})">{name}</text>')


def area_label(aid, poly):
    """Name of a land cover area at the middle of its outline."""
    if aid not in AREA_NAMES:
        return ""
    name, big = AREA_NAMES[aid]
    if aid in AREA_LABEL_AT:
        if AREA_LABEL_AT[aid] is None:
            return ""
        x, y = AREA_LABEL_AT[aid]
    else:
        x = sum(p[0] for p in poly) / len(poly)
        y = sum(p[1] for p in poly) / len(poly)
    style = ('font-size="34" letter-spacing="10"' if big
             else 'font-size="19" font-style="italic" letter-spacing="1"')
    color = "#6b5a46" if aid == "ashlands" else "#3f5a2e"
    return (f'<text x="{x:.0f}" y="{y:.0f}" {style} text-anchor="middle" fill="{color}" stroke="{LAND}" '
            f'stroke-width="7" paint-order="stroke">{name}</text>')


def nearest_index(points, p):
    return min(range(len(points)), key=lambda i: math.dist(points[i], p))


def valdren_outline(coast, rivers, lake):
    """Kingdom of Valdren: between Silvermere with the Silverrun and Aldwater on the west and the Vael
    on the east, from the Ironpeaks down to the southern coast."""
    aldwater, silverrun, vael = rivers["river-6"], rivers["river-9"], rivers["river-10"]
    i_v, i_s = nearest_index(coast, vael[-1]), nearest_index(coast, silverrun[-1])
    shore = coast[i_v:i_s + 1] if i_v <= i_s else coast[i_v:] + coast[:i_s + 1]
    a, b = nearest_index(lake, silverrun[0]), nearest_index(lake, aldwater[-1])
    step = 1 if (b - a) % len(lake) < len(lake) / 2 else -1
    lake_side, i = [], a
    while i != b:
        lake_side.append(lake[i])
        i = (i + step) % len(lake)
    lake_side.append(lake[b])
    outline = list(vael) + shore[1:-1] + list(silverrun[::-1]) + lake_side + list(aldwater[::-1])
    border = list(silverrun[::-1]) + lake_side + list(aldwater[::-1]) + list(vael)
    return outline, border


def place_svg(pid, name, kind, x, y, anchor, dx, dy):
    if kind == "capital":
        mark = (f'<circle cx="{x}" cy="{y}" r="17" fill="#fff" stroke="{INK}" stroke-width="5"/>'
                f'<circle cx="{x}" cy="{y}" r="7" fill="{INK}"/>')
    elif kind == "city":
        mark = f'<circle cx="{x}" cy="{y}" r="12" fill="{INK}" stroke="#fff" stroke-width="3"/>'
    elif kind == "hold":
        mark = f'<path d="M{x - 15} {y + 11}L{x} {y - 15}L{x + 15} {y + 11}Z" fill="{INK}" stroke="#fff" stroke-width="3"/>'
    elif kind == "ruin":
        mark = (f'<path d="M{x - 12} {y + 9}V{y - 4}A12 12 0 0 1 {x + 12} {y - 4}V{y + 9}" fill="none" stroke="#fff" '
                f'stroke-width="8"/><path d="M{x - 12} {y + 9}V{y - 4}A12 12 0 0 1 {x + 12} {y - 4}V{y + 9}" fill="none" '
                f'stroke="{INK}" stroke-width="3.5" stroke-dasharray="11 5"/>'
                f'<path d="M{x - 16} {y + 10}H{x + 16}" stroke="{INK}" stroke-width="3"/>')
    elif kind == "pass":
        mark = (f'<path d="M{x - 14} {y - 12}Q{x - 4} {y} {x - 14} {y + 12}M{x + 14} {y - 12}Q{x + 4} {y} {x + 14} {y + 12}" '
                f'fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round"/>'
                f'<path d="M{x - 14} {y - 12}Q{x - 4} {y} {x - 14} {y + 12}M{x + 14} {y - 12}Q{x + 4} {y} {x + 14} {y + 12}" '
                f'fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>')
    elif kind == "fort":
        mark = f'<rect x="{x - 11}" y="{y - 11}" width="22" height="22" fill="{INK}" stroke="#fff" stroke-width="3"/>'
    else:
        mark = f'<circle cx="{x}" cy="{y}" r="8" fill="#fff" stroke="{INK}" stroke-width="4"/>'
    size, weight = (32, ' font-weight="bold"') if kind == "capital" else (24, "")
    if kind in ("ruin", "pass"):
        size, weight = 21, ' font-style="italic"'
    label = (f'<text x="{x + dx}" y="{y + dy}" font-size="{size}"{weight} text-anchor="{anchor}" fill="{INK}" '
             f'stroke="{LAND}" stroke-width="8" paint-order="stroke">{name}</text>')
    return f'<g id="place-{pid}" data-name="{name}" data-kind="{kind}" data-x="{x}" data-y="{y}">{mark}{label}</g>'


def summary(river_lines, road_lines):
    """Plain-text digest of the map for the GM: places with coordinates, roads and rivers with lengths."""
    out = ["Elandria, continent of Generia, 1 px = 1 km, north up, x east, y south. Places (x, y in km):"]
    out += [f"  {name} ({kind}): {x}, {y}" for _, name, kind, x, y, *_ in PLACES]
    out.append("Roads (km):")
    for (_, a, b, _), line in zip(ROADS, road_lines):
        out.append(f"  {a} - {b}: {km(line)}{junction(line[0], road_lines)}")
    out.append("Rivers, source to mouth (km):")
    out += [f"  {RIVER_NAMES[rid][0]}: {km(line)}" for (rid, _, _), line in zip(RIVERS, river_lines)]
    return "\n".join(out)


def junction(start, road_lines):
    """Where a branch road starts on another road: ' (joins the A - B road N km from A)', or ''."""
    for (_, a, b, _), line in zip(ROADS, road_lines):
        if start in line[1:-1]:
            return f" (joins the {a} - {b} road {km(line[:line.index(start) + 1])} km from {a})"
    return ""


def km(points):
    return round(sum(math.dist(a, b) for a, b in zip(points, points[1:])))


def pts(points):
    return " ".join(f"{x:.0f},{y:.0f}" for x, y in points)


def jagged(points, rng, rough=0.32, min_len=22):
    """Closed outline with each edge broken up by midpoint displacement; vertices stay put."""
    out = []

    def split(a, b):
        length = math.dist(a, b)
        if length < min_len:
            return []
        nx, ny = (a[1] - b[1]) / length, (b[0] - a[0]) / length
        off = rng.uniform(-rough, rough) * length
        mid = ((a[0] + b[0]) / 2 + nx * off, (a[1] + b[1]) / 2 + ny * off)
        return split(a, mid) + [mid] + split(mid, b)

    for a, b in zip(points, points[1:] + points[:1]):
        out.append(a)
        out.extend(split(a, b))
    return out


def compass(cx, cy):
    return (f'<g id="compass">'
            f'<circle cx="{cx}" cy="{cy}" r="58" fill="none" stroke="{INK}" stroke-width="2"/>'
            f'<path d="M{cx} {cy - 80}L{cx + 14} {cy}L{cx} {cy - 10}L{cx - 14} {cy}Z" fill="{INK}"/>'
            f'<path d="M{cx} {cy + 80}L{cx + 14} {cy}L{cx} {cy + 10}L{cx - 14} {cy}Z" fill="#fff" stroke="{INK}" stroke-width="2"/>'
            f'<path d="M{cx - 70} {cy}L{cx} {cy - 10}L{cx + 70} {cy}L{cx} {cy + 10}Z" fill="#fff" stroke="{INK}" stroke-width="2"/>'
            f'<text x="{cx}" y="{cy - 92}" font-size="30" font-weight="bold" text-anchor="middle">N</text></g>')


def mark_svg(kind, x, y):
    """Just the symbol of a place, as drawn on the map."""
    return place_svg("legend", "", kind, x, y, "start", 0, 0).split("<text")[0].split('">', 1)[1]


def legend():
    top = H + MS + 30
    s = [f'<g id="legend" font-size="24">',
         f'<text x="{-M + 60}" y="{top + 48}" font-size="52" font-weight="bold" letter-spacing="10">ELANDRIA</text>',
         f'<text x="{-M + 62}" y="{top + 88}" font-style="italic">1 px = 1 km, north up</text>']
    sx, sy = -M + 62, top + 120
    for i in range(5):
        s.append(f'<rect x="{sx + i * 100}" y="{sy}" width="100" height="12" fill="{INK if i % 2 == 0 else "#fff"}" stroke="{INK}" stroke-width="2"/>')
    for i, t in ((0, "0"), (5, "500 km")):
        s.append(f'<text x="{sx + i * 100}" y="{sy + 40}" text-anchor="{"start" if i == 0 else "middle"}">{t}</text>')

    def line(stroke, width, dash=""):
        return lambda x, y: (f'<line x1="{x - 24}" y1="{y}" x2="{x + 24}" y2="{y}" stroke="{stroke}" stroke-width="{width}" '
                             f'stroke-linecap="round"{f" stroke-dasharray={chr(34)}{dash}{chr(34)}" if dash else ""}/>')

    def patch(fill, glyph=None, dy=8):
        return lambda x, y: (f'<rect x="{x - 28}" y="{y - 20}" width="56" height="34" rx="6" fill="{fill}"/>'
                             + (f'<use href="#g-{glyph}" x="{x}" y="{y + dy}"/>' if glyph else ""))

    items = [
        (lambda x, y: mark_svg("capital", x, y), "capital"),
        (lambda x, y: mark_svg("city", x, y), "city"),
        (lambda x, y: mark_svg("town", x, y), "town"),
        (lambda x, y: mark_svg("hold", x, y), "dwarven hold"),
        (lambda x, y: mark_svg("fort", x, y), "fort"),
        (lambda x, y: mark_svg("pass", x, y), "pass"),
        (lambda x, y: mark_svg("ruin", x, y), "ruin"),
        (line("#8b5a2b", 4, "0.5 8"), "road"),
        (line(RIVER, 5), "river"),
        (line("#8a3b2e", 5, "20 12"), "border"),
        (patch("#e6dcc8", "peak", 14), "young mountains"),
        (patch("#e6dcc8", "hump", 10), "old mountains"),
        (patch("#dbe7c9", "tree", 6), "forest"),
        (patch("#dce6d6", "pine", 10), "coniferous forest"),
        (patch("#dde7de", "reed", 8), "marsh"),
        (patch("#e3edcc", "hill", 6), "farmland hills"),
        (patch("#ebe4da", "ash", 0), "wastes"),
        (patch(WATER), "lake"),
    ]
    kx, ky = 760, top + 40
    for i, (draw, text) in enumerate(items):
        col, row = divmod(i, 3)
        x, y = kx + col * 520, ky + row * 62
        s.append(draw(x, y) + f'<text x="{x + 44}" y="{y + 8}">{text}</text>')
    s.append('</g>')
    return "\n".join(s)


def build():
    rng = random.Random(42)
    coast = jagged(COAST, rng)
    islands = [jagged(i, rng, rough=0.4, min_len=14) for i in ISLANDS]
    total_h = H + M + MS + LEGEND_H
    global LAND_SHAPE
    LAND_SHAPE = coast
    river_lines = [clip_to_land(bend(to_coast(p, coast), random.Random(n + 51), rough=0.2, min_len=16), coast)
                   for n, (_, _, p) in enumerate(RIVERS)]
    by_id = {rid: n for n, (rid, _, _) in enumerate(RIVERS)}
    for rid, target in TRIBUTARIES.items():
        line, main = river_lines[by_id[rid]], river_lines[by_id[target]]
        river_lines[by_id[rid]] = line[:-1] + [min(main, key=lambda q: math.dist(q, line[-1]))]
    road_lines = [[(round(x), round(y)) for x, y in bend(p, random.Random(n + 91), rough=0.06, min_len=30)]
                  for n, (_, _, _, p) in enumerate(ROADS)]
    lake_shapes = [jagged(poly, random.Random(n + 31), rough=0.22, min_len=14) for n, (_, poly) in enumerate(LAKES)]
    valdren, valdren_border = valdren_outline(coast, {rid: line for (rid, _, _), line in zip(RIVERS, river_lines)}, lake_shapes[0])

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-M} {-M} {W + 2 * M} {total_h}" '
           f'width="{W + 2 * M}" height="{total_h}" font-family="Georgia, \'Times New Roman\', serif" fill="{INK}">',
           "<title>Elandria</title>",
           "<desc>\n" + summary(river_lines, road_lines) + "\n</desc>",
           f"""<defs>
  <polygon id="coast-shape" points="{pts(coast)}"/>
  <clipPath id="land"><use href="#coast-shape"/></clipPath>{GLYPHS}
  <g id="islands-shape">{"".join(f'<polygon id="island-{n + 1}" points="{pts(p)}"/>' for n, p in enumerate(islands))}</g>
</defs>""",
           f'<rect x="{-M}" y="{-M}" width="{W + 2 * M}" height="{H + M + MS}" fill="{SEA}"/>',
           f'<g id="shallows" fill="{SHALLOW}" stroke="{SHALLOW}" stroke-width="60" stroke-linejoin="round">'
           f'<use href="#coast-shape"/><use href="#islands-shape"/></g>',
           f'<g id="land" fill="{LAND}" stroke="{SHORE}" stroke-width="4" stroke-linejoin="round">'
           f'<use href="#coast-shape"/><use href="#islands-shape"/></g>',
           f'<polygon id="kingdom-valdren" data-name="Kingdom of Valdren" points="{pts(valdren)}" fill="#c9a07a" '
           f'fill-opacity="0.12"/>',
           f'<polyline id="border-valdren" points="{pts(valdren_border)}" fill="none" stroke="#8a3b2e" stroke-width="5" '
           f'stroke-dasharray="20 12" stroke-opacity="0.75"/>',
           '<g id="land-cover" clip-path="url(#land)">',
           *[cover_svg(k, aid, poly, random.Random(n + 71), river_lines + road_lines, lake_shapes)
             for n, (k, aid, poly) in enumerate(AREAS)],
           '</g>',
           f'<g id="rivers" fill="none" stroke="{RIVER}" stroke-linejoin="round" stroke-linecap="round">',
           *[f'  <polyline id="{rid}" data-name="{RIVER_NAMES[rid][0]}" data-km="{km(line)}" stroke-width="{w}" '
             f'points="{pts(line)}"/>' for (rid, w, _), line in zip(RIVERS, river_lines)],
           '</g>',
           f'<g id="lakes" fill="{WATER}" stroke="{RIVER}" stroke-width="4" stroke-linejoin="round">',
           *[f'  <polygon id="{lid}" data-name="{LAKE_NAMES[lid][0]}" points="{pts(shape)}"/>'
             for (lid, _), shape in zip(LAKES, lake_shapes)],
           '</g>',
           '<g id="mountains">',
           *[range_svg(*r, random.Random(n + 11)) for n, r in enumerate(RANGES)],
           '</g>',
           '<g id="area-labels">', *[area_label(aid, poly) for _, aid, poly in AREAS], '</g>',
           '<g id="water-labels">',
           *[river_label(rid, line) for (rid, _, _), line in zip(RIVERS, river_lines)],
           *[f'<text x="{x}" y="{y}" font-size="{size}" font-style="italic" text-anchor="middle" fill="#2f5f8a">{n}</text>'
             for n, x, y, size in LAKE_NAMES.values()],
           '</g>',
           '<g id="regions">',
           *[f'<polygon id="region-{rid}" data-name="{name.title()}" points="{pts(poly)}" fill="none" stroke="none"/>'
             f'<text x="{x}" y="{y}" font-size="30" letter-spacing="9" text-anchor="middle" fill="#5a4a32" '
             f'stroke="{LAND}" stroke-width="8" paint-order="stroke"{REGION_TILT.get(rid, "")}>{name}</text>'
             for rid, name, x, y, poly in REGIONS],
           '</g>',
           '<g id="labels">', *[label_svg(*l) for l in LABELS],
           f'<text x="{KINGDOM_LABEL[2]}" y="{KINGDOM_LABEL[3]}" font-size="24" letter-spacing="8" text-anchor="middle" '
           f'fill="#7a3428" stroke="{LAND}" stroke-width="7" paint-order="stroke">{KINGDOM_LABEL[0]}</text>',
           f'<text x="{KINGDOM_LABEL[2]}" y="{KINGDOM_LABEL[3] + 46}" font-size="40" letter-spacing="10" text-anchor="middle" '
           f'fill="#7a3428" stroke="{LAND}" stroke-width="8" paint-order="stroke">{KINGDOM_LABEL[1]}</text>',
           '</g>',
           '<g id="roads" fill="none" stroke="#8b5a2b" stroke-width="4" stroke-dasharray="0.5 8" stroke-linecap="round">',
           *[f'  <polyline id="{rid}" data-from="{a}" data-to="{b}" data-km="{km(line)}" points="{pts(line)}"/>'
             for (rid, a, b, _), line in zip(ROADS, road_lines)],
           '</g>',
           '<g id="places">', *[place_svg(*p) for p in PLACES], '</g>',
           compass(3600, -150),
           f'<rect x="{-M}" y="{H + MS}" width="{W + 2 * M}" height="{LEGEND_H}" fill="{LAND}"/>',
           f'<line x1="{-M}" y1="{H + MS}" x2="{W + M}" y2="{H + MS}" stroke="{INK}" stroke-width="3"/>',
           f'<rect x="{-M + 12}" y="{-M + 12}" width="{W + 2 * M - 24}" height="{total_h - 24}" fill="none" stroke="{INK}" stroke-width="4"/>',
           legend(),
           "</svg>"]
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    OUT.parent.mkdir(parents=True, exist_ok=True)
    svg = build()
    OUT.write_text(svg, encoding="utf-8", newline="\n")
    print(OUT, len(svg) // 1024, "KB")
