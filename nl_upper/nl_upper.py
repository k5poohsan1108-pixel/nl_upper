#!/usr/bin/env python3
# Convert input text to uppercase with line numbers
# SPDX-FileCopyrightText:  2025 yamaguchi keigo
# SPDX-License-Identifier: GPL-3.0-or-later
import sys

def main():
    # ファイルが指定されていればファイルを読み込む
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        lines = sys.stdin.readlines()

    n = 1
    for line in lines:
        s = line.rstrip("\n")
        # 空行でも行番号だけ出力
        if s == "":
            print(f"{n:>4}\t")
        else:
            print(f"{n:>4}\t{s.upper()}")
        n += 1

if __name__ == "__main__":
    main()
