"""Cutest-cat entry for make.fun (cutest-cat-01).

Copies the kitten picture held in this repository to the grader's
output path. The program is deterministic: it writes the same bytes
on every run, uses no network, and needs nothing but the standard
library.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "cat.jpg"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT = OUTPUT_DIR / "entry.png"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    if OUTPUT.stat().st_size != SOURCE.stat().st_size:
        raise RuntimeError("output does not match the source image")


if __name__ == "__main__":
    main()
