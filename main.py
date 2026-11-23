#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261123.

Copies the pre-rendered front page (entry.png, in this repository) to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR when set) and verifies the copy
is byte-identical by comparing sha256 hashes. Standard library only.
"""
import hashlib
import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not os.path.isfile(SOURCE):
        print(f"FATAL: missing source image: {SOURCE}", file=sys.stderr)
        sys.exit(1)
    if os.path.getsize(SOURCE) > 1048576:
        print("FATAL: source image exceeds the 1 MiB gate", file=sys.stderr)
        sys.exit(1)
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    src_hash = sha256_of(SOURCE)
    dst_hash = sha256_of(dest)
    if src_hash != dst_hash:
        print(f"FATAL: copy mismatch: {src_hash} != {dst_hash}",
              file=sys.stderr)
        sys.exit(1)
    print(f"Wrote {dest} sha256={dst_hash}")


if __name__ == "__main__":
    main()
