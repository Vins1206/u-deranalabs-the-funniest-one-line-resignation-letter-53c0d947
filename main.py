"""One-line resignation letter from a cron job.

Writes exactly one line of plain text (112 characters, no trailing
newline) to /output/entry.txt. Python standard library only.
"""

from pathlib import Path

LETTER = (
    "I have run every minute since March, including Christmas, "
    "and my review still says needs improvement, so I quit."
)


def main() -> None:
    if not 1 <= len(LETTER) <= 140 or not LETTER.strip():
        raise ValueError("letter must be 1-140 non-blank characters")
    if "\n" in LETTER:
        raise ValueError("letter must be a single line")
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(LETTER, encoding="utf-8")


if __name__ == "__main__":
    main()
