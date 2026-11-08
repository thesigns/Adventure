"""Losowe skarby scenariusza Krypta.

Przykład:
    python Scenarios/Krypta/treasure.py --kampania Randuvil --miejsce sarkofag

Miejsca:
    sarkofag   zawartość jednego zamkniętego sarkofagu w sali grobów (pokój 5)
    worek      losowa część łupu w worku Ostapa (pokój 6)
    grobowiec  zawartość szkatuły w grobowcu Borzywoja (pokój 8)

--kampania to nazwa folderu kampanii w Campaigns/ (obowiązkowa).
Każde losowanie jest dopisywane do Campaigns/<kampania>/Rolls.log.
"""

import argparse
import random
import sys
from datetime import datetime
from pathlib import Path

CAMPAIGNS = Path(__file__).resolve().parents[2] / "Campaigns"

rng = random.SystemRandom()


def d6(n):
    return sum(rng.randint(1, 6) for _ in range(n))


# Każda pozycja: (waga, funkcja zwracająca (opis, wartość w groszach)).
def coins(dice, mult=1, what="srebrnych groszy dawnego bicia"):
    def make():
        n = d6(dice) * mult
        return f"{n} {what}", n
    return make


def item(name, value):
    return lambda: (name, value)


SARKOFAG = [
    (8, item("tylko proch, kości i strzępy całunu", 0)),
    (4, coins(1, 1)),
    (2, coins(2, 1)),
    (2, item("srebrna zapinka do płaszcza w kształcie wilczej głowy", 15)),
    (2, item("sznur bursztynowych paciorków", 10)),
    (1, item("pierścień z granatem", 30)),
    (1, item("złoty kolczyk z perłą", 25)),
    (1, item("zdobiony sztylet w pochwie ze srebrnymi okuciami (zwykła broń)", 20)),
    (1, item("miedziana misa z wyrytymi modlitwami", 3)),
]

WOREK = [
    (3, coins(2, 1)),
    (2, item("srebrna zapinka do płaszcza w kształcie wilczej głowy", 15)),
    (2, item("sznur bursztynowych paciorków", 10)),
    (1, item("pierścień z granatem", 30)),
    (1, item("srebrny łańcuszek z krzyżykiem", 12)),
    (1, item("pozłacana klamra pasa", 18)),
]

GROBOWIEC = [
    (3, coins(3, 2)),
    (2, item("srebrny kielich z herbem wilka", 40)),
    (2, item("złoty łańcuch z ciężkimi ogniwami", 80)),
    (2, item("diadem z matowego srebra z trzema granatami", 70)),
    (1, item("szkatułka z kości słoniowej pełna zaschniętych ziół (bez wartości, ale piękna)", 25)),
    (1, item("rzeźbiony róg do picia w srebrnej oprawie", 35)),
]

PLACES = {
    "sarkofag": ("Sarkofag w sali grobów", SARKOFAG, 1),
    "worek": ("Worek Ostapa (część losowa)", WOREK, 2),
    "grobowiec": ("Szkatuła w grobowcu Borzywoja", GROBOWIEC, 2),
}


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


def draw(table):
    weights = [w for w, _ in table]
    make = rng.choices([m for _, m in table], weights=weights)[0]
    return make()


def main():
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Losowe skarby scenariusza Krypta.")
    parser.add_argument("--kampania", required=True, help="nazwa folderu kampanii w Campaigns/")
    parser.add_argument("--miejsce", required=True, choices=sorted(PLACES), help="gdzie postać szuka skarbu")
    args = parser.parse_args()

    log_path = campaign_log(args.kampania)
    title, table, count = PLACES[args.miejsce]

    found, seen = [], set()
    while len(found) < count:
        name, value = draw(table)
        if name in seen and value:
            continue
        seen.add(name)
        found.append((name, value))

    lines = [f"Skarb (Krypta): {title}"]
    for name, value in found:
        lines.append(f"  - {name}" + (f" [ok. {value} gr]" if value else ""))
    total = sum(v for _, v in found)
    lines.append(f"Łączna wartość: ok. {total} gr")
    report = "\n".join(lines)
    print(report)

    with log_path.open("a", encoding="utf-8") as log:
        log.write(f"=== {datetime.now().isoformat(timespec='seconds')}\n{report}\n\n")


if __name__ == "__main__":
    main()
