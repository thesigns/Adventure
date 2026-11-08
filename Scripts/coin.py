"""Rzut monetą rozstrzygający spór między graczem a MG.

Przykład:
    python Scripts/coin.py --kampania Randuvil --opis "Czy postać zdążyła zamknąć bramę" --mg "brama była otwarta" --gracz "postać zamknęła bramę"

Wynik to "Rację ma MG" albo "Rację ma gracz", z szansą 50% na każdy.
--kampania to nazwa folderu kampanii w Campaigns/ (obowiązkowa).
Każdy rzut jest dopisywany do Campaigns/<kampania>/Rolls.log.
"""

import argparse
import random
import sys
from datetime import datetime
from pathlib import Path

CAMPAIGNS = Path(__file__).resolve().parent.parent / "Campaigns"
OUTCOMES = ("Rację ma MG", "Rację ma gracz")

rng = random.SystemRandom()


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


def main():
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Rzut monetą rozstrzygający spór między graczem a MG.")
    parser.add_argument("--kampania", required=True, help="nazwa folderu kampanii w Campaigns/")
    parser.add_argument("--opis", required=True, help="czego dotyczy spór")
    parser.add_argument("--mg", default="", help="stanowisko MG")
    parser.add_argument("--gracz", default="", help="stanowisko gracza")
    args = parser.parse_args()

    log_path = campaign_log(args.kampania)
    outcome = rng.choice(OUTCOMES)

    lines = [f"Rzut monetą: {args.opis}"]
    if args.mg:
        lines.append(f"Stanowisko MG: {args.mg}")
    if args.gracz:
        lines.append(f"Stanowisko gracza: {args.gracz}")
    lines.append(f"Rezultat: {outcome}")
    report = "\n".join(lines)
    print(report)

    with log_path.open("a", encoding="utf-8") as log:
        log.write(f"=== {datetime.now().isoformat(timespec='seconds')}\n{report}\n\n")


if __name__ == "__main__":
    main()
