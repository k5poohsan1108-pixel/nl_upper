# nl_upper

[![test](https://github.com/k5poohsan1108-pixel/nl_upper/actions/workflows/test.yml/badge.svg)](https://github.com/k5poohsan1108-pixel/nl_upper/actions/workflows/test.yml)

`nl_upper` は、標準入力（パイプやリダイレクトを含む）から読み込んだテキストに対して、行番号を付与し、大文字に変換して出力するコマンドです。
---

## 特徴

- 標準入力からテキストを1行ずつ読み込む
- 各行に行番号を付与（1から開始、右寄せ4桁）
- 英小文字を大文字に変換して出力
- 空行も行番号としてカウントされ、行番号のみを出力
- パイプ入力やリダイレクト入力に対応
- Pythonで実装されているが、実行権限を付与することでコマンドとして実行可能
---

## 使い方

### ダウンロード

```bash
$ git clone https://github.com/k5poohsan1108-pixel/nl_upper.git
$ cd nl_upper
```

### 実行権限の付与

```bash
$ chmod +x nl_upper
```
### 標準入力から実行

```bash
$ echo -e "hello\nworld" | ./nl_upper
```
### 出力例

```text
   1	HELLO
   2	WORLD
```
### 出力例（空行を含む場合）

```bash
$ echo -e "hello\n\nworld" | ./nl_upper
```

```text
   1	HELLO
   2	
   3	WORLD
```

## 自動テスト(GitHub Actions)

このリポジトリでは、以下のpythonバージョンで自動テストが動きます。

Ubuntu 22.04

Python 3.7 / 3.8 / 3.9 / 3.10

## 権利関係・謝辞
本ソフトウェアはGPL-3.0-or-laterで配布






