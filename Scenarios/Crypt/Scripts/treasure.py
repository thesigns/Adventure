"""Random treasure of the Crypt scenario.

Example:
    python Scenarios/Crypt/Scripts/treasure.py --campaign Randuvil --place sarkofag

Places:
    sarkofag   contents of one closed sarcophagus in the hall of graves (room 5)
    worek      random part of the loot in Ostap's sack (room 6)
    grobowiec  contents of the casket in Borzywoj's tomb (room 8)

--campaign is the name of the campaign folder in Campaigns/ (required).
Every draw is appended to Campaigns/<campaign>/Rolls.log.
Item names and values (in grosze) are scenario content and stay in Polish.
"""

import argparse
import random
import sys
from datetime import datetime
from pathlib import Path

CAMPAIGNS = Path(__file__).resolve().parents[3] / "Campaigns"

rng = random.SystemRandom()


def d6(n):
    return sum(rng.randint(1, 6) for _ in range(n))


# Each entry: (weight, function returning (description, value in grosze)).
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
    """Path to the campaign's roll log. The campaign must already have its folder."""
    if not name or name in (".", "..") or any(c in name for c in "/\\"):
        sys.exit(f"Error: '{name}' is not a valid campaign name.")
    folder = CAMPAIGNS / name
    if not folder.is_dir():
        known = sorted(p.name for p in CAMPAIGNS.iterdir() if p.is_dir()) if CAMPAIGNS.is_dir() else []
        hint = f" Existing campaigns: {', '.join(known)}." if known else " There are no campaigns yet."
        sys.exit(f"Error: campaign '{name}' does not exist (no folder Campaigns/{name}).{hint}")
    return folder / "Rolls.log"


def draw(table):
    weights = [w for w, _ in table]
    make = rng.choices([m for _, m in table], weights=weights)[0]
    return make()


def main():
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Random treasure of the Crypt scenario.")
    parser.add_argument("--campaign", required=True, help="name of the campaign folder in Campaigns/")
    parser.add_argument("--place", required=True, choices=sorted(PLACES), help="where the character searches for treasure")
    args = parser.parse_args()

    log_path = campaign_log(args.campaign)
    title, table, count = PLACES[args.place]

    found, seen = [], set()
    while len(found) < count:
        name, value = draw(table)
        if name in seen and value:
            continue
        seen.add(name)
        found.append((name, value))

    lines = [f"Treasure (Crypt): {title}"]
    for name, value in found:
        lines.append(f"  - {name}" + (f" [about {value} gr]" if value else ""))
    total = sum(v for _, v in found)
    lines.append(f"Total value: about {total} gr")
    report = "\n".join(lines)
    print(report)

    with log_path.open("a", encoding="utf-8") as log:
        log.write(f"=== {datetime.now().isoformat(timespec='seconds')}\n{report}\n\n")


if __name__ == "__main__":
    main()
