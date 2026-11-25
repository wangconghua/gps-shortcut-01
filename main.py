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
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line (no newline)")
    # The GPS is the speaker: first person, blaming the map.
    if "map" not in text.lower():
        raise ValueError("entry should blame the map, in the GPS's voice")


def main() -> None:
    validate(ENTRY_TEXT)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT + "\n")
    print(f"Wrote {len(ENTRY_TEXT)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
