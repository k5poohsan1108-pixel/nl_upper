#!/usr/bin/env python3
# Convert input text to uppercase with line numbers
# SPDX-FileCopyrightText: 2025 yamaguchi keigo
# SPDX-License-Identifier: GPL-3.0-or-later

import sys

def main():
    n = 1
    for line in sys.stdin:
        s = line.rstrip("\n")
        # 空行も含めて行番号を付与し大文字変換
        print(f"    {n}\t{s.upper()}")
        n += 1

if __name__ == "__main__":
    main()
