"""Rzut 3K6 z tablicą rezultatów.

Przykład:
    python Scripts/roll.py --kampania Randuvil --opis "Wspinaczka na mur" --pdt 2 "3-4:upadek, lekka rana" "5-8:upadek, draśnięcie" "9-18:sukces"

Tablica musi pokrywać wyniki 3-18 bez luk i nakładania się.
--pdt N to wydane Punkty Determinacji: rzuca się 3+N kośćmi, N najsłabszych
się odrzuca, a trzy najlepsze sumuje.
--kampania to nazwa folderu kampanii w Campaigns/ (obowiązkowa).
--rundy N rzuca serię najwyżej N rzutów z tą samą tablicą (np. kolejne
rundy walki), a --stop "3-5,17-18" przerywa serię po wyniku z podanych
zakresów. Przy serii --pdt dotyczy każdego rzutu osobno.
Każdy rzut jest dopisywany do Campaigns/<kampania>/Rolls.log.
"""

import argparse
import itertools
import math
import random
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

MIN, MAX = 3, 18
KEPT = 3
MAX_PDT = 15
CAMPAIGNS = Path(__file__).resolve().parent.parent / "Campaigns"

rng = random.SystemRandom()


def odds(pdt):
    """Dokładny rozkład sumy trzech najlepszych kości z 3+pdt."""
    n = KEPT + pdt
    counts = Counter()
    for combo in itertools.combinations_with_replacement(range(1, 7), n):
        ways = math.factorial(n)
        for c in Counter(combo).values():
            ways //= math.factorial(c)
        counts[sum(combo[-KEPT:])] += ways
    total = 6 ** n
    return {v: c / total for v, c in counts.items()}


def campaign_log(name):
    """Ścieżka do rejestru rzutów kampanii. Kampania musi już mieć swój folder."""
    if not name or name in (".", "..") or any(c in name for c in "/\\"):
        sys.exit(f"Błąd: '{name}' nie jest poprawną nazwą kampanii.")
    folder = CAMPAIGNS / name
    if not folder.is_dir():
        known = sorted(p.name for p in CAMPAIGNS.iterdir() if p.is_dir()) if CAMPAIGNS.is_dir() else []
        hint = f" Istniejące kampanie: {', '.join(known)}." if known else " Nie ma jeszcze żadnej kampanii."
        sys.exit(f"Błąd: kampania '{name}' nie istnieje (brak folderu Campaigns/{name}).{hint}")
    return folder / "Rolls.log"


def pct(p):
    return "<0.1%" if 0 < p < 0.0005 else f"{p * 100:.1f}%"


def parse_table(entries):
    table = []
    for entry in entries:
        if ":" not in entry:
            sys.exit(f"Błąd: wpis tablicy '{entry}' nie ma formatu 'od-do:rezultat'.")
        span, outcome = entry.split(":", 1)
        span, outcome = span.strip(), outcome.strip()
        try:
            if "-" in span:
                low, high = (int(x) for x in span.split("-", 1))
            else:
                low = high = int(span)
        except ValueError:
            sys.exit(f"Błąd: zakres '{span}' nie jest liczbą ani zakresem 'od-do'.")
        if low > high or low < MIN or high > MAX:
            sys.exit(f"Błąd: zakres '{span}' wykracza poza {MIN}-{MAX} albo jest odwrócony.")
        if not outcome:
            sys.exit(f"Błąd: zakres '{span}' nie ma opisu rezultatu.")
        table.append((low, high, outcome))

    covered = Counter(v for low, high, _ in table for v in range(low, high + 1))
    missing = [v for v in range(MIN, MAX + 1) if v not in covered]
    doubled = sorted(v for v, n in covered.items() if n > 1)
    if missing:
        sys.exit(f"Błąd: tablica nie pokrywa wyników: {missing}.")
    if doubled:
        sys.exit(f"Błąd: wyniki przypisane do więcej niż jednego rezultatu: {doubled}.")
    return sorted(table)


def parse_stop(text):
    """Zbiór wyników, po których seria rzutów się kończy, np. '3-5,17-18'."""
    stop = set()
    if not text:
        return stop
    for part in text.split(","):
        part = part.strip()
        try:
            if "-" in part:
                low, high = (int(x) for x in part.split("-", 1))
            else:
                low = high = int(part)
        except ValueError:
            sys.exit(f"Błąd: zakres --stop '{part}' nie jest liczbą ani zakresem 'od-do'.")
        if low > high or low < MIN or high > MAX:
            sys.exit(f"Błąd: zakres --stop '{part}' wykracza poza {MIN}-{MAX} albo jest odwrócony.")
        stop.update(range(low, high + 1))
    return stop


def roll(pdt):
    dice = [rng.randint(1, 6) for _ in range(KEPT + pdt)]
    ranked = sorted(dice)
    dropped, kept = ranked[:pdt], ranked[pdt:]
    return dice, dropped, sum(kept)


def main():
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Rzut 3K6 z tablicą rezultatów.")
    parser.add_argument("tablica", nargs="+", help="wpisy 'od-do:rezultat', np. '9-18:sukces'")
    parser.add_argument("--kampania", required=True, help="nazwa folderu kampanii w Campaigns/")
    parser.add_argument("--opis", default="", help="czego dotyczy rzut")
    parser.add_argument("--pdt", type=int, default=0, help="wydane Punkty Determinacji (dodatkowe kości)")
    parser.add_argument("--rundy", type=int, default=1, help="najwyższa liczba rzutów w serii z tą samą tablicą")
    parser.add_argument("--stop", default="", help="wyniki kończące serię, np. '3-5,17-18'")
    args = parser.parse_args()

    if not 0 <= args.pdt <= MAX_PDT:
        sys.exit(f"Błąd: --pdt musi być liczbą od 0 do {MAX_PDT}.")
    if not 1 <= args.rundy <= 50:
        sys.exit("Błąd: --rundy musi być liczbą od 1 do 50.")
    if args.stop and args.rundy == 1:
        sys.exit("Błąd: --stop ma sens tylko przy serii (--rundy większe niż 1).")

    log_path = campaign_log(args.kampania)
    table = parse_table(args.tablica)
    stop = parse_stop(args.stop)
    base_odds = odds(0)
    pdt_odds = odds(args.pdt)

    lines = []
    if args.opis:
        lines.append(f"Rzut: {args.opis}")
    if args.pdt:
        lines.append(f"Punkty Determinacji: {args.pdt} ({KEPT + args.pdt}K6, liczą się 3 najlepsze)")
    if args.rundy > 1:
        stop_info = f", przerwanie po wynikach: {args.stop}" if args.stop else ""
        lines.append(f"Seria: najwyżej {args.rundy} rzutów{stop_info}")
    results = []
    for _ in range(args.rundy):
        dice, dropped, total = roll(args.pdt)
        outcome = next(o for low, high, o in table if low <= total <= high)
        results.append((dice, dropped, total, outcome))
        if total in stop:
            break

    lines.append("Tablica:")
    for low, high, o in table:
        span = f"{low}" if low == high else f"{low}-{high}"
        p0 = sum(base_odds.get(v, 0) for v in range(low, high + 1))
        p = sum(pdt_odds.get(v, 0) for v in range(low, high + 1))
        chance = f"{pct(p0)} -> {pct(p)}" if args.pdt else pct(p)
        single = args.rundy == 1 and low <= results[0][2] <= high
        marker = "  <--" if single else ""
        lines.append(f"  {span}: {o} [{chance}]{marker}")

    for n, (dice, dropped, total, outcome) in enumerate(results, 1):
        if args.rundy > 1:
            lines.append(f"Rzut {n}:")
        lines.append(f"Kości: {dice}")
        if args.pdt:
            lines.append(f"Odrzucone: {dropped}")
        lines.append(f"Wynik: {total}")
        lines.append(f"Rezultat: {outcome}")
    if args.rundy > 1:
        last = results[-1][2]
        if last in stop:
            lines.append(f"Seria przerwana po rzucie {len(results)} (wynik {last}).")
        else:
            lines.append(f"Seria zakończona po {len(results)} rzutach.")
        if args.pdt:
            lines.append(f"Wydane PDT w serii: {args.pdt * len(results)}")

    report = "\n".join(lines)
    print(report)

    with log_path.open("a", encoding="utf-8") as log:
        log.write(f"=== {datetime.now().isoformat(timespec='seconds')}\n{report}\n\n")


if __name__ == "__main__":
    main()
