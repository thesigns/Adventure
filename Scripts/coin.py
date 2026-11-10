"""Coin toss settling a dispute between the player and the GM.

Example:
    python Scripts/coin.py --campaign Randuvil --desc "Did the character manage to close the gate" --gm "the gate was open" --player "the character closed the gate"

The result is "The GM is right" or "The player is right", 50% each.
--campaign is the name of the campaign folder in Campaigns/ (required).
Every toss is appended to Campaigns/<campaign>/Rolls.log.
"""

import argparse
import random
import sys
from datetime import datetime

import gm

OUTCOMES = ("The GM is right", "The player is right")

rng = random.SystemRandom()


def main():
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Coin toss settling a dispute between the player and the GM.")
    parser.add_argument("--campaign", required=True, help="name of the campaign folder in Campaigns/")
    parser.add_argument("--desc", required=True, help="what the dispute is about")
    parser.add_argument("--gm", default="", help="the GM's position")
    parser.add_argument("--player", default="", help="the player's position")
    args = parser.parse_args()

    log_path = gm.campaign_folder(args.campaign) / "Rolls.log"
    outcome = rng.choice(OUTCOMES)

    lines = [f"Coin toss: {args.desc}"]
    if args.gm:
        lines.append(f"GM's position: {args.gm}")
    if args.player:
        lines.append(f"Player's position: {args.player}")
    lines.append(f"Outcome: {outcome}")
    report = "\n".join(lines)
    print(report)

    with log_path.open("a", encoding="utf-8") as log:
        log.write(f"=== {datetime.now().isoformat(timespec='seconds')}\n{report}\n\n")


if __name__ == "__main__":
    main()
