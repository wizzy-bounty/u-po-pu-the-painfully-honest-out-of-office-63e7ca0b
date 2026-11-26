import os
from pathlib import Path

ENTRY = "I am out of office until Monday and will reply when I return; I'll start where a reply can still change the outcome."


def output_dir():
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main():
    destination = output_dir()
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
