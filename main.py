"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip (a single line, at most 200 characters)
to /output/entry.txt. Deterministic: no input, no network, no randomness,
no time dependence -- the same bytes on every run.

Entry for make.fun competition
u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.
"""

import os

TIP = "Tip: name your variables like the next person reading them is an AI with no context. It is."

OUTPUT_PATH = "/output/entry.txt"


def write_tip(path: str = OUTPUT_PATH) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TIP)


def main() -> None:
    write_tip()


if __name__ == "__main__":
    main()
