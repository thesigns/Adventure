"""The GM's hidden campaign state: world clock, hidden events and hidden rolls.

The player sees the same console as the GM, so secrets must not end up in
commands, diffs or script output. This script rolls by itself, stores the
result in Campaigns/<campaign>/Gm.json (obfuscated, so that it cannot be
read by accident) and prints only what has already happened.

Examples:
    python Scripts/gm.py --campaign Randuvil time --date 1240-04-05 --now 16:00
    python Scripts/gm.py --campaign Randuvil time --now 22:00 --setting SettingName
    python Scripts/gm.py --campaign Randuvil timer --label n1 --table delay --from 0:40 --not-before 1:00
    python Scripts/gm.py --campaign Randuvil time --now 1:50
    python Scripts/gm.py --campaign Randuvil remove --label n1
    python Scripts/gm.py --campaign Randuvil show

Commands:
    time    sets the world clock (the first time with --date) and prints the
            events whose time has just passed; never prints future ones;
            with --setting (remembered in the campaign state) dates follow
            the calendar in Settings/<setting>/Tables/Calendar.json, if the
            setting has one, with the weekday, month, season and moon
            phases printed, and the
            time of day comes from Settings/<setting>/Tables/Daylight.json
    timer   rolls 3d6 on a named table from Tables/GmTables.json whose
            values are minutes, and stores a hidden event; prints only
            a confirmation; --from is the occurrence of that time closest
            to the clock, earlier or later (at 17:50 --from 23:00 means this
            evening, at 1:00 --from 0:40 means twenty minutes ago); an event
            that would fall before the clock happens at once and is reported
            by the next `time`
    remove  removes a hidden event or a hidden roll, e.g. when the character
            prevented the event before it happened
    show    prints the whole hidden state; only when resuming play

Named tables live in Tables/GmTables.json files in setting and scenario
folders (Settings/*/Tables/GmTables.json, Scenarios/*/Tables/GmTables.json),
in the form {"name": {"entries": {"3-5": 10, "6-18": 30}}}.
Hidden rolls with a text table are made by Scripts/roll.py --hidden.

Calendar.json has the form {"months": [{"name": "Tiriwen", "days": 30,
"season": "spring"}, ...], "weekdays": ["Duriel", ...], "first_weekday":
"Duriel", "moons": [{"name": "Selwen", "phases": ["new", ...]}]}, where
first_weekday is the weekday of the first day of year 1, and a moon's phases
are listed for each night of its cycle, starting with the night of the first
day of year 1. "season", "weekdays" and "moons" are optional. Every year has
the same months. Dates are written YYYY-MM-DD, with months numbered from 01
in the order listed. Without Calendar.json dates follow the Gregorian
calendar.

Daylight.json has the form {"days": {"MM-DD": {"sunrise": "HH:MM",
"sunset": "HH:MM", "darkness": "HH:MM-HH:MM"}}}, with days in the setting's
calendar; without "darkness" the night is a white night. Values between the
listed days are interpolated.
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
STATE_FILE = "Gm.json"
TABLES_FILE = "Tables/GmTables.json"
DAYLIGHT_FILE = "Tables/Daylight.json"
CALENDAR_FILE = "Tables/Calendar.json"
FORMAT = "gm-base64-2"
MIN, MAX = 3, 18
EPOCH = datetime(1, 1, 1)

rng = random.SystemRandom()


def campaign_folder(name):
    """The campaign folder in Campaigns/. The campaign must already exist."""
    if not name or name in (".", "..") or any(c in name for c in "/\\"):
        sys.exit(f"Error: '{name}' is not a valid campaign name.")
    folder = CAMPAIGNS / name
    if not folder.is_dir():
        known = sorted(p.name for p in CAMPAIGNS.iterdir() if p.is_dir()) if CAMPAIGNS.is_dir() else []
        hint = f" Existing campaigns: {', '.join(known)}." if known else " There are no campaigns yet."
        sys.exit(f"Error: campaign '{name}' does not exist (no folder Campaigns/{name}).{hint}")
    return folder


def load_state(folder):
    path = folder / STATE_FILE
    if not path.exists():
        return {"clock": None, "events": {}, "rolls": {}}
    with path.open(encoding="utf-8") as fh:
        wrapper = json.load(fh)
    if wrapper.get("format") != FORMAT:
        sys.exit(f"Error: unknown format of file {path}.")
    return json.loads(base64.b64decode(wrapper["data"]).decode("utf-8"))


def save_state(folder, state):
    data = base64.b64encode(json.dumps(state, ensure_ascii=False).encode("utf-8")).decode("ascii")
    with (folder / STATE_FILE).open("w", encoding="utf-8", newline="\n") as fh:
        json.dump({"format": FORMAT, "data": data}, fh)
        fh.write("\n")


def label_taken(state, label):
    return label in state["events"] or label in state["rolls"]


def log_hidden(folder, label, source):
    """Rolls.log only records that a hidden roll happened, without the result."""
    with (folder / "Rolls.log").open("a", encoding="utf-8") as log:
        log.write(f"=== {datetime.now().isoformat(timespec='seconds')}\nHidden roll: {label} ({source})\n\n")


def load_tables():
    """Named tables from all Tables/GmTables.json files of settings and scenarios."""
    tables, origin = {}, {}
    for path in sorted(ROOT.glob(f"Settings/*/{TABLES_FILE}")) + sorted(ROOT.glob(f"Scenarios/*/{TABLES_FILE}")):
        with path.open(encoding="utf-8") as fh:
            data = json.load(fh)
        for name, table in data.items():
            if name in tables:
                sys.exit(f"Error: table '{name}' is defined in {origin[name]} and in {path.relative_to(ROOT)}.")
            tables[name] = table
            origin[name] = path.relative_to(ROOT).as_posix()
    return tables


def table_entries(name, tables):
    """List of (from, to, value) of a named table, checked to cover 3-18."""
    if name not in tables:
        known = ", ".join(sorted(tables)) or "none"
        sys.exit(f"Error: there is no table '{name}'. Available: {known}.")
    entries = []
    for span, value in tables[name]["entries"].items():
        try:
            low, high = (int(x) for x in span.split("-", 1)) if "-" in span else (int(span),) * 2
        except ValueError:
            sys.exit(f"Error: range '{span}' in table '{name}' is not a number or a 'from-to' range.")
        entries.append((low, high, value))
    covered = Counter(v for low, high, _ in entries for v in range(low, high + 1))
    if any(v not in covered for v in range(MIN, MAX + 1)) or any(n > 1 for n in covered.values()) \
            or any(v < MIN or v > MAX for v in covered):
        sys.exit(f"Error: table '{name}' must cover results {MIN}-{MAX} with no gaps and no overlaps.")
    return sorted(entries)


def roll_3d6():
    dice = [rng.randint(1, 6) for _ in range(3)]
    return dice, sum(dice)


def lookup(entries, total):
    return next(v for low, high, v in entries if low <= total <= high)


def parse_hm(text):
    try:
        hour, minute = (int(x) for x in text.split(":", 1))
    except ValueError:
        sys.exit(f"Error: '{text}' is not a time in the format HH:MM.")
    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        sys.exit(f"Error: '{text}' is not a valid time.")
    return hour, minute


def nearest(ref, hm):
    """The moment at time hm closest to ref, earlier or later (a tie goes to the earlier)."""
    moment = ref.replace(hour=hm[0], minute=hm[1])
    return min((moment - timedelta(days=1), moment, moment + timedelta(days=1)),
               key=lambda m: abs(m - ref))


def at_or_after(ref, hm):
    """The first moment at time hm no earlier than ref."""
    moment = ref.replace(hour=hm[0], minute=hm[1])
    return moment + timedelta(days=1) if moment < ref else moment


class Calendar:
    """Dates of a setting's calendar, kept internally as datetimes.

    Without months it is the Gregorian calendar. With months, every year has
    the same days, and day n of the calendar's era is EPOCH + n - 1 days, so
    the rest of the script can add minutes with timedelta as usual.
    """

    def __init__(self, months=None, weekdays=None, first_weekday=0, seasons=None, moons=None):
        self.months = months
        self.weekdays = weekdays or []
        self.first_weekday = first_weekday
        self.seasons = seasons or []
        self.moons = moons or []
        self.year_len = sum(days for _, days in months) if months else 365

    def make(self, year, month, day, where):
        if not self.months:
            try:
                return datetime(year, month, day)
            except ValueError:
                sys.exit(f"Error: '{where}' is not a valid date.")
        if not (year >= 1 and 1 <= month <= len(self.months) and 1 <= day <= self.months[month - 1][1]):
            sys.exit(f"Error: '{where}' is not a valid date in the setting's calendar.")
        doy = sum(days for _, days in self.months[:month - 1]) + day
        return EPOCH + timedelta(days=(year - 1) * self.year_len + doy - 1)

    def parse(self, text):
        """A date YYYY-MM-DD, optionally followed by HH:MM."""
        date, _, hm = text.partition(" ")
        try:
            year, month, day = (int(x) for x in date.split("-"))
        except ValueError:
            sys.exit(f"Error: '{text}' is not a date in the format YYYY-MM-DD.")
        moment = self.make(year, month, day, text)
        if hm:
            hour, minute = parse_hm(hm)
            moment = moment.replace(hour=hour, minute=minute)
        return moment

    def split(self, moment):
        """Year, month, day and day of the year of a moment."""
        if not self.months:
            leap_free = datetime(2001, moment.month, min(moment.day, 28) if moment.month == 2 else moment.day)
            return moment.year, moment.month, moment.day, leap_free.timetuple().tm_yday
        days = (moment - EPOCH).days
        year, doy = days // self.year_len + 1, days % self.year_len + 1
        rest = doy
        for month, (_, length) in enumerate(self.months, 1):
            if rest <= length:
                return year, month, rest, doy
            rest -= length

    def fmt(self, moment):
        year, month, day, _ = self.split(moment)
        return f"{year:04d}-{month:02d}-{day:02d} {moment.hour:02d}:{moment.minute:02d}"

    def describe(self, moment):
        """Weekday, month, season and moons, e.g. 'Lumiel, 20 Saelis, summer; Selwen full, Nimras full'.

        Empty without a calendar.
        """
        if not self.months:
            return ""
        _, month, day, _ = self.split(moment)
        days = (moment - EPOCH).days
        text = f"{day} {self.months[month - 1][0]}"
        if self.weekdays:
            text = f"{self.weekdays[(days + self.first_weekday) % len(self.weekdays)]}, {text}"
        if self.seasons and self.seasons[month - 1]:
            text += f", {self.seasons[month - 1]}"
        if self.moons:
            text += "; " + ", ".join(f"{name} {phases[days % len(phases)]}" for name, phases in self.moons)
        return text

    def day_of_year(self, key, where):
        """Day of the year of a day 'MM-DD' in this calendar."""
        try:
            month, day = (int(x) for x in key.split("-"))
        except ValueError:
            sys.exit(f"Error: '{key}' in {where} is not a day in the format MM-DD.")
        return self.split(self.make(1 if self.months else 2001, month, day, f"{key} in {where}"))[3]


def load_calendar(setting):
    """The setting's calendar, or the Gregorian one if it has no Calendar.json."""
    path = ROOT / "Settings" / setting / CALENDAR_FILE if setting else None
    if not path or not path.exists():
        return Calendar()
    with path.open(encoding="utf-8") as fh:
        data = json.load(fh)
    months = [(m["name"], int(m["days"])) for m in data["months"]]
    weekdays = data.get("weekdays", [])
    first = weekdays.index(data["first_weekday"]) if data.get("first_weekday") in weekdays else 0
    seasons = [m.get("season", "") for m in data["months"]]
    moons = [(m["name"], m["phases"]) for m in data.get("moons", [])]
    return Calendar(months, weekdays, first, seasons, moons)


def get_clock(state, cal):
    if not state["clock"]:
        sys.exit("Error: the world clock is not set. Use: time --date YYYY-MM-DD --now HH:MM.")
    return cal.parse(state["clock"])


def hm_minutes(text, where):
    try:
        hour, minute = (int(x) for x in text.split(":", 1))
    except (ValueError, AttributeError):
        sys.exit(f"Error: '{text}' in {where} is not a time in the format HH:MM.")
    return hour * 60 + minute


def load_daylight(setting, cal):
    """Rows (day of year, sunrise, sunset, start of darkness, end of darkness) in minutes.

    Darkness lasts from the evening (start) past midnight to the morning
    (end). No darkness (white nights) is start = 1440 and end = 0.
    """
    path = ROOT / "Settings" / setting / DAYLIGHT_FILE
    if not path.exists():
        sys.exit(f"Error: setting '{setting}' has no file {DAYLIGHT_FILE}.")
    with path.open(encoding="utf-8") as fh:
        days = json.load(fh)["days"]
    rows = []
    for key, d in days.items():
        doy = cal.day_of_year(key, path.name)
        if d.get("darkness"):
            start, end = d["darkness"].split("-", 1)
            start, end = hm_minutes(start, path.name), hm_minutes(end, path.name)
        else:
            start, end = 1440, 0
        rows.append((doy, hm_minutes(d["sunrise"], path.name), hm_minutes(d["sunset"], path.name), start, end))
    if not rows:
        sys.exit(f"Error: {path.name} lists no days.")
    return sorted(rows)


def daylight_on(rows, clock, cal):
    """Sunrise, sunset and darkness on a given day, linearly interpolated between rows."""
    doy = cal.split(clock)[3]
    before = [r for r in rows if r[0] <= doy]
    after = [r for r in rows if r[0] > doy]
    prev = before[-1] if before else (rows[-1][0] - cal.year_len,) + rows[-1][1:]
    nxt = after[0] if after else (rows[0][0] + cal.year_len,) + rows[0][1:]
    if nxt[0] == prev[0]:
        return prev[1:]
    f = (doy - prev[0]) / (nxt[0] - prev[0])
    return tuple(round(a + (b - a) * f) for a, b in zip(prev[1:], nxt[1:]))


def fmt_min(m):
    m = int(round(m / 5) * 5) % 1440
    return f"{m // 60}:{m % 60:02d}"


def day_phase(rows, clock, cal):
    sunrise, sunset, start, end = daylight_on(rows, clock, cal)
    t = clock.hour * 60 + clock.minute
    dark = end > 0 or start < 1440
    if dark and (t >= start or t < end):
        phase = "darkness"
    elif t < sunrise:
        phase = "dawn" if dark else "white night"
    elif t < sunset:
        phase = "day"
    else:
        phase = "dusk" if dark else "white night"
    darkness = f"darkness {fmt_min(start)}–{fmt_min(end)}" if dark else "no darkness (white nights)"
    return f"Time of day: {phase} (sunrise {fmt_min(sunrise)}, sunset {fmt_min(sunset)}, {darkness})"


def cmd_time(args, folder, state):
    hm = parse_hm(args.now)
    if args.setting:
        if not (ROOT / "Settings" / args.setting).is_dir():
            sys.exit(f"Error: there is no setting folder Settings/{args.setting}.")
        state["setting"] = args.setting
    setting = state.get("setting")
    cal = load_calendar(setting)
    if args.date:
        clock = cal.parse(args.date).replace(hour=hm[0], minute=hm[1])
    else:
        clock = at_or_after(get_clock(state, cal), hm)
    state["clock"] = cal.fmt(clock)
    daylight = load_daylight(setting, cal) if setting and (ROOT / "Settings" / setting / DAYLIGHT_FILE).exists() else None

    due = sorted((e["at"], label, e) for label, e in state["events"].items()
                 if not e["reported"] and e["at"] <= state["clock"])
    about_day = cal.describe(clock)
    print(f"Clock: {state['clock']}" + (f" ({about_day})" if about_day else ""))
    if daylight:
        print(day_phase(daylight, clock, cal))
    if not due:
        print("No new events.")
    for moment, label, event in due:
        event["reported"] = True
        about = f": {event['desc']}" if event.get("desc") else ""
        print(f"Now: {label}{about} (at {moment[-5:]})")
    save_state(folder, state)


def cmd_timer(args, folder, state):
    if label_taken(state, args.label):
        sys.exit(f"Error: label '{args.label}' is already taken.")
    cal = load_calendar(state.get("setting"))
    clock = get_clock(state, cal)
    entries = table_entries(args.table, load_tables())
    if not all(isinstance(v, int) for _, _, v in entries):
        sys.exit(f"Error: table '{args.table}' does not give minutes, so it cannot be used for a timer. "
                 "A hidden roll with a text table is made by Scripts/roll.py --hidden.")
    start = nearest(clock, parse_hm(args.start)) if args.start else clock
    dice, total = roll_3d6()
    moment = start + timedelta(minutes=lookup(entries, total))
    if args.not_before:
        moment = max(moment, at_or_after(start, parse_hm(args.not_before)))
    # An event whose time has already passed happens now: it is reported by
    # the next `time`, never with a moment before the clock.
    moment = max(moment, clock)
    state["events"][args.label] = {
        "at": cal.fmt(moment),
        "desc": args.desc,
        "table": args.table,
        "from": cal.fmt(start),
        "dice": dice,
        "result": total,
        "reported": False,
    }
    save_state(folder, state)
    log_hidden(folder, args.label, f"timer, table {args.table}")
    print(f"Hidden event saved: {args.label}.")


def cmd_remove(args, folder, state):
    for kind in ("events", "rolls"):
        if args.label in state[kind]:
            del state[kind][args.label]
            save_state(folder, state)
            print(f"Removed {args.label}.")
            return
    sys.exit(f"Error: there is no label '{args.label}'.")


def cmd_show(args, folder, state):
    print(f"Clock: {state['clock'] or 'not set'}")
    events = state["events"]
    rolls = state["rolls"]
    if args.label:
        if not label_taken(state, args.label):
            sys.exit(f"Error: there is no label '{args.label}'.")
        events = {k: v for k, v in events.items() if k == args.label}
        rolls = {k: v for k, v in rolls.items() if k == args.label}
    print("Events:" if events else "Events: none")
    for label, e in sorted(events.items(), key=lambda kv: kv[1]["at"]):
        status = "happened" if e["reported"] else "pending"
        about = f" {e['desc']}" if e.get("desc") else ""
        print(f"  {label}{about}: {e['at']} ({status}; from {e['from']}, table {e['table']}, result {e['result']})")
    print("Hidden rolls:" if rolls else "Hidden rolls: none")
    for label, r in rolls.items():
        about = f" {r['desc']}" if r.get("desc") else ""
        print(f"  {label}{about}: result {r['result']}, {r['outcome']}")


def main():
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="The GM's hidden state: clock, hidden events and rolls.")
    parser.add_argument("--campaign", required=True, help="name of the campaign folder in Campaigns/")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("time", help="set the world clock and print the events that have just happened")
    p.add_argument("--now", required=True, help="time in the world, HH:MM")
    p.add_argument("--date", help="date in the world, YYYY-MM-DD (when first set or corrected)")
    p.add_argument("--setting", help="setting folder, for its Tables/Calendar.json and Tables/Daylight.json; remembered in the campaign state")

    p = sub.add_parser("timer", help="roll the hidden time of an event on a named table")
    p.add_argument("--label", required=True, help="neutral label, e.g. n1")
    p.add_argument("--table", required=True, help="name of a table from Tables/GmTables.json (values in minutes)")
    p.add_argument("--from", dest="start", help="time the countdown starts, HH:MM, the occurrence closest to the clock (default now)")
    p.add_argument("--not-before", dest="not_before", help="the event happens no earlier than HH:MM")
    p.add_argument("--desc", default="", help="short, neutral description, visible in the console")

    p = sub.add_parser("remove", help="remove a hidden event or a hidden roll")
    p.add_argument("--label", required=True)

    p = sub.add_parser("show", help="print the whole hidden state (only when resuming play)")
    p.add_argument("--label", help="only this label")

    args = parser.parse_args()
    folder = campaign_folder(args.campaign)
    state = load_state(folder)
    {"time": cmd_time, "timer": cmd_timer, "remove": cmd_remove, "show": cmd_show}[args.command](args, folder, state)


if __name__ == "__main__":
    main()
