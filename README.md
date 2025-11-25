
# nl_upper
[![test](https://github.com/k5poohsan1108-pixel/nl_upper/actions/workflows/test.yml/badge.svg)](https://github.com/k5poohsan1108-pixel/nl_upper/actions/workflows/test.yml)

行番号をつけながら、入力された文字を大文字に変換するコマンドです。標準入力もファイルもどちらも使えます。
GitHub Actions で自動テストも動くようにしてあり、Python の複数バージョンで確認しています。
できることは
・入力されたテキストを大文字に変換

・各行に 行番号を付与

・空行も正しくカウント

・標準入力・ファイル入力の両方に対応

## 使い方
標準入力から使うとき
echo -e "hello\nworld" | ./nl_upper.py
ファイルを指定してから使うとき
$./nl_upper.py mytext.txt
インストール
chmod +x nl_upper.py
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
・自動テスト(GitHub Actions)・ワークフロー構築
といった、学んだことをまとめて練習できる内容になっています。
