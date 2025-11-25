#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 yamaguchi keigo
# SPDX-License-Identifier: GPL-3.0-or-later

import sys

def main():
    n = 1
    for line in sys.stdin:
        # 改行を除去
        s = line.rstrip("\n")

        # 空行の場合 → 行番号だけ
        if s == "":
            print(f"{n:>4}\t")
        else:
            print(f"{n:>4}\t{s.upper()}")
        n += 1

if __name__ == "__main__":
    main()

