#!/usr/bin/env python3
"""Check that a response file contains only printable 7-bit ASCII, tab, and newline.

Usage: python3 check_ascii.py <file> [<file> ...]
Prints PASS/FAIL per file with offending characters if any.
"""
import sys

for path in sys.argv[1:]:
    try:
        data = open(path, encoding="utf-8").read()
    except OSError as e:
        print(f"{path}: ERROR {e}")
        continue
    bad = {}
    for i, ch in enumerate(data):
        if ch in ("\n", "\t"):
            continue
        if 32 <= ord(ch) <= 126:
            continue
        bad.setdefault(repr(ch), []).append(i)
    if bad:
        detail = ", ".join(f"{ch} x{len(pos)} (first at {pos[0]})" for ch, pos in bad.items())
        print(f"{path}: FAIL {detail}")
    else:
        print(f"{path}: PASS ({len(data)} chars, all ASCII)")
