# nl_upper

[![test](https://github.com/k5poohsan1108-pixel/nl_upper/actions/workflows/test.yml/badge.svg)](https://github.com/k5poohsan1108-pixel/nl_upper/actions/workflows/test.yml)

標準入力から読み込んだテキストを、大文字に変換して行番号付きで出力するコマンド。

---

## 使い方
```bash
$ echo -e "hello\n\nworld" | ./nl_upper
   1	HELLO
   2	
   3	WORLD
```
## 動作
- 標準入力を1行ずつ処理
- 行番号は1から開始し、右寄せ4桁
- 英小文字は英大文字に変換
- 空行も行番号として扱う

## インストール
```bash
$ git clone https://github.com/k5poohsan1108-pixel/nl_upper.git
$ cd nl_upper
$ chmod +x nl_upper
```
## ライセンス








