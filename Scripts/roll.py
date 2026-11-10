"""3d6 roll against an outcome table.

Example:
    python Scripts/roll.py --campaign Randuvil --desc "Climbing the wall" --dp 2 "3-4:falls, light wound" "5-8:falls, scratch" "9-18:success"

The table must cover results 3-18 with no gaps and no overlaps.
--dp N is the number of Determination Points spent: 3+N dice are rolled,
the N lowest are dropped and the best three are added up.
--campaign is the name of the campaign folder in Campaigns/ (required).
--rounds N rolls a series of at most N rolls with the same table (e.g.
consecutive combat rounds), and --stop "3-5,17-18" ends the series after
a result in the given ranges. In a series --dp applies to each roll.
Every roll is appended to Campaigns/<campaign>/Rolls.log.

--table NAME takes the table from Tables/GmTables.json of a setting or
scenario instead of entries in the command.
--preview prints the table with the chances for 0-3 DP (or up to --dp, if
higher) without rolling and without an entry in Rolls.log. The GM shows it
to the player before their decision instead of computing chances mentally:
    python Scripts/roll.py --campaign Randuvil --preview "3-8:failure" "9-18:success"

--hidden --label L is a roll hidden from the player: the result goes only
to Campaigns/<campaign>/Gm.json (see Scripts/gm.py), and the script prints
only a confirmation. The table is then given with --table, so that the
command reveals nothing:
    python Scripts/roll.py --campaign Randuvil --hidden --label r1 --table doubtful
"""

import argparse
import itertools
import math
import random
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

import gm

MIN, MAX = 3, 18
KEPT = 3
MAX_DP = 15
CAMPAIGNS = Path(__file__).resolve().parent.parent / "Campaigns"

rng = random.SystemRandom()


def odds(dp):
    """Exact distribution of the sum of the best three of 3+dp dice."""
    n = KEPT + dp
    counts = Counter()
    for combo in itertools.combinations_with_replacement(range(1, 7), n):
        ways = math.factorial(n)
        for c in Counter(combo).values():
            ways //= math.factorial(c)
        counts[sum(combo[-KEPT:])] += ways
    total = 6 ** n
    return {v: c / total for v, c in counts.items()}


def campaign_log(name):
    """Path to the campaign's roll log. The campaign must already have its folder."""
    return gm.campaign_folder(name) / "Rolls.log"


def pct(p):
    return "<0.1%" if 0 < p < 0.0005 else f"{p * 100:.1f}%"


def parse_span(span, what):
    """A single result or a 'from-to' range, checked against 3-18."""
    try:
        if "-" in span:
            low, high = (int(x) for x in span.split("-", 1))
        else:
            low = high = int(span)
    except ValueError:
        sys.exit(f"Error: {what} '{span}' is not a number or a 'from-to' range.")
    if low > high or low < MIN or high > MAX:
        sys.exit(f"Error: {what} '{span}' is outside {MIN}-{MAX} or reversed.")
    return low, high


def parse_table(entries):
    table = []
    for entry in entries:
        if ":" not in entry:
            sys.exit(f"Error: table entry '{entry}' is not in the form 'from-to:outcome'.")
        span, outcome = entry.split(":", 1)
        span, outcome = span.strip(), outcome.strip()
        low, high = parse_span(span, "range")
        if not outcome:
            sys.exit(f"Error: range '{span}' has no outcome.")
        table.append((low, high, outcome))

    covered = Counter(v for low, high, _ in table for v in range(low, high + 1))
    missing = [v for v in range(MIN, MAX + 1) if v not in covered]
    doubled = sorted(v for v, n in covered.items() if n > 1)
    if missing:
        sys.exit(f"Error: the table does not cover results: {missing}.")
    if doubled:
        sys.exit(f"Error: results assigned to more than one outcome: {doubled}.")
    return sorted(table)


def parse_stop(text):
    """Set of results after which a series of rolls ends, e.g. '3-5,17-18'."""
    stop = set()
    if not text:
        return stop
    for part in text.split(","):
        low, high = parse_span(part.strip(), "--stop range")
        stop.update(range(low, high + 1))
    return stop


def preview(args, table):
    """The table with chances for increasing numbers of DP, without rolling or logging."""
    levels = list(range(max(3, args.dp) + 1))
    by_level = [odds(n) for n in levels]
    lines = [f"Preview (no roll): {args.desc}" if args.desc else "Preview (no roll)"]
    lines.append("Chances with " + " / ".join(str(n) for n in levels) + " DP:")
    rows = []
    for low, high, o in table:
        span = f"{low}" if low == high else f"{low}-{high}"
        chances = " / ".join(pct(sum(d.get(v, 0) for v in range(low, high + 1))) for d in by_level)
        rows.append((f"{span}: {o}", chances))
    width = max(len(label) for label, _ in rows)
    lines.extend(f"  {label.ljust(width)}  {chances}" for label, chances in rows)
    print("\n".join(lines))


def roll(dp):
    dice = [rng.randint(1, 6) for _ in range(KEPT + dp)]
    ranked = sorted(dice)
    dropped, kept = ranked[:dp], ranked[dp:]
    return dice, dropped, sum(kept)


def hidden_roll(args, folder, table):
    """Hidden roll: gm.py stores the result, and only a confirmation is printed."""
    state = gm.load_state(folder)
    if gm.label_taken(state, args.label):
        sys.exit(f"Error: label '{args.label}' is already taken.")
    dice, _, total = roll(0)
    state["rolls"][args.label] = {
        "desc": args.desc,
        "table": args.table_name or "",
        "dice": dice,
        "result": total,
        "outcome": next(o for low, high, o in table if low <= total <= high),
        "time": datetime.now().isoformat(timespec="seconds"),
    }
    gm.save_state(folder, state)
    gm.log_hidden(folder, args.label, f"roll.py, table {args.table_name or 'from the command'}")
    print(f"Hidden roll saved: {args.label}.")


def main():
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="3d6 roll against an outcome table.")
    parser.add_argument("entries", nargs="*", help="'from-to:outcome' entries, e.g. '9-18:success'")
    parser.add_argument("--campaign", required=True, help="name of the campaign folder in Campaigns/")
    parser.add_argument("--desc", default="", help="what the roll is about")
    parser.add_argument("--dp", type=int, default=0, help="Determination Points spent (extra dice)")
    parser.add_argument("--rounds", type=int, default=1, help="maximum number of rolls in a series with the same table")
    parser.add_argument("--stop", default="", help="results that end the series, e.g. '3-5,17-18'")
    parser.add_argument("--table", dest="table_name", help="name of a table from Tables/GmTables.json instead of entries")
    parser.add_argument("--hidden", action="store_true", help="hidden roll: result only in the campaign's Gm.json")
    parser.add_argument("--label", help="neutral label of a hidden roll, e.g. r1")
    parser.add_argument("--preview", action="store_true",
                        help="only print the table with chances for 0-3 DP, without rolling or logging")
    args = parser.parse_args()

    if not 0 <= args.dp <= MAX_DP:
        sys.exit(f"Error: --dp must be a number from 0 to {MAX_DP}.")
    if not 1 <= args.rounds <= 50:
        sys.exit("Error: --rounds must be a number from 1 to 50.")
    if args.stop and args.rounds == 1:
        sys.exit("Error: --stop only makes sense in a series (--rounds greater than 1).")
    if bool(args.entries) == bool(args.table_name):
        sys.exit("Error: give either table entries in the command or --table NAME.")
    if args.preview and args.hidden:
        sys.exit("Error: a hidden roll cannot be previewed, because the player does not see its table.")
    if args.hidden:
        if not args.label:
            sys.exit("Error: a hidden roll requires --label.")
        if args.dp or args.rounds > 1:
            sys.exit("Error: a hidden roll cannot have --dp or --rounds, because the player does not see the table.")
    elif args.label:
        sys.exit("Error: --label only makes sense with --hidden.")

    log_path = campaign_log(args.campaign)
    if args.table_name:
        entries = gm.table_entries(args.table_name, gm.load_tables())
        spans = [f"{low}-{high}:{v} min" if isinstance(v, int) else f"{low}-{high}:{v}" for low, high, v in entries]
        table = parse_table(spans)
    else:
        table = parse_table(args.entries)

    if args.preview:
        preview(args, table)
        return
    if args.hidden:
        hidden_roll(args, log_path.parent, table)
        return

    stop = parse_stop(args.stop)
    base_odds = odds(0)
    dp_odds = odds(args.dp)

    lines = []
    if args.desc:
        lines.append(f"Roll: {args.desc}")
    if args.dp:
        lines.append(f"Determination Points: {args.dp} ({KEPT + args.dp}d6, best 3 count)")
    if args.rounds > 1:
        stop_info = f", stopping after results: {args.stop}" if args.stop else ""
        lines.append(f"Series: at most {args.rounds} rolls{stop_info}")
    results = []
    for _ in range(args.rounds):
        dice, dropped, total = roll(args.dp)
        outcome = next(o for low, high, o in table if low <= total <= high)
        results.append((dice, dropped, total, outcome))
        if total in stop:
            break

    lines.append("Table:")
    for low, high, o in table:
        span = f"{low}" if low == high else f"{low}-{high}"
        p0 = sum(base_odds.get(v, 0) for v in range(low, high + 1))
        p = sum(dp_odds.get(v, 0) for v in range(low, high + 1))
        chance = f"{pct(p0)} -> {pct(p)}" if args.dp else pct(p)
        single = args.rounds == 1 and low <= results[0][2] <= high
        marker = "  <--" if single else ""
        lines.append(f"  {span}: {o} [{chance}]{marker}")

    for n, (dice, dropped, total, outcome) in enumerate(results, 1):
        if args.rounds > 1:
            lines.append(f"Roll {n}:")
        lines.append(f"Dice: {dice}")
        if args.dp:
            lines.append(f"Dropped: {dropped}")
        lines.append(f"Result: {total}")
        lines.append(f"Outcome: {outcome}")
    if args.rounds > 1:
        last = results[-1][2]
        if last in stop:
            lines.append(f"Series stopped after roll {len(results)} (result {last}).")
        else:
            lines.append(f"Series finished after {len(results)} rolls.")
        if args.dp:
            lines.append(f"DP spent in the series: {args.dp * len(results)}")

    report = "\n".join(lines)
    print(report)

    with log_path.open("a", encoding="utf-8") as log:
        log.write(f"=== {datetime.now().isoformat(timespec='seconds')}\n{report}\n\n")


if __name__ == "__main__":
    main()
