#!/usr/bin/env python3
# Convert input text to uppercase with line numbers
# SPDX-FileCopyrightText: 2025 yamaguchi keigo
# SPDX-License-Identifier: GPL-3.0-or-later

import sys

def main():
    n = 1
    for line in sys.stdin:
        s = line.rstrip("\n")
        print(f"{n:>4}\t{s.upper()}" if s else f"{n:>4}\t")
        n += 1

if __name__ == "__main__":
    main()
