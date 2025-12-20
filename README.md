# nl_upper

[![test](https://github.com/k5poohsan1108-pixel/nl_upper/actions/workflows/test.yml/badge.svg)](https://github.com/k5poohsan1108-pixel/nl_upper/actions/workflows/test.yml)

`nl_upper` は、標準入力またはファイルから読み込んだテキストに  
行番号を付与し、大文字に変換して出力するコマンドです。

---

## 特徴

- 各行に行番号を付与
- 小文字を大文字に変換
- 空行も正しくカウント
- 標準入力・ファイル入力の両方に対応

---

## 使い方

### ダウンロード

```bash
$ git clone https://github.com/k5poohsan1108-pixel/nl_upper.git
$ cd nl_upper

### 実行権限の付与

$ chmod +x nl_upper

### 標準入力から実行

$ echo -e "hello\nworld" | ./nl_upper

##出力例

   1	HELLO
   2	WORLD

## 自動テスト(GitHub Actions)

このリポジトリでは、以下のpythonバージョンで自動テストが動きます。

Ubuntu 22.04

Python 3.7 / 3.8 / 3.9 / 3.10

## 権利関係・謝辞
本ソフトウェアはGPL-3.0-or-laterで配布

# SPDX-FileCopyrightText: 2025 yamaguchi keigo

# SPDX-License-Identifier: GPL-3.0-or-later

## その他

このプログラムは小さいですが、

ライセンス表記

自動テスト

ワークフロー構築

といった、学んだことをまとめて練習できる内容になっています。
