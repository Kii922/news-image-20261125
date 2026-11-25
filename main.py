"""World News - 25 November 2026 (make.fun news-image-20261125 entry).

Copies the pre-rendered front page, entry.png, byte-for-byte to the
output directory. Python 3.13 standard library only; no network, no
clock, no files outside this repository, so repeated runs write
identical bytes.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def output_dir():
    """Resolve the output directory from the environment, default /output."""
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return out


def main():
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    dst = os.path.join(out, "entry.png")
    shutil.copyfile(SRC, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
