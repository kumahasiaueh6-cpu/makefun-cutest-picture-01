#!/usr/bin/env python3
"""make.fun entry (cutest-picture-01): write the bundled picture to /output/entry.png.

Deterministic by construction: a byte-identical copy of the bundled
image. No network, no randomness, no timestamps, Python stdlib only.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")

# Pinned digest of the bundled entry.png (v2: cream kitten hugging a chick,
# blue eyes, mint scarf, daisy crown). The run fails loudly if the bundled
# image is swapped or corrupted.
EXPECTED_SHA256 = "5b0bb4b5a558edfff76463ab61e22dbf6b1b684e9eb31168d8a6ca8685bb8856"


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    if not os.path.isfile(SOURCE):
        raise SystemExit("bundled entry.png not found next to main.py")
    # The bundled image must be the exact v2 entry; a swapped or corrupt
    # file fails here instead of silently submitting the wrong picture.
    if _sha256(SOURCE) != EXPECTED_SHA256:
        raise SystemExit("bundled entry.png sha256 mismatch")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    # Self-check: the output must be byte-identical to the bundled image,
    # so a partial or corrupt copy fails loudly instead of passing silently.
    if _sha256(SOURCE) != _sha256(OUTPUT):
        raise SystemExit("output does not match the bundled entry.png")


if __name__ == "__main__":
    main()
