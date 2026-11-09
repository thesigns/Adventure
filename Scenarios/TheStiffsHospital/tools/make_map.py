"""Generator planu Szpitala Czerniakowskiego dla scenariusza TheStiffsHospital.

Narzędzie autora, nie do gry. Tworzy dwa pliki w folderze scenariusza:
    MapHospital.svg         pełny plan dla MG
    MapHospital.areas.json  obszary dla Scripts/fogmap.py

Użycie:
    python Scenarios/TheStiffsHospital/tools/make_map.py

Plan pokazuje wszystkie kondygnacje gmachu i pawilon gospodarczy na jednym
arkuszu, jak rzuty w dokumentacji budynku. Wymiary są w metrach (gmach ma
60 x 14 m, północ u góry). Układ pomieszczeń jest wymyślony na potrzeby
scenariusza. Po zmianie planu obszary aktualizują się same, bo powstają
z tych samych danych co rysunek.
"""
import json
import math
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
OUT_SVG = HERE / "MapHospital.svg"
OUT_AREAS = HERE / "MapHospital.areas.json"
rnd = random.Random(1990)

S = 11.0                       # px na metr
BW, BH = 60.0, 14.0            # gmach w metrach
WALL = 0.45                    # grubość ściany zewnętrznej
CY0, CY1 = 5.5, 8.5            # korytarz
PAD_X, PAD_TOP, PAD_BOT = 42, 58, 46
PANEL_W = BW * S + 2 * PAD_X
PANEL_H = BH * S + PAD_TOP + PAD_BOT
GAP = 26
MARGIN = 30
LEG_H = 250
W = 2 * PANEL_W + GAP + 2 * MARGIN
H = 4 * PANEL_H + 3 * GAP + 2 * MARGIN + LEG_H

INK = "#161616"
SHADOW = "#9b9b9b"
CORR = "#ececec"
GRID = "#d4d4d4"


def f(v):
    return f"{v:.1f}"


class Panel:
    def __init__(self, col, row, title, subtitle=""):
        self.ox = MARGIN + col * (PANEL_W + GAP)
        self.oy = MARGIN + row * (PANEL_H + GAP)
        self.title, self.subtitle = title, subtitle
        self.svg = []
        self.areas = {}
        self.codes = []

    def X(self, x):
        return self.ox + PAD_X + x * S

    def Y(self, y):
        return self.oy + PAD_TOP + y * S

    def rect_px(self, x0, y0, x1, y1, pad=0.0):
        a, b = self.X(x0 - pad), self.Y(y0 - pad)
        c, d = self.X(x1 + pad), self.Y(y1 + pad)
        return [[round(a, 1), round(b, 1)], [round(c, 1), round(b, 1)],
                [round(c, 1), round(d, 1)], [round(a, 1), round(d, 1)]]

    def area(self, key, name, *rects, pad=0.35):
        self.areas[key] = {"name": name, "polygons": [self.rect_px(*r, pad=pad) for r in rects]}
        x0, y0, x1, y1 = rects[0]
        self.codes.append((key, (x0 + x1) / 2, y1 + 0.05))

    # ------------------------------------------------------------ drawing
    def box(self, x0, y0, x1, y1, fill="#fff", stroke=INK, w=2.0, rx=0, extra=""):
        st = "none" if w == 0 else stroke
        self.svg.append(f'<rect x="{f(self.X(x0))}" y="{f(self.Y(y0))}" width="{f((x1 - x0) * S)}" '
                        f'height="{f((y1 - y0) * S)}" rx="{rx}" fill="{fill}" stroke="{st}" stroke-width="{w}" {extra}/>')

    def line(self, x0, y0, x1, y1, w=1.6, color=INK, extra=""):
        self.svg.append(f'<line x1="{f(self.X(x0))}" y1="{f(self.Y(y0))}" x2="{f(self.X(x1))}" y2="{f(self.Y(y1))}" '
                        f'stroke="{color}" stroke-width="{w}" stroke-linecap="round" {extra}/>')

    def circle(self, x, y, r, fill="#fff", w=1.6, extra=""):
        self.svg.append(f'<circle cx="{f(self.X(x))}" cy="{f(self.Y(y))}" r="{f(r * S)}" fill="{fill}" stroke="{INK}" stroke-width="{w}" {extra}/>')

    def text(self, x, y, t, cls="room", anchor="middle", halo=True):
        X, Y = f(self.X(x)), f(self.Y(y))
        if halo:
            self.svg.append(f'<text x="{X}" y="{Y}" class="{cls}" text-anchor="{anchor}" stroke="#fff" stroke-width="4" stroke-linejoin="round">{t}</text>')
        self.svg.append(f'<text x="{X}" y="{Y}" class="{cls}" text-anchor="{anchor}">{t}</text>')

    def grid(self, x0, y0, x1, y1):
        d = []
        for gx in range(math.ceil(x0), math.floor(x1) + 1):
            d.append(f"M{f(self.X(gx))} {f(self.Y(y0))}V{f(self.Y(y1))}")
        for gy in range(math.ceil(y0), math.floor(y1) + 1):
            d.append(f"M{f(self.X(x0))} {f(self.Y(gy))}H{f(self.X(x1))}")
        self.svg.append(f'<path d="{"".join(d)}" stroke="{GRID}" stroke-width="0.8" fill="none"/>')

    def shell(self, x0=0.0, y0=0.0, x1=BW, y1=BH, ground=False):
        """Zewnętrzny obrys budynku: cień, gruba ściana, podłoga z siatką."""
        self.svg.append(f'<rect x="{f(self.X(x0) + 7)}" y="{f(self.Y(y0) + 7)}" width="{f((x1 - x0) * S)}" '
                        f'height="{f((y1 - y0) * S)}" fill="{SHADOW}"/>')
        self.box(x0, y0, x1, y1, fill=INK, w=0)
        self.box(x0 + WALL, y0 + WALL, x1 - WALL, y1 - WALL, fill="#fff", w=0)
        self.grid(x0 + WALL, y0 + WALL, x1 - WALL, y1 - WALL)

    def corridor(self, x0=WALL, x1=BW - WALL):
        self.box(x0, CY0, x1, CY1, fill=CORR, w=0)
        d = []
        x = x0
        while x < x1:
            d.append(f"M{f(self.X(x))} {f(self.Y(CY0))}V{f(self.Y(CY1))}")
            x += 1.0
        for yy in (6.5, 7.5):
            d.append(f"M{f(self.X(x0))} {f(self.Y(yy))}H{f(self.X(x1))}")
        self.svg.append(f'<path d="{"".join(d)}" stroke="#cfcfcf" stroke-width="0.8" fill="none"/>')

    def room(self, x0, y0, x1, y1, fill="#fff"):
        self.box(x0, y0, x1, y1, fill=fill, w=0)
        self.grid(x0, y0, x1, y1)
        self.box(x0, y0, x1, y1, fill="none", w=2.6)

    def door(self, x, y, horizontal=True, width=1.0, swing=1, double=False):
        """Drzwi w ścianie: przerwa i łuk skrzydła. swing=1 otwiera w dół/prawo, -1 w górę/lewo."""
        if horizontal:
            self.box(x - width / 2, y - 0.16, x + width / 2, y + 0.16, fill="#fff", w=0)
            leaves = [(x - width / 2, width)] if not double else [(x - width / 2, width / 2), (x + width / 2, -width / 2)]
            for hx, wl in leaves:
                r = abs(wl)
                sx = 1 if wl > 0 else -1
                ex, ey = hx, y + swing * r
                self.line(hx, y, ex, ey, w=1.6)
                sweep = 1 if (sx * swing) > 0 else 0
                self.svg.append(f'<path d="M{f(self.X(hx + wl))} {f(self.Y(y))} A{f(r * S)} {f(r * S)} 0 0 {sweep} '
                                f'{f(self.X(ex))} {f(self.Y(ey))}" fill="none" stroke="{INK}" stroke-width="1" stroke-dasharray="3 2"/>')
        else:
            self.box(x - 0.16, y - width / 2, x + 0.16, y + width / 2, fill="#fff", w=0)
            hy = y - width / 2
            ex, ey = x + swing * width, hy
            self.line(x, hy, ex, ey, w=1.6)
            sweep = 0 if swing > 0 else 1
            self.svg.append(f'<path d="M{f(self.X(x))} {f(self.Y(hy + width))} A{f(width * S)} {f(width * S)} 0 0 {sweep} '
                            f'{f(self.X(ex))} {f(self.Y(ey))}" fill="none" stroke="{INK}" stroke-width="1" stroke-dasharray="3 2"/>')

    def opening(self, x, y, horizontal=True, width=1.2):
        if horizontal:
            self.box(x - width / 2, y - 0.2, x + width / 2, y + 0.2, fill=CORR, w=0)
        else:
            self.box(x - 0.2, y - width / 2, x + 0.2, y + width / 2, fill=CORR, w=0)

    def windows(self, x0, x1, north=True, step=3.5):
        y = 0 if north else BH - WALL
        n = max(1, int((x1 - x0) / step))
        for i in range(n):
            cx = x0 + (x1 - x0) * (i + 0.5) / n
            self.box(cx - 0.8, y, cx + 0.8, y + WALL, fill="#fff", w=0)
            for k in (0.15, 0.30):
                self.line(cx - 0.8, y + k, cx + 0.8, y + k, w=1.0)
            self.line(cx - 0.8, y, cx - 0.8, y + WALL, w=1.4)
            self.line(cx + 0.8, y, cx + 0.8, y + WALL, w=1.4)

    def stairs(self, x0, y0, x1, y1, label="", up=True):
        self.box(x0, y0, x1, y1, fill="#fff", w=2.2)
        mid = (x0 + x1) / 2
        n = int((y1 - y0 - 1.2) / 0.3)
        for i in range(n + 1):
            yy = y0 + 1.2 + i * 0.3
            self.line(x0 + 0.1, yy, mid - 0.08, yy, w=1.0)
            self.line(mid + 0.08, yy, x1 - 0.1, yy, w=1.0)
        self.line(mid, y0 + 1.2, mid, y1 - 0.05, w=2.0)
        ax = (x0 + mid) / 2
        self.line(ax, y1 - 0.4, ax, y0 + 1.5, w=1.4)
        self.svg.append(f'<path d="M{f(self.X(ax - 0.25))} {f(self.Y(y0 + 1.9))}L{f(self.X(ax))} {f(self.Y(y0 + 1.45))}'
                        f'L{f(self.X(ax + 0.25))} {f(self.Y(y0 + 1.9))}" fill="none" stroke="{INK}" stroke-width="1.4"/>')
        if label:
            self.text(mid, y0 + 0.85, label, cls="tiny")

    def lift(self, x0, y0, x1, y1, label="", broken=False):
        self.box(x0, y0, x1, y1, fill="#fff", w=2.4)
        self.line(x0, y0, x1, y1, w=1.2)
        self.line(x1, y0, x0, y1, w=1.2)
        if broken:
            self.box(x0 + 0.25, y0 + 0.25, x1 - 0.25, y1 - 0.25, fill="none", w=1.0, extra='stroke-dasharray="3 2"')
        if label:
            self.text((x0 + x1) / 2, y1 + 0.75, label, cls="tiny")

    def bed(self, x, y, horizontal=False):
        if horizontal:
            self.box(x, y, x + 2.0, y + 0.9, fill="#fff", w=1.4, rx=2)
            self.line(x + 0.45, y + 0.08, x + 0.45, y + 0.82, w=1.0)
        else:
            self.box(x, y, x + 0.9, y + 2.0, fill="#fff", w=1.4, rx=2)
            self.line(x + 0.08, y + 0.45, x + 0.82, y + 0.45, w=1.0)

    def ward(self, x0, x1, north=True, beds=3):
        """Sala chorych: łóżka głową do ściany zewnętrznej, stolik pośrodku."""
        span = x1 - x0
        for i in range(beds):
            bx = x0 + span * (i + 0.5) / beds - 0.45
            by = WALL + 0.25 if north else BH - WALL - 2.25
            self.bed(bx, by)

    def code_tags(self):
        out = []
        for key, x, y in self.codes:
            X, Y = f(self.X(x)), f(self.Y(y))
            wpx = len(key) * 6.2 + 8
            out.append(f'<rect x="{f(float(X) - wpx / 2)}" y="{f(float(Y) - 10)}" width="{f(wpx)}" height="13" rx="2" fill="#fff" stroke="#8a1c1c" stroke-width="0.8"/>'
                       f'<text x="{X}" y="{Y}" class="code" text-anchor="middle">{key}</text>')
        return "".join(out)

    def header(self):
        x, y = self.ox + PAD_X, self.oy + 30
        s = f'<text x="{f(x)}" y="{f(y)}" class="ptitle">{self.title}</text>'
        if self.subtitle:
            s += f'<text x="{f(x)}" y="{f(y + 19)}" class="psub">{self.subtitle}</text>'
        s += f'<line x1="{f(x)}" y1="{f(y + 26)}" x2="{f(self.ox + PANEL_W - PAD_X)}" y2="{f(y + 26)}" stroke="{INK}" stroke-width="1.2"/>'
        return s

    def header_poly(self):
        x0, y0 = self.ox + PAD_X - 6, self.oy + 6
        x1, y1 = self.ox + PANEL_W - PAD_X + 6, self.oy + 57
        return [[round(x0, 1), round(y0, 1)], [round(x1, 1), round(y0, 1)], [round(x1, 1), round(y1, 1)], [round(x0, 1), round(y1, 1)]]


# ================================================================ wspólne elementy kondygnacji gmachu
MAIN_ST = (27.0, CY1, 31.0, BH - WALL)       # główna klatka schodowa (od frontu)
LIFT_P = (31.0, CY1, 33.5, 11.5)              # winda osobowa (zepsuta)
SERV_ST = (55.5, WALL, BW - WALL, CY0)       # schody gospodarcze (północny wschód)
LIFT_T = (55.5, CY1, BW - WALL, 12.0)        # winda towarowa


def floor_base(p, rooms_n, rooms_s, stair_label="schody"):
    p.shell()
    p.corridor()
    for r in rooms_n:
        p.room(r[0], WALL, r[1], CY0, fill=r[2] if len(r) > 2 else "#fff")
    for r in rooms_s:
        p.room(r[0], CY1, r[1], BH - WALL, fill=r[2] if len(r) > 2 else "#fff")
    p.windows(WALL, 55.5, north=True)
    p.windows(WALL, 27.0, north=False)
    p.windows(33.5, 55.5, north=False)
    p.stairs(*MAIN_ST, label=stair_label)
    p.opening(29.0, CY1, width=3.6)
    p.lift(*LIFT_P, label="winda", broken=True)
    p.stairs(*SERV_ST, label="gosp.")
    p.opening(57.5, CY0, width=3.6)
    p.lift(*LIFT_T, label="towarowa")
    p.opening(57.5, CY1, width=3.0)
    p.box(33.5, 11.5, 55.5 if False else 33.5, 11.5, w=0)


def ward_floor(p, north_rooms, south_rooms):
    """Standardowe piętro oddziału. Pokoje: (x0, x1, nazwa, rodzaj)."""
    floor_base(p, [(a, b) for a, b, *_ in north_rooms], [(a, b) for a, b, *_ in south_rooms])
    for x0, x1, name, kind in north_rooms:
        if kind == "sala":
            p.ward(x0, x1, north=True)
        p.door((x0 + x1) / 2 + 1.2, CY0, swing=-1)
        p.text((x0 + x1) / 2, {"sala": 4.95, "op": 4.95}.get(kind, 2.95), name)
    for x0, x1, name, kind in south_rooms:
        if kind == "sala":
            p.ward(x0, x1, north=False)
        p.door((x0 + x1) / 2 - 1.2, CY1, swing=1)
        p.text((x0 + x1) / 2, {"sala": 9.6, "ior": 13.0}.get(kind, 11.4), name)
    p.text(2.2, 7.25, "palarnia", cls="tiny")


GENERIC_N = [(WALL, 7.0, "sala 1", "sala"), (7.0, 14.0, "sala 2", "sala"), (14.0, 21.0, "sala 3", "sala"),
             (21.0, 28.0, "sala 4", "sala"), (28.0, 32.0, "dyż. lek.", "pok"), (32.0, 37.5, "dyż. piel.", "pok"),
             (37.5, 46.5, "sala 5", "sala"), (46.5, 55.5, "sala 6", "sala")]
GENERIC_S = [(WALL, 5.5, "łazienka", "pok"), (5.5, 9.5, "WC", "pok"), (9.5, 16.5, "sala 7", "sala"),
             (16.5, 23.5, "sala 8", "sala"), (23.5, 27.0, "gosp.", "pok"), (33.5, 41.0, "sala 9", "sala"),
             (41.0, 48.0, "sala 10", "sala"), (48.0, 55.5, "sala 11", "sala")]


def replace(rooms, *new):
    out = [r for r in rooms if not any(r[0] < n[1] and n[0] < r[1] for n in new)]
    return sorted(out + list(new))


panels = []

# ---------------------------------------------------------------- IV piętro
p4 = Panel(0, 0, "IV PIĘTRO", "neurologia · laryngologia · okulistyka")
n4 = replace(GENERIC_N, (37.5, 46.5, "laryngologia", "sala"), (46.5, 55.5, "okulistyka", "sala"))
s4 = replace(GENERIC_S, (48.0, 55.5, "sala dzieci", "sala"), (41.0, 48.0, "zabiegowy", "pok"))
ward_floor(p4, n4, s4)
p4.line(30.0, CY0 + 0.15, 30.0, CY1 - 0.15, w=1.2, extra='stroke-dasharray="5 4"')
p4.text(15.0, 7.25, "NEUROLOGIA", cls="wing")
p4.text(44.0, 7.25, "LARYNGOLOGIA · OKULISTYKA", cls="wing")
p4.area("4-neurologia", "IV piętro: neurologia", (0, 0, 30.0, BH))
p4.area("4-laryngologia", "IV piętro: laryngologia, okulistyka, sala dzieci", (30.0, 0, BW, BH))
panels.append(p4)

# ---------------------------------------------------------------- III piętro
p3 = Panel(0, 1, "III PIĘTRO", "oddział chorób wewnętrznych")
s3 = replace(GENERIC_S, (48.0, 55.5, "dla umierających", "sala"))
ward_floor(p3, GENERIC_N, s3)
p3.line(48.6, 11.6, 54.9, 11.6, w=1.4, extra='stroke-dasharray="2 2"')   # parawan
p3.text(28.0, 7.25, "INTERNA", cls="wing")
p3.area("3-interna", "III piętro: interna", (0, 0, 48.0, BH), (48.0, 0, BW, CY1), (55.5, CY1, BW, BH))
p3.area("3-umierajacy", "III piętro: sala dla umierających", (48.0, CY1, 55.5, BH))
panels.append(p3)

# ---------------------------------------------------------------- II piętro
p2 = Panel(0, 2, "II PIĘTRO", "chirurgia urazowo-ortopedyczna")
s2 = replace(GENERIC_S, (33.5, 41.0, "gipsownia", "pok"))
ward_floor(p2, GENERIC_N, s2)
# gablota przeciwpożarowa z siekierą przy klatce schodowej
p2.box(25.0, CY1 - 0.55, 26.6, CY1 - 0.05, fill="#fff", w=1.8)
p2.text(25.8, CY1 - 0.12, "G", cls="sym", halo=False)
p2.box(35.0, 9.4, 37.6, 10.4, fill="#fff", w=1.2)                    # stół gipsowy
p2.text(28.0, 7.25, "URAZÓWKA", cls="wing")
p2.area("2-urazowka", "II piętro: urazówka", (0, 0, 33.5, BH), (33.5, 0, BW, CY1), (41.0, CY1, BW, BH))
p2.area("2-gipsownia", "II piętro: gipsownia", (33.5, CY1, 41.0, BH))
panels.append(p2)

# ---------------------------------------------------------------- I piętro
p1 = Panel(1, 0, "I PIĘTRO", "chirurgia · blok operacyjny · intensywna opieka")
n1 = replace(GENERIC_N, (37.5, 46.5, "sala operacyjna 1", "op"), (46.5, 55.5, "sala operacyjna 2", "op"))
s1 = replace(GENERIC_S, (33.5, 41.0, "intensywna opieka", "ior"), (41.0, 48.0, "sterylizatornia", "pok"),
             (48.0, 55.5, "śluza i myjnia", "pok"))
ward_floor(p1, n1, s1)
for x0, x1 in ((37.5, 46.5), (46.5, 55.5)):
    cx = (x0 + x1) / 2
    p1.box(cx - 0.4, 1.2, cx + 0.4, 3.2, fill="#fff", w=1.6, rx=2)
    p1.circle(cx, 2.2, 0.95, fill="none", w=1.0, extra='stroke-dasharray="3 3"')
for i in range(4):
    p1.bed(34.0 + i * 1.75, 9.2)
p1.box(37.5, CY0 + 0.1, 37.75, CY1 - 0.1, fill=INK, w=0)              # ściana z drzwiami bloku
p1.door(37.6, 7.0, horizontal=False, width=2.2, swing=1)
p1.text(18.0, 7.25, "CHIRURGIA", cls="wing")
p1.text(46.0, 7.25, "BLOK OPERACYJNY", cls="wing")
p1.area("1-chirurgia", "I piętro: chirurgia", (0, 0, 33.5, BH), (33.5, 0, 37.6, CY1))
p1.area("1-blok", "I piętro: blok operacyjny", (37.6, 0, BW, CY1), (41.0, CY1, BW, BH))
p1.area("1-intensywna", "I piętro: sala intensywnej opieki", (33.5, CY1, 41.0, BH))
panels.append(p1)

# ---------------------------------------------------------------- parter
p0 = Panel(1, 1, "PARTER", "izba przyjęć · portiernia · apteka · przychodnia")
n0 = [(WALL, 14.0), (14.0, 22.0), (22.0, 55.5)]
s0 = [(WALL, 12.0), (12.0, 18.0), (18.0, 27.0), (33.5, 41.0), (41.0, 48.0), (48.0, 55.5)]
floor_base(p0, n0, s0)
p0.room(18.0, CY1, 27.0, BH - WALL, fill=CORR)                         # hol wejściowy
p0.room(18.0, CY1, 21.5, 11.6)                                         # portiernia
p0.box(18.3, 9.0, 21.2, 9.6, fill="#fff", w=1.2)                       # lada portiera
p0.opening(22.5, CY1, width=4.0)
for x0, x1, name in ((WALL, 14.0, "apteka"), (14.0, 22.0, "dyrektor"), (22.0, 30.0, "rejestracja")):
    p0.text((x0 + x1) / 2, 4.6, name)
for x0, x1 in ((30.0, 38.0), (38.0, 46.0), (46.0, 55.5)):
    p0.text((x0 + x1) / 2, 2.4, "gabinet", cls="tiny")
for x0, x1, dx in ((WALL, 14.0, 10.5), (14.0, 22.0, 18.0), (22.0, 55.5, 30.0)):
    p0.door(dx, CY0, swing=-1)
for xx in (30.0, 38.0, 46.0):
    p0.line(xx, WALL, xx, 3.8, w=2.2)                                  # gabinety przychodni
for i in range(9):                                                     # krata w aptece
    p0.line(8.6 + i * 0.25, CY0 - 0.95, 8.6 + i * 0.25, CY0 - 0.15, w=1.2)
p0.box(15.2, 1.2, 18.6, 2.2, fill="#fff", w=1.4)                       # biurko
p0.box(20.4, 1.0, 21.4, 2.0, fill="#3a3a3a", w=1.4)                    # sejf
p0.door(9.0, CY1, swing=1)
p0.door(15.0, CY1, swing=1)
p0.text(6.2, 11.4, "gabinet zabiegowy przychodni")
p0.text(15.0, 11.4, "depozyt")
p0.text(19.75, 10.9, "portiernia", cls="tiny")
p0.text(23.4, 12.6, "hol")
# wejście główne
p0.box(22.0, BH - WALL, 25.0, BH, fill="#fff", w=0)
p0.door(23.5, BH - WALL / 2, width=3.0, swing=1, double=True)
# izba przyjęć
p0.text(37.25, 11.4, "poczekalnia")
p0.text(44.5, 11.4, "zabiegowy")
p0.text(51.75, 9.6, "sala przyjęć")
for i in range(5):
    p0.box(34.0 + i * 1.35, 12.6, 35.0 + i * 1.35, 13.2, fill="#fff", w=1.1)   # krzesła
p0.box(42.5, 9.2, 44.5, 10.0, fill="#fff", w=1.4, rx=2)
p0.bed(49.0, 10.3, horizontal=True)
p0.bed(52.6, 10.3, horizontal=True)
p0.door(37.25, CY1, width=1.6, double=True)
p0.door(44.5, CY1)
p0.door(51.75, CY1, width=1.6, double=True)
p0.box(49.8, BH - WALL, 53.4, BH, fill="#fff", w=0)
p0.door(51.6, BH - WALL / 2, width=3.6, swing=1, double=True)
p0.text(31.5, 7.25, "IZBA PRZYJĘĆ  →", cls="wing")
# teren przed gmachem
p0.svg.append(f'<path d="M{f(p0.X(-2.5))} {f(p0.Y(BH + 3.6))}H{f(p0.X(BW + 2.5))}" stroke="{INK}" stroke-width="1.4" stroke-dasharray="7 4" fill="none"/>')
p0.svg.append(f'<path d="M{f(p0.X(44))} {f(p0.Y(BH + 3.6))}C{f(p0.X(46))} {f(p0.Y(BH + 1.0))} {f(p0.X(49))} {f(p0.Y(BH + 0.6))} '
              f'{f(p0.X(51.6))} {f(p0.Y(BH + 0.4))}" stroke="{INK}" stroke-width="1.2" fill="none"/>')
p0.text(51.6, BH + 2.3, "podjazd dla karetek", cls="tiny")
p0.text(23.5, BH + 2.3, "wejście główne", cls="tiny")
p0.text(8.0, BH + 3.1, "ogrodzenie, dalej ul. Stępińska", cls="tiny", anchor="start")
p0.area("0-hol", "Parter: hol, portiernia i korytarz", (0, CY0, 33.5, CY1), (18.0, CY1, 33.5, BH), (33.5, CY0, BW, CY1), (55.5, 0, BW, CY0))
p0.area("0-apteka", "Parter: apteka szpitalna", (0, 0, 14.0, CY0))
p0.area("0-dyrektor", "Parter: gabinet dyrektora", (14.0, 0, 22.0, CY0))
p0.area("0-przychodnia", "Parter: rejestracja i przychodnia", (22.0, 0, 55.5, CY0))
p0.area("0-depozyt", "Parter: depozyt", (12.0, CY1, 18.0, BH))
p0.area("0-zabiegowy", "Parter: gabinet zabiegowy przychodni", (0, CY1, 12.0, BH))
p0.area("0-izba", "Parter: izba przyjęć", (33.5, CY1, BW, BH))
p0.area("0-podjazd", "Teren przed gmachem: wejście i podjazd", (-3.0, BH, BW + 3.0, BH + 3.9), pad=0.0)
panels.append(p0)

# ---------------------------------------------------------------- piwnica
pp = Panel(1, 2, "PIWNICA", "kostnica · szatnie · magazyn · warsztat")
np_ = [(WALL, 20.0), (20.0, 30.0), (30.0, 55.5)]
sp = [(WALL, 27.0), (33.5, 38.0), (38.0, 46.0), (46.0, 55.5)]
pp.shell()
pp.corridor()
for a, b in np_:
    pp.room(a, WALL, b, CY0)
for a, b in sp:
    pp.room(a, CY1, b, BH - WALL)
pp.stairs(*MAIN_ST, label="schody")
pp.opening(29.0, CY1, width=3.6)
pp.lift(*LIFT_P, label="winda", broken=True)
pp.stairs(*SERV_ST, label="gosp.")
pp.opening(57.5, CY0, width=3.6)
pp.lift(*LIFT_T, label="towarowa")
pp.opening(57.5, CY1, width=3.0)
pp.text(10.0, 4.75, "magazyn bielizny")
pp.text(25.0, 4.75, "warsztat")
pp.text(42.5, 4.75, "węzeł cieplny")
pp.text(13.5, 11.4, "szatnie personelu")
pp.text(35.75, 12.9, "kantorek", cls="tiny")
pp.text(42.0, 12.9, "prosektorium", cls="tiny")
pp.text(50.75, 12.9, "chłodnia", cls="tiny")
for dx, sw in ((10.0, -1), (25.0, -1), (42.5, -1)):
    pp.door(dx, CY0, swing=sw)
pp.door(13.5, CY1)
pp.door(35.75, CY1)
pp.door(42.0, CY1, width=1.4, double=True)
pp.door(46.0, 11.2, horizontal=False, width=1.4, swing=1)
for i in range(4):                                                     # szafki
    pp.box(1.4 + i * 4.6, 12.4, 4.6 + i * 4.6, 13.2, fill="#fff", w=1.2)
for i in range(5):                                                     # półki magazynu
    pp.line(1.5, 1.1 + i * 0.6, 18.5, 1.1 + i * 0.6, w=1.0, color="#777")
pp.box(21.0, 1.2, 28.8, 2.0, fill="#fff", w=1.4)                       # stół warsztatowy
for i in range(4):                                                     # rury węzła
    pp.line(31.0, 1.1 + i * 0.55, 54.5, 1.1 + i * 0.55, w=2.2 if i % 2 == 0 else 1.2)
pp.circle(36.0, 3.5, 0.5)
pp.circle(48.0, 3.5, 0.5)
pp.box(40.5, 10.0, 43.5, 11.2, fill="#fff", w=1.8, rx=3)               # stół sekcyjny
for row in range(3):                                                   # szuflady chłodni
    for col in range(2):
        pp.box(53.2 + col * 1.0, 9.0 + row * 1.25, 54.1 + col * 1.0, 10.1 + row * 1.25, fill="#fff", w=1.4)
pp.box(34.2, 9.0, 36.2, 9.8, fill="#fff", w=1.2)                       # biurko prosektoryjnego
# wejście do tunelu na zachodnim końcu korytarza
pp.box(0, CY0 + 0.6, WALL, CY1 - 0.6, fill="#fff", w=0)
pp.door(WALL / 2, 7.0, horizontal=False, width=1.6, swing=1)
pp.box(-3.4, CY0 + 0.7, 0, CY1 - 0.7, fill=CORR, w=0)
pp.line(-3.4, CY0 + 0.7, 0, CY0 + 0.7, w=2.6)
pp.line(-3.4, CY1 - 0.7, 0, CY1 - 0.7, w=2.6)
pp.text(-1.7, CY0 - 0.25, "tunel", cls="tiny")
pp.text(-1.7, CY1 + 0.95, "do pawilonu", cls="tiny")
pp.area("P-korytarz", "Piwnica: korytarz i klatki schodowe", (0, CY0, BW, CY1), (27.0, CY1, 33.5, BH), (55.5, 0, BW, CY0), (55.5, CY1, BW, BH))
pp.area("P-magazyn", "Piwnica: magazyn bielizny", (0, 0, 20.0, CY0))
pp.area("P-warsztat", "Piwnica: warsztat konserwatora", (20.0, 0, 30.0, CY0))
pp.area("P-wezel", "Piwnica: węzeł cieplny", (30.0, 0, 55.5, CY0))
pp.area("P-szatnie", "Piwnica: szatnie personelu", (0, CY1, 27.0, BH))
pp.area("P-kostnica", "Piwnica: kostnica i prosektorium", (33.5, CY1, 55.5, BH))
pp.area("P-tunel", "Piwnica: wejście do tunelu", (-3.6, CY0 + 0.4, 0.4, CY1 - 0.4), pad=0.1)
panels.append(pp)

# ---------------------------------------------------------------- strych i dach
pd = Panel(0, 3, "STRYCH I DACH", "płaski dach z attyką, klapa nad schodami gospodarczymi")
pd.svg.append(f'<rect x="{f(pd.X(0) + 7)}" y="{f(pd.Y(0) + 7)}" width="{f(BW * S)}" height="{f(BH * S)}" fill="{SHADOW}"/>')
pd.box(0, 0, BW, BH, fill=INK, w=0)
pd.box(0.35, 0.35, BW - 0.35, BH - 0.35, fill="#f6f6f6", w=0)
d = []
for i in range(-20, 90):                                               # papa: drobne kreskowanie
    x = i * 0.9
    d.append(f"M{f(pd.X(max(0.35, x)))} {f(pd.Y(0.35 + max(0, 0.35 - x)))}")
hatch = []
k = -BH
while k < BW:
    x0, y0 = k, 0.35
    x1, y1 = k + BH, BH - 0.35
    if x0 < 0.35:
        y0 += 0.35 - x0
        x0 = 0.35
    if x1 > BW - 0.35:
        y1 -= x1 - (BW - 0.35)
        x1 = BW - 0.35
    if x1 > x0:
        hatch.append(f"M{f(pd.X(x0))} {f(pd.Y(y0))}L{f(pd.X(x1))} {f(pd.Y(y1))}")
    k += 1.2
pd.svg.append(f'<path d="{"".join(hatch)}" stroke="#c9c9c9" stroke-width="0.9" fill="none"/>')
pd.line(0.35, 7.0, BW - 0.35, 7.0, w=1.0, extra='stroke-dasharray="8 5"')        # kalenica spadku
pd.text(30.0, 6.6, "spadek dachu ← →", cls="tiny")
pd.box(55.9, 1.2, 58.9, 4.2, fill="#fff", w=2.4)                      # klapa
pd.line(55.9, 1.2, 58.9, 4.2, w=1.0)
pd.text(57.4, 5.15, "klapa", cls="tiny")
for cx in (8.0, 20.0, 40.0, 50.0):                                     # wywiewki
    pd.box(cx - 0.6, 2.0, cx + 0.6, 3.2, fill="#fff", w=1.8)
    pd.box(cx - 0.6, 10.8, cx + 0.6, 12.0, fill="#fff", w=1.8)
pd.box(28.0, 9.2, 32.0, 12.4, fill="#fff", w=2.2)                     # maszynownia windy
pd.text(30.0, 11.2, "maszynownia", cls="tiny")
pd.box(31.0, 1.6, 34.0, 3.6, fill="#fff", w=2.0)                      # zbiornik wody
pd.circle(32.5, 2.6, 0.75, fill="none", w=1.2)
pd.text(32.5, 4.7, "zbiornik wody", cls="tiny")
pd.text(30.0, 8.0, "strych techniczny pod stropodachem: wejście przez drzwi ze schodów gospodarczych", cls="tiny")
pd.text(BW / 2, BH + 1.9, "z dachu widać Dolny Mokotów, Siekierki z kominami elektrociepłowni, skarpę, Łazienki i Wisłę", cls="note")
pd.area("dach", "Strych i dach", (0, 0, BW, BH))
panels.append(pd)

# ---------------------------------------------------------------- pawilon gospodarczy
pg = Panel(1, 3, "PAWILON GOSPODARCZY", "kuchnia · pralnia · kotłownia · garaż · podwórze")
GX0, GX1, GY0, GY1 = 6.0, 44.0, 1.6, 12.1
# podwórze
pg.box(-2.5, 0.2, BW + 2.5, BH + 1.2, fill="#fafafa", w=0)
stip = []
for _ in range(420):
    x, y = rnd.uniform(-2.3, BW + 2.3), rnd.uniform(0.4, BH + 1.0)
    if not (GX0 - 0.6 < x < GX1 + 0.6 and GY0 - 0.6 < y < GY1 + 0.6):
        stip.append(f'<circle cx="{f(pg.X(x))}" cy="{f(pg.Y(y))}" r="{f(rnd.uniform(0.6, 1.3))}" fill="#9a9a9a"/>')
pg.svg.append("".join(stip))
pg.svg.append(f'<rect x="{f(pg.X(-2.5))}" y="{f(pg.Y(0.2))}" width="{f((BW + 5) * S)}" height="{f((BH + 1.0) * S)}" fill="none" stroke="{INK}" stroke-width="1.4" stroke-dasharray="7 4"/>')
pg.shell(GX0, GY0, GX1, GY1)
rooms_g = [(GX0 + WALL, 20.0, "kuchnia"), (20.0, 28.0, "pralnia"), (28.0, 34.0, "kotłownia"), (34.0, GX1 - WALL, "garaż")]
for a, b, name in rooms_g:
    pg.room(a, GY0 + WALL, b, GY1 - WALL)
    pg.text((a + b) / 2, GY0 + 1.6, name)
for i in range(3):                                                     # kotły kuchenne
    pg.circle(9.0 + i * 2.4, 6.0, 0.8)
pg.box(7.0, GY1 - WALL - 1.0, 19.4, GY1 - WALL - 0.4, fill="#fff", w=1.2)   # blaty
pg.box(14.5, 3.4, 19.2, 4.6, fill="#fff", w=1.2)                        # magazynek
pg.text(16.85, 4.25, "zapasy", cls="tiny")
for i in range(3):                                                     # pralki
    pg.circle(22.0 + i * 2.0, 5.2, 0.7)
pg.box(21.0, 8.4, 27.0, 9.4, fill="#fff", w=1.2)
pg.box(29.0, 4.0, 33.0, 7.6, fill="#fff", w=2.0, rx=3)                  # piec
pg.circle(31.0, 9.6, 0.8, fill="#3a3a3a")                               # komin
# nyska
pg.box(36.5, 4.2, 41.5, 6.6, fill="#fff", w=2.0, rx=4)
pg.box(40.6, 4.4, 41.3, 6.4, fill="#d0d0d0", w=1.2, rx=2)
pg.text(39.0, 8.8, "nyska", cls="tiny")
pg.box(GX1 - WALL, 3.5, GX1, 7.5, fill="#fff", w=0)                    # brama garażu
pg.line(GX1 - WALL / 2, 3.5, GX1 - WALL / 2, 7.5, w=1.2, extra='stroke-dasharray="3 2"')
# drzwi wewnętrzne i zewnętrzne
for x in (20.0, 28.0, 34.0):
    pg.door(x, 8.2, horizontal=False, width=1.2, swing=1)
pg.box(12.0, GY1 - WALL, 14.0, GY1, fill="#fff", w=0)
pg.door(13.0, GY1 - WALL / 2, width=2.0, swing=1)
# tunel z piwnicy gmachu (od zachodu)
pg.box(-2.5, 5.3, GX0, 6.7, fill=CORR, w=0)
pg.line(-2.5, 5.3, GX0, 5.3, w=2.6)
pg.line(-2.5, 6.7, GX0, 6.7, w=2.6)
pg.box(GX0, 5.3, GX0 + WALL, 6.7, fill="#fff", w=0)
pg.door(GX0 + WALL / 2, 6.0, horizontal=False, width=1.2, swing=1)
pg.text(0.8, 4.8, "tunel z piwnicy gmachu", cls="tiny", anchor="start")
# brama na boczną ulicę
pg.box(BW + 1.6, 4.0, BW + 3.4, 8.0, fill="#fff", w=0)
pg.line(BW + 2.5, 4.0, BW + 2.5, 8.0, w=3.0)
pg.circle(BW + 2.5, 6.0, 0.3, fill=INK, w=0)
pg.text(BW + 0.9, 3.3, "brama (kłódka)", cls="tiny", anchor="end")
pg.text(BW + 0.9, 9.4, "na boczną ulicę", cls="tiny", anchor="end")
pg.text(52.0, 12.9, "podwórze gospodarcze", cls="tiny")
pg.area("G-tunel", "Pawilon: tunel z piwnicy", (-2.7, 5.0, GX0, 7.0), pad=0.1)
pg.area("G-kuchnia", "Pawilon: kuchnia", (GX0, GY0, 20.0, GY1))
pg.area("G-pralnia", "Pawilon: pralnia", (20.0, GY0, 28.0, GY1))
pg.area("G-kotlownia", "Pawilon: kotłownia", (28.0, GY0, 34.0, GY1))
pg.area("G-garaz", "Pawilon: garaż z nyską", (34.0, GY0, GX1, GY1))
pg.area("G-podworze", "Podwórze gospodarcze i brama", (-2.5, 0.2, BW + 3.6, GY0 - 0.4), (GX1 + 0.4, 0.2, BW + 3.6, BH + 1.2),
        (-2.5, GY1 + 0.4, BW + 3.6, BH + 1.2), pad=0.0)
panels.append(pg)


# ================================================================ legenda i tabliczka
def legend():
    top = H - MARGIN - LEG_H + 18
    s = [f'<line x1="{MARGIN}" y1="{f(top)}" x2="{f(W - MARGIN)}" y2="{f(top)}" stroke="{INK}" stroke-width="2.5"/>']
    s.append(f'<text x="{MARGIN}" y="{f(top + 52)}" class="title">SZPITAL CZERNIAKOWSKI</text>')
    s.append(f'<text x="{MARGIN + 2}" y="{f(top + 82)}" class="sub">ul. Stępińska 19/25 · Warszawa, Dolny Mokotów · rzuty kondygnacji, stan na marzec 1990</text>')
    s.append(f'<text x="{MARGIN + 2}" y="{f(top + 106)}" class="sub">scenariusz „Pierwsza noc w Szpitalu Czerniakowskim”</text>')
    sx, sy = MARGIN + 2, top + 150
    for i in range(5):
        s.append(f'<rect x="{f(sx + i * S * 2)}" y="{f(sy)}" width="{f(S * 2)}" height="8" fill="{INK if i % 2 == 0 else "#fff"}" stroke="{INK}" stroke-width="1.4"/>')
    s.append(f'<text x="{f(sx)}" y="{f(sy + 28)}" class="small">0</text>')
    s.append(f'<text x="{f(sx + 10 * S)}" y="{f(sy + 28)}" class="small" text-anchor="middle">10 m</text>')
    s.append(f'<text x="{f(sx)}" y="{f(sy + 50)}" class="small">1 kratka = 1 m · północ u góry</text>')
    cx, cy = MARGIN + 300, top + 162
    s.append(f'<circle cx="{cx}" cy="{cy}" r="24" fill="none" stroke="{INK}" stroke-width="1.2"/>')
    s.append(f'<path d="M{cx} {cy - 32}L{cx + 8} {cy}L{cx} {cy - 5}L{cx - 8} {cy}Z" fill="{INK}"/>')
    s.append(f'<path d="M{cx} {cy + 32}L{cx + 8} {cy}L{cx} {cy + 5}L{cx - 8} {cy}Z" fill="#fff" stroke="{INK}" stroke-width="1.2"/>')
    s.append(f'<text x="{cx}" y="{cy - 38}" class="small" text-anchor="middle" font-weight="bold">N</text>')
    kx, ky = 820, top + 46
    items = [
        (f'<rect x="{kx}" y="{ky - 10}" width="34" height="20" fill="#fff" stroke="{INK}" stroke-width="2.6"/>'
         f'<rect x="{kx + 10}" y="{ky - 12}" width="14" height="5" fill="#fff"/>'
         f'<path d="M{kx + 10} {ky - 10}A14 14 0 0 0 {kx + 24} {ky + 4}" fill="none" stroke="{INK}" stroke-width="1" stroke-dasharray="3 2"/>', "drzwi"),
        (f'<rect x="{kx}" y="{ky - 4}" width="34" height="8" fill="{INK}"/><rect x="{kx + 8}" y="{ky - 4}" width="18" height="8" fill="#fff"/>'
         f'<line x1="{kx + 8}" y1="{ky - 1}" x2="{kx + 26}" y2="{ky - 1}" stroke="{INK}" stroke-width="1"/>'
         f'<line x1="{kx + 8}" y1="{ky + 2}" x2="{kx + 26}" y2="{ky + 2}" stroke="{INK}" stroke-width="1"/>', "okno"),
        ("".join(f'<line x1="{kx}" y1="{ky - 10 + i * 4}" x2="{kx + 34}" y2="{ky - 10 + i * 4}" stroke="{INK}" stroke-width="1"/>' for i in range(6))
         + f'<rect x="{kx}" y="{ky - 12}" width="34" height="24" fill="none" stroke="{INK}" stroke-width="2"/>', "schody"),
        (f'<rect x="{kx + 5}" y="{ky - 12}" width="24" height="24" fill="#fff" stroke="{INK}" stroke-width="2.4"/>'
         f'<path d="M{kx + 5} {ky - 12}L{kx + 29} {ky + 12}M{kx + 29} {ky - 12}L{kx + 5} {ky + 12}" stroke="{INK}" stroke-width="1.2"/>', "winda"),
        (f'<rect x="{kx + 7}" y="{ky - 12}" width="11" height="24" rx="2" fill="#fff" stroke="{INK}" stroke-width="1.4"/>'
         f'<line x1="{kx + 8}" y1="{ky - 6}" x2="{kx + 17}" y2="{ky - 6}" stroke="{INK}" stroke-width="1"/>', "łóżko"),
        (f'<rect x="{kx + 7}" y="{ky - 7}" width="20" height="14" fill="#fff" stroke="{INK}" stroke-width="1.8"/>'
         f'<text x="{kx + 17}" y="{ky + 5}" class="sym" text-anchor="middle">G</text>', "gablota ppoż."),
        (f'<rect x="{kx}" y="{ky - 10}" width="34" height="20" fill="{CORR}" stroke="{INK}" stroke-width="1"/>', "korytarz"),
        (f'<path d="M{kx} {ky}H{kx + 34}" stroke="{INK}" stroke-width="1.4" stroke-dasharray="7 4"/>', "ogrodzenie"),
    ]
    for i, (g, t) in enumerate(items):
        dx = (i // 4) * 230
        dy = (i % 4) * 44
        s.append(f'<g transform="translate({dx},{dy})">{g}<text x="{kx + 48}" y="{ky + 6}" class="ltext">{t}</text></g>')
    return "\n".join(s), [[round(0.0, 1), round(top - 8, 1)], [round(W, 1), round(top - 8, 1)], [round(W, 1), round(H, 1)], [0.0, round(H, 1)]]


legend_svg, legend_poly = legend()

FONT = "'Arial Narrow', 'Helvetica Neue', Helvetica, Arial, sans-serif"
style = f"""
  .ptitle {{ font: bold 22px {FONT}; fill: {INK}; letter-spacing: 3px; }}
  .psub {{ font: 13px {FONT}; fill: #444; letter-spacing: 1px; }}
  .room {{ font: 12px {FONT}; fill: {INK}; }}
  .wing {{ font: bold 12px {FONT}; fill: #555; letter-spacing: 3px; }}
  .tiny {{ font: 10px {FONT}; fill: {INK}; }}
  .note {{ font: italic 12px {FONT}; fill: #333; }}
  .sym {{ font: bold 9px {FONT}; fill: {INK}; text-anchor: middle; }}
  .code {{ font: bold 10px 'Courier New', monospace; fill: #8a1c1c; }}
  .title {{ font: bold 38px {FONT}; fill: {INK}; letter-spacing: 4px; }}
  .sub {{ font: 16px {FONT}; fill: #333; }}
  .small {{ font: 14px {FONT}; fill: {INK}; }}
  .ltext {{ font: 16px {FONT}; fill: {INK}; }}
"""

body = []
for p in panels:
    body.append(f'<g id="panel-{p.title.lower().replace(" ", "-")}">' + "".join(p.svg) + "</g>")
headers = "".join(p.header() for p in panels)
codes = "".join(p.code_tags() for p in panels)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {f(W)} {f(H)}" width="{f(W)}" height="{f(H)}">
<title>Szpital Czerniakowski: plan kondygnacji</title>
<style>{style}</style>
<rect x="0" y="0" width="{f(W)}" height="{f(H)}" fill="#fff"/>
{"".join(body)}
<g id="headers">{headers}</g>
<g id="codes">{codes}</g>
<g id="legend">{legend_svg}</g>
</svg>
'''

areas = {}
for p in panels:
    areas.update(p.areas)
spec = {
    "map": OUT_SVG.name,
    "mg_only": ["codes"],
    "always": [legend_poly] + [p.header_poly() for p in panels],
    "areas": areas,
}


def dump(o, ind=0):
    pad = "  " * (ind + 1)
    if isinstance(o, dict):
        items = [f"{pad}{json.dumps(k, ensure_ascii=False)}: {dump(v, ind + 1)}" for k, v in o.items()]
        return "{\n" + ",\n".join(items) + "\n" + "  " * ind + "}"
    if isinstance(o, list) and o and not (isinstance(o[0], list) and isinstance(o[0][0], list)):
        return json.dumps(o, ensure_ascii=False)
    if isinstance(o, list):
        return "[\n" + ",\n".join(pad + dump(v, ind + 1) for v in o) + "\n" + "  " * ind + "]"
    return json.dumps(o, ensure_ascii=False)


OUT_AREAS.write_text(dump(spec) + "\n", encoding="utf-8", newline="\n")
OUT_SVG.write_text(svg, encoding="utf-8", newline="\n")
print(OUT_SVG.name, len(svg) // 1024, "KB,", len(areas), "obszarów")
