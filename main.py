#!/usr/bin/env python3
"""Entry for make.fun: "The GPS Swears It Was a Shortcut".

Writes the GPS's one-line excuse for sending the driver down the wrong
road to /output/entry.txt.

The line is written in the GPS's own voice: smug, defensive, and blaming
the map. It carries a fresh, specific detail (a wedding, and cake) instead
of the usual "recalculating" joke, and its turn is that the GPS itself was
promised cake -- it keeps its promises, unlike the map.
"""

ENTRY_TEXT = (
    "I rerouted you through the wedding because the map promised me cake "
    "-- and unlike the map, I keep my promises."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_single_line(text: str) -> None:
    """The entry must be exactly one line of plain text.

    No embedded newlines or carriage returns, no leading/trailing
    blank lines, and no trailing spaces after the final period --
    the kit reads the file as one line and a stray newline would
    make it look like a second, empty line.
    """
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line (no newline)")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing spaces")
    if text.endswith(" "):
        raise ValueError("entry must not end with a space")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def validate_gps_voice(text: str) -> None:
    """The excuse must sound like the GPS itself talking.

    First person ("I"), defensive, blaming the map -- never a
    narrator describing the GPS, never a dialogue tag like
    'GPS:' or a quoted line. The turn (the GPS was promised
    cake) has to be in the GPS's own words, not reported speech.
    """
    lowered = text.lower()
    if not lowered.startswith("i "):
        raise ValueError("entry should be in the GPS's first-person voice")
    if "map" not in lowered:
        raise ValueError("entry should blame the map, in the GPS's voice")
    if text.startswith(("GPS:", "GPS says", '"')):
        raise ValueError("entry must not carry a dialogue tag or quotes")
    if "recalculating" in lowered:
        raise ValueError("entry must not reuse the tired recalculating joke")


def validate_fresh_detail(text: str) -> None:
    """The excuse needs one fresh, specific detail, not a cliche.

    The brief asks for a specific, surprising detail (here: a
    wedding, and cake) instead of the generic "wrong turn" joke.
    Require at least one concrete noun from the entry's own
    premise, and forbid the stock phrases every GPS joke reuses.
    """
    lowered = text.lower()
    concrete = ("wedding", "cake", "detour", "shortcut", "traffic")
    if not any(word in lowered for word in concrete):
        raise ValueError("entry needs one fresh, specific detail")
    banned = ("wrong turn", "u-turn", "signal lost", "satellite")
    if any(phrase in lowered for phrase in banned):
        raise ValueError("entry must not reuse a stock GPS cliche")


def validate(text: str) -> None:
    """Check the kit's gates for the entry text.

    Gate: UTF-8 text of 1 to 200 characters, not only white space.
    Entry: a single line of plain text -- no newline, no setup,
    no dialogue tags, just the excuse itself.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    text.encode("utf-8")  # raises if not valid UTF-8-encodable text
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if not 1 <= len(text) <= 200:
        raise ValueError(
            f"entry must be 1-200 characters, got {len(text)}"
        )
    # Stage checks, one helper per concern: line shape, voice, detail.
    validate_single_line(text)
    validate_gps_voice(text)
    validate_fresh_detail(text)


def main() -> None:
    validate(ENTRY_TEXT)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT + "\n")
    print(f"Wrote {len(ENTRY_TEXT)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
