
# nl_upper
[![test](https://github.com/k5poohsan1108-pixel/nl_upper/actions/workflows/test.yml/badge.svg)](https://github.com/k5poohsan1108-pixel/nl_upper/actions/workflows/test.yml)

行番号をつけながら、入力された文字を大文字に変換するコマンドです。
GitHub Actions で自動テストも動くようにしてあり、Python の複数バージョンで確認しています。
できることは

・入力されたテキストを大文字に変換

・各行に 行番号を付与

・空行も行番号をつけて正しくカウント

## 使い方

・ダウンロード

$ git clone https://github.com/k5poohsan1108-pixel/nl_upper.git

$ cd nl_upper

・インストール

$ chmod +x nl_upper.py

・起動(標準入力）

$ echo -e "hello\nworld" | ./nl_upper.py

・出力

  1   HELLO

  2   WORLD

$ echo -e "abc\n\nxyz" | ./nl_upper.py

・出力

   1   ABC
   
   2   
   
   3   XYZ

起動(標準入力）

$ ./nl_upper.py mytext.txt

mytext.txt に書かれた各行が大文字化され、行番号付きで出力されます。

## 自動テスト(GitHub Actions）
このリポジトリでは、以下の Python バージョンで自動テストが動きます：

・3.9

・3.10

・3.11

・3.12

## 動作環境
・OS: Linux, macOS, Windows (WSL 推奨)

・Python: 3.9～3.12

・必要なライブラリ: なし（標準ライブラリのみ）

## 権利関係・謝辞
・本ソフトウェアは GPL-3.0-or-later で配布

・SPDX ライセンス表記あり

# SPDX-FileCopyrightText: 2025 yamaguchi keigo

# SPDX-License-Identifier: GPL-3.0-or-later

## その他
このプログラムは小さいですが、

・Git / コミット管理

・ライセンス表記

・自動テスト(GitHub Actions)

・ワークフロー構築

といった、学んだことをまとめて練習できる内容になっています。
