#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 yamaguchi keigo
# SPDX-License-Identifier: GPL-3.0-or-only

import sys

def process(stream):
    for i, line in enumerate(stream, 1):
        text = line.rstrip("\n").upper()
        print(f"{i:4}\t{text}")

def main():
    if len(sys.argv) == 1:
        process(sys.stdin)
        return
    for filename in sys.argv[1:]:
        try:
            with open(filename, encoding="utf-8") as f:
                process(f)
        except FileNotFoundError:
            print(f"{sys.argv[0]}: {filename}: No such file", file=sys.stderr)

if __name__ == "__main__":
    main()
