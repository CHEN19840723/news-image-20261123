#!/usr/bin/env python3
"""Place the 23 November 2026 front page where the harness looks for it.

The picture is drawn ahead of time by render.py and kept in this
repository as entry.png. This runner only copies that file to the
harness output directory and proves the copy is exact, byte for byte.
It refuses to run when the picture is absent, when it is larger than
the one-mebibyte gate, or when the copy and the original disagree.
"""

from __future__ import annotations

from hashlib import sha256
from os import environ
from pathlib import Path

PICTURE = "entry.png"
CEILING = 1_048_576
CHUNK = 1 << 16


def fingerprint(path: Path) -> str:
    """Hex digest of a file, streamed so big files stay cheap."""
    summer = sha256()
    with path.open("rb") as stream:
        while (block := stream.read(CHUNK)):
            summer.update(block)
    return summer.hexdigest()


def run() -> int:
    """Copy entry.png to the output directory and verify the copy."""
    here = Path(__file__).resolve().parent
    original = here / PICTURE
    if not original.is_file():
        print(f"missing picture: {original}")
        return 1
    if original.stat().st_size > CEILING:
        print(f"picture over the 1 MiB gate: {original}")
        return 1
    out_dir = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / PICTURE
    target.write_bytes(original.read_bytes())
    if fingerprint(original) != fingerprint(target):
        print("copy differs from the original")
        return 1
    print(f"wrote {target} {fingerprint(target)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
