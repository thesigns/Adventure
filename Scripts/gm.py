"""Ukryty stan MG kampanii: zegar świata, ukryte zdarzenia i ukryte rzuty.

Gracz widzi tę samą konsolę co MG, więc sekrety nie mogą trafiać do treści
poleceń, diffów ani wyjścia skryptów. Ten skrypt sam rzuca, sam zapisuje
wynik w Campaigns/<kampania>/gm.json (zaciemnionym, żeby nie dało się go
przeczytać przypadkiem) i wypisuje tylko to, co już się wydarzyło.

Przykłady:
    python Scripts/gm.py --kampania Kloc czas --data 1990-03-21 --teraz 23:30
    python Scripts/gm.py --kampania Kloc timer --etykieta n1 --tablica opoznienie --od 0:40 --nie-wczesniej 1:00
    python Scripts/gm.py --kampania Kloc czas --teraz 1:50
    python Scripts/gm.py --kampania Kloc usun --etykieta n1
    python Scripts/gm.py --kampania Kloc pokaz

Polecenia:
    czas    ustawia zegar świata (pierwszy raz z --data) i wypisuje zdarzenia,
            których godzina właśnie minęła; przyszłych nigdy nie wypisuje
    timer   rzuca 3K6 według nazwanej tablicy z gm_tables.json, której
            wartości to minuty, i zapisuje ukryte zdarzenie; wypisuje tylko
            potwierdzenie
    usun    usuwa ukryte zdarzenie albo ukryty rzut, np. gdy ciało zostało
            zniszczone przed czasem
    pokaz   wypisuje cały ukryty stan; tylko przy wznowieniu gry

Nazwane tablice leżą w plikach gm_tables.json w folderach settingów
i scenariuszy (Settings/*/gm_tables.json, Scenarios/*/gm_tables.json).
Ukryte rzuty z tablicą tekstową wykonuje Scripts/roll.py --ukryty.
"""

import argparse
import base64
import json
import random
import sys
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAMPAIGNS = ROOT / "Campaigns"
STATE_FILE = "gm.json"
TABLES_FILE = "gm_tables.json"
FORMAT = "gm-base64-1"
MIN, MAX = 3, 18
CLOCK_FMT = "%Y-%m-%d %H:%M"

rng = random.SystemRandom()


def campaign_folder(name):
    if not name or name in (".", "..") or any(c in name for c in "/\\"):
        sys.exit(f"Błąd: '{name}' nie jest poprawną nazwą kampanii.")
    folder = CAMPAIGNS / name
    if not folder.is_dir():
        known = sorted(p.name for p in CAMPAIGNS.iterdir() if p.is_dir()) if CAMPAIGNS.is_dir() else []
        hint = f" Istniejące kampanie: {', '.join(known)}." if known else " Nie ma jeszcze żadnej kampanii."
        sys.exit(f"Błąd: kampania '{name}' nie istnieje (brak folderu Campaigns/{name}).{hint}")
    return folder


def load_state(folder):
    path = folder / STATE_FILE
    if not path.exists():
        return {"zegar": None, "zdarzenia": {}, "rzuty": {}}
    with path.open(encoding="utf-8") as fh:
        wrapper = json.load(fh)
    if wrapper.get("format") != FORMAT:
        sys.exit(f"Błąd: nieznany format pliku {path}.")
    return json.loads(base64.b64decode(wrapper["dane"]).decode("utf-8"))


def save_state(folder, state):
    data = base64.b64encode(json.dumps(state, ensure_ascii=False).encode("utf-8")).decode("ascii")
    with (folder / STATE_FILE).open("w", encoding="utf-8", newline="\n") as fh:
        json.dump({"format": FORMAT, "dane": data}, fh)
        fh.write("\n")


def label_taken(state, label):
    return label in state["zdarzenia"] or label in state["rzuty"]


def log_hidden(folder, label, source):
    """Do Rolls.log trafia tylko informacja, że był rzut ukryty, bez wyniku."""
    with (folder / "Rolls.log").open("a", encoding="utf-8") as log:
        log.write(f"=== {datetime.now().isoformat(timespec='seconds')}\nRzut ukryty: {label} ({source})\n\n")


def load_tables():
    """Nazwane tablice ze wszystkich gm_tables.json settingów i scenariuszy."""
    tables, origin = {}, {}
    for path in sorted(ROOT.glob(f"Settings/*/{TABLES_FILE}")) + sorted(ROOT.glob(f"Scenarios/*/{TABLES_FILE}")):
        with path.open(encoding="utf-8") as fh:
            data = json.load(fh)
        for name, table in data.items():
            if name in tables:
                sys.exit(f"Błąd: tablica '{name}' jest zdefiniowana w {origin[name]} i w {path.relative_to(ROOT)}.")
            tables[name] = table
            origin[name] = path.relative_to(ROOT).as_posix()
    return tables


def table_entries(name, tables):
    """Lista (od, do, wartość) nazwanej tablicy, sprawdzona pod kątem pokrycia 3-18."""
    if name not in tables:
        known = ", ".join(sorted(tables)) or "brak"
        sys.exit(f"Błąd: nie ma tablicy '{name}'. Dostępne: {known}.")
    entries = []
    for span, value in tables[name]["wpisy"].items():
        try:
            low, high = (int(x) for x in span.split("-", 1)) if "-" in span else (int(span),) * 2
        except ValueError:
            sys.exit(f"Błąd: zakres '{span}' w tablicy '{name}' nie jest liczbą ani zakresem 'od-do'.")
        entries.append((low, high, value))
    covered = Counter(v for low, high, _ in entries for v in range(low, high + 1))
    if any(v not in covered for v in range(MIN, MAX + 1)) or any(n > 1 for n in covered.values()) \
            or any(v < MIN or v > MAX for v in covered):
        sys.exit(f"Błąd: tablica '{name}' musi pokrywać wyniki {MIN}-{MAX} bez luk i nakładania się.")
    return sorted(entries)


def roll_3k6():
    dice = [rng.randint(1, 6) for _ in range(3)]
    return dice, sum(dice)


def lookup(entries, total):
    return next(v for low, high, v in entries if low <= total <= high)


def parse_hm(text):
    try:
        hour, minute = (int(x) for x in text.split(":", 1))
    except ValueError:
        sys.exit(f"Błąd: '{text}' nie jest godziną w formacie GG:MM.")
    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        sys.exit(f"Błąd: '{text}' nie jest poprawną godziną.")
    return hour, minute


def at_or_before(ref, hm):
    """Ostatnia chwila o godzinie hm, nie późniejsza niż ref."""
    moment = ref.replace(hour=hm[0], minute=hm[1])
    return moment - timedelta(days=1) if moment > ref else moment


def at_or_after(ref, hm):
    """Pierwsza chwila o godzinie hm, nie wcześniejsza niż ref."""
    moment = ref.replace(hour=hm[0], minute=hm[1])
    return moment + timedelta(days=1) if moment < ref else moment


def get_clock(state):
    if not state["zegar"]:
        sys.exit("Błąd: zegar świata nie jest ustawiony. Użyj: czas --data RRRR-MM-DD --teraz GG:MM.")
    return datetime.strptime(state["zegar"], CLOCK_FMT)


def cmd_czas(args, folder, state):
    hm = parse_hm(args.teraz)
    if args.data:
        try:
            day = datetime.strptime(args.data, "%Y-%m-%d")
        except ValueError:
            sys.exit(f"Błąd: '{args.data}' nie jest datą w formacie RRRR-MM-DD.")
        clock = day.replace(hour=hm[0], minute=hm[1])
    else:
        clock = at_or_after(get_clock(state), hm)
    state["zegar"] = clock.strftime(CLOCK_FMT)

    due = sorted((e["godzina"], label, e) for label, e in state["zdarzenia"].items()
                 if not e["zgloszone"] and e["godzina"] <= state["zegar"])
    print(f"Zegar: {state['zegar']}")
    if not due:
        print("Brak nowych zdarzeń.")
    for moment, label, event in due:
        event["zgloszone"] = True
        about = f": {event['opis']}" if event.get("opis") else ""
        print(f"Teraz: {label}{about} (o {moment[-5:]})")
    save_state(folder, state)


def cmd_timer(args, folder, state):
    if label_taken(state, args.etykieta):
        sys.exit(f"Błąd: etykieta '{args.etykieta}' jest już zajęta.")
    clock = get_clock(state)
    entries = table_entries(args.tablica, load_tables())
    if not all(isinstance(v, int) for _, _, v in entries):
        sys.exit(f"Błąd: tablica '{args.tablica}' nie podaje minut, więc nie nadaje się do timera. "
                 "Ukryty rzut z tablicą tekstową wykonuje Scripts/roll.py --ukryty.")
    start = at_or_before(clock, parse_hm(args.od)) if args.od else clock
    dice, total = roll_3k6()
    moment = start + timedelta(minutes=lookup(entries, total))
    if args.nie_wczesniej:
        moment = max(moment, at_or_after(start, parse_hm(args.nie_wczesniej)))
    state["zdarzenia"][args.etykieta] = {
        "godzina": moment.strftime(CLOCK_FMT),
        "opis": args.opis,
        "tablica": args.tablica,
        "od": start.strftime(CLOCK_FMT),
        "kosci": dice,
        "wynik": total,
        "zgloszone": False,
    }
    save_state(folder, state)
    log_hidden(folder, args.etykieta, f"timer, tablica {args.tablica}")
    print(f"Zapisano ukryte zdarzenie {args.etykieta}.")


def cmd_usun(args, folder, state):
    for kind in ("zdarzenia", "rzuty"):
        if args.etykieta in state[kind]:
            del state[kind][args.etykieta]
            save_state(folder, state)
            print(f"Usunięto {args.etykieta}.")
            return
    sys.exit(f"Błąd: nie ma etykiety '{args.etykieta}'.")


def cmd_pokaz(args, folder, state):
    print(f"Zegar: {state['zegar'] or 'nieustawiony'}")
    events = state["zdarzenia"]
    rolls = state["rzuty"]
    if args.etykieta:
        if not label_taken(state, args.etykieta):
            sys.exit(f"Błąd: nie ma etykiety '{args.etykieta}'.")
        events = {k: v for k, v in events.items() if k == args.etykieta}
        rolls = {k: v for k, v in rolls.items() if k == args.etykieta}
    print("Zdarzenia:" if events else "Zdarzenia: brak")
    for label, e in sorted(events.items(), key=lambda kv: kv[1]["godzina"]):
        status = "nastąpiło" if e["zgloszone"] else "czeka"
        about = f" {e['opis']}" if e.get("opis") else ""
        print(f"  {label}{about}: {e['godzina']} ({status}; od {e['od']}, tablica {e['tablica']}, wynik {e['wynik']})")
    print("Rzuty ukryte:" if rolls else "Rzuty ukryte: brak")
    for label, r in rolls.items():
        about = f" {r['opis']}" if r.get("opis") else ""
        print(f"  {label}{about}: wynik {r['wynik']}, {r['rezultat']}")


def main():
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Ukryty stan MG: zegar, ukryte zdarzenia i rzuty.")
    parser.add_argument("--kampania", required=True, help="nazwa folderu kampanii w Campaigns/")
    sub = parser.add_subparsers(dest="polecenie", required=True)

    p = sub.add_parser("czas", help="ustaw zegar świata i wypisz zdarzenia, które właśnie nastąpiły")
    p.add_argument("--teraz", required=True, help="godzina w świecie, GG:MM")
    p.add_argument("--data", help="data w świecie, RRRR-MM-DD (przy pierwszym ustawieniu albo korekcie)")

    p = sub.add_parser("timer", help="rzuć ukryty czas zdarzenia według nazwanej tablicy")
    p.add_argument("--etykieta", required=True, help="neutralna etykieta, np. n1")
    p.add_argument("--tablica", required=True, help="nazwa tablicy z gm_tables.json (wartości w minutach)")
    p.add_argument("--od", help="godzina początku odliczania, GG:MM (domyślnie teraz)")
    p.add_argument("--nie-wczesniej", dest="nie_wczesniej", help="zdarzenie nie wcześniej niż o GG:MM")
    p.add_argument("--opis", default="", help="krótki, neutralny opis, widoczny w konsoli")

    p = sub.add_parser("usun", help="usuń ukryte zdarzenie albo ukryty rzut")
    p.add_argument("--etykieta", required=True)

    p = sub.add_parser("pokaz", help="wypisz cały ukryty stan (tylko przy wznowieniu gry)")
    p.add_argument("--etykieta", help="tylko ta etykieta")

    args = parser.parse_args()
    folder = campaign_folder(args.kampania)
    state = load_state(folder)
    {"czas": cmd_czas, "timer": cmd_timer, "usun": cmd_usun, "pokaz": cmd_pokaz}[args.polecenie](args, folder, state)


if __name__ == "__main__":
    main()
