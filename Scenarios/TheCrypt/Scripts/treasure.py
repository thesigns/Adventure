"""Random treasure of the scenario The Crypt.

Example:
    python Scenarios/TheCrypt/Scripts/treasure.py --campaign Randuvil --place sarcophagus

Places:
    sarcophagus  contents of one closed sarcophagus in the hall of graves (room 5)
    sack         random part of the loot in Corwin's sack (room 6)
    tomb         contents of the casket in Malric's tomb (room 8)

--campaign is the name of the campaign folder in Campaigns/ (required).
Every draw is appended to Campaigns/<campaign>/Rolls.log.
Values are in silver (see Settings/Generia/Equipment.md).
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


# Each entry: (weight, function returning (description, value in silver)).
def coins(dice, mult=1, what="old silver coins"):
    def make():
        n = d6(dice) * mult
        return f"{n} {what}", n
    return make


def item(name, value):
    return lambda: (name, value)


SARCOPHAGUS = [
    (8, item("only dust, bones and shreds of a shroud", 0)),
    (4, coins(1, 1)),
    (2, coins(2, 1)),
    (2, item("a silver cloak clasp shaped like a wolf's head", 15)),
    (2, item("a string of amber beads", 10)),
    (1, item("a ring with a garnet", 30)),
    (1, item("a gold earring with a pearl", 25)),
    (1, item("an ornate dagger in a silver-mounted sheath (an ordinary weapon)", 20)),
    (1, item("a copper bowl engraved with prayers", 3)),
]

SACK = [
    (3, coins(2, 1)),
    (2, item("a silver cloak clasp shaped like a wolf's head", 15)),
    (2, item("a string of amber beads", 10)),
    (1, item("a ring with a garnet", 30)),
    (1, item("a silver chain with the sign of Solarius", 12)),
    (1, item("a gilded belt buckle", 18)),
]

TOMB = [
    (3, coins(3, 2)),
    (2, item("a silver goblet with the wolf crest", 40)),
    (2, item("a gold chain with heavy links", 80)),
    (2, item("a diadem of dull silver with three garnets", 70)),
    (1, item("an ivory box full of dried herbs (worthless contents, but beautiful)", 25)),
    (1, item("a carved drinking horn in a silver mount", 35)),
]

PLACES = {
    "sarcophagus": ("Sarcophagus in the hall of graves", SARCOPHAGUS, 1),
    "sack": ("Corwin's sack (random part)", SACK, 2),
    "tomb": ("Casket in Malric's tomb", TOMB, 2),
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

    parser = argparse.ArgumentParser(description="Random treasure of the scenario The Crypt.")
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

    lines = [f"Treasure (The Crypt): {title}"]
    for name, value in found:
        lines.append(f"  - {name}" + (f" [about {value} s]" if value else ""))
    total = sum(v for _, v in found)
    lines.append(f"Total value: about {total} s")
    report = "\n".join(lines)
    print(report)

    with log_path.open("a", encoding="utf-8") as log:
        log.write(f"=== {datetime.now().isoformat(timespec='seconds')}\n{report}\n\n")


if __name__ == "__main__":
    main()
