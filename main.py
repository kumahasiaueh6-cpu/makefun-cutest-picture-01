#!/usr/bin/env python3
"""make.fun entry (cutest-picture-01): write the bundled picture to /output/entry.png.

Deterministic by construction: a byte-identical copy of the bundled
image. No network, no randomness, no timestamps, Python stdlib only.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)


if __name__ == "__main__":
    main()
