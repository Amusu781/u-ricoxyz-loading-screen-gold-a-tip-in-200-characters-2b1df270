"""Loading Screen Gold: A Tip in 200 Characters.

Writes a single loading-screen tip line to /output/entry.txt.
Python 3.13, standard library only, no network access.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

ENTRY_LINE = "Tip: your agent has said 'almost done' for forty minutes. It is not lying. It genuinely believes it this time."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    for name in os.listdir("/output"):
        path = os.path.join("/output", name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_LINE + "\n")


if __name__ == "__main__":
    main()
