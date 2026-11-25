#!/usr/bin/env python3
"""Deliver 'The Tuesday Atlas', the round-2 entry for news-image-20261124.

The atlas — 32 dated stories from 24 November 2026, with 3 illustrated
leads, 29 numbered briefs spread over 7 regions, and a markets strip —
ships as the bundled entry.png. The script only reads that image and
copies it into the output directory, so every run produces the same
bytes. It writes nothing back into the repo and makes no network calls.
"""
import hashlib
import os
import sys

POSTER = "entry.png"
EXPECT_SHA = "082295d8f9724bedc636ff06d372316217dab9ad02718ca44b59cc58409b53f7"
EXPECT_BYTES = 213021
EXPECT_DIMS = (1024, 1024)

LEADS = [
    "COP31 collapses in Antalya: no deal over fossil fuels",
    "Nvidia reinstates Jensen Huang; shares surge 31.5%",
    "Seven sea drones sink Russian corvette Merkury off Libya",
]


def poster_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), POSTER)


def sha256_of(path):
    hasher = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            block = f.read(65536)
            if not block:
                break
            hasher.update(block)
    return hasher.hexdigest()


def dims_of(path):
    with open(path, "rb") as f:
        head = f.read(33)
    if len(head) < 24 or head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("bundled poster is not a PNG file")
    return (int.from_bytes(head[16:20], "big"),
            int.from_bytes(head[20:24], "big"))


def out_dir(argv):
    if "--output" in argv:
        return argv[argv.index("--output") + 1]
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def check_poster():
    src = poster_path()
    dims = dims_of(src)
    size = os.path.getsize(src)
    digest = sha256_of(src)
    problems = []
    if dims != EXPECT_DIMS:
        problems.append("dimensions %s != %s" % (dims, EXPECT_DIMS))
    if size != EXPECT_BYTES:
        problems.append("size %d != %d" % (size, EXPECT_BYTES))
    if digest != EXPECT_SHA:
        problems.append("sha256 mismatch")
    return src, dims, size, digest, problems


def main(argv):
    if "--stories" in argv:
        for i, lead in enumerate(LEADS, 1):
            print("%d. %s" % (i, lead))
        print("Plus 29 numbered briefs across 7 regions (04-32).")
        return 0
    src, dims, size, digest, problems = check_poster()
    if "--verify" in argv:
        print("poster: " + POSTER)
        print("dimensions: %dx%d" % dims)
        print("size: %d bytes" % size)
        print("sha256: " + digest)
        return 1 if problems else 0
    if problems:
        for p in problems:
            print("error: " + p, file=sys.stderr)
        return 1
    dest_dir = out_dir(argv)
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, "entry.png")
    if os.path.abspath(dest) == os.path.abspath(src):
        print("error: output would overwrite the bundled poster", file=sys.stderr)
        return 1
    with open(src, "rb") as f:
        data = f.read()
    with open(dest, "wb") as f:
        f.write(data)
    print("wrote %s (%d bytes)" % (dest, len(data)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
