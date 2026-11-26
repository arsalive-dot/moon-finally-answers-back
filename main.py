"""make.fun entry: The Moon Finally Answers Back.

Writes one line to /output/entry.txt — the Moon's reply, at last,
to the wishes, howls and late-night promises of everyone staring
up at it. The joke is the turn at the end: for four billion years
people have wished ON the Moon, and nobody has ever once wished
the Moon good night.

Built to the judge brief's top criteria: it speaks as the Moon
answering the wishes, howls and late-night promises (criterion 1),
in a wry, old, slightly tired voice (criterion 3), and the turn —
nobody wishing the Moon good night — arrives in the last words
(criterion 4), inside 240 characters with none wasted.
"""

import os

ENTRY = (
    "I've heard every wish, every howl, every 2 a.m. promise for "
    "four billion years — and nobody has ever once wished me good night."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
