"""Daylight table generator for the Generia setting.

An author's tool, not for play. Writes Settings/Generia/Tables/Daylight.json.

Usage:
    python Settings/Generia/Tools/make_daylight.py

Generia's year has 360 days: 12 months of 30 days, three to each season
(see Tables/Calendar.json). The year starts on the spring equinox, so the
seasons start on the equinoxes and solstices: 1 Tiriwen, 1 Saelis,
1 Calaris and 1 Ysmara. The table is computed for latitude 47° N,
the heart of Valdren around Kingsbridge, in local solar time (noon at 12:00).
Darkness starts when the sun sinks 6° below the horizon (the end of civil
twilight) and ends when it rises back there.
"""

import json
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "Tables" / "Daylight.json"
LATITUDE = 47.0
DARK_ALTITUDE = -6.0
SUN_ALTITUDE = -0.833      # sunrise and sunset, with refraction and the sun's disc
MONTHS = 12
MONTH_DAYS = 30
YEAR = MONTHS * MONTH_DAYS  # 360
EQUINOX_DOY = 1             # 1 Tiriwen, the spring equinox


def declination(doy):
    """The sun's declination in degrees, with the spring equinox on EQUINOX_DOY."""
    angle = 2 * math.pi * (doy - EQUINOX_DOY) / YEAR
    return 23.44 * math.sin(angle)


def hour_angle(altitude, decl):
    """Half the time the sun spends above an altitude, in hours, or None if it never sinks below it."""
    lat, dec, alt = (math.radians(x) for x in (LATITUDE, decl, altitude))
    cos_h = (math.sin(alt) - math.sin(lat) * math.sin(dec)) / (math.cos(lat) * math.cos(dec))
    if cos_h < -1:
        return None
    return math.degrees(math.acos(min(1.0, cos_h))) / 15


def hm(hours):
    minutes = int(round(hours * 60 / 5) * 5) % 1440
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


def row(doy):
    decl = declination(doy)
    day = hour_angle(SUN_ALTITUDE, decl)
    entry = {"sunrise": hm(12 - day), "sunset": hm(12 + day)}
    light = hour_angle(DARK_ALTITUDE, decl)
    if light is not None:
        entry["darkness"] = f"{hm(12 + light)}-{hm(12 - light)}"
    return entry


def main():
    days = {}
    for month in range(1, MONTHS + 1):
        for day in (1, 11, 21):
            days[f"{month:02d}-{day:02d}"] = row((month - 1) * MONTH_DAYS + day)
    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="\n") as fh:
        fh.write('{\n  "days": {\n')
        fh.write(",\n".join(f'    "{key}": {json.dumps(value)}' for key, value in days.items()))
        fh.write("\n  }\n}\n")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
