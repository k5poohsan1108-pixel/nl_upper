#!/bin/bash
# commit_sequence.sh
# nl_upper のコミットを順番に実行するサンプル

# 1. 初期ファイル追加
git add nl_upper/nl_upper.py nl_upper/LICENSE nl_upper/README.md
git commit -m "Add initial version of nl_upper with LICENSE and README"

# 2. 基本機能の実装
git add nl_upper/nl_upper.py
git commit -m "Add basic functionality: convert text to uppercase with line numbers"

# 3. 空行対応追加
git add nl_upper/nl_upper.py
git commit -m "Support empty lines correctly in input"

# 4. エラーハンドリング改善
git add nl_upper/nl_upper.py
git commit -m "Enhance error messages when input file is missing"

# 5. 実行権限付与
chmod +x nl_upper/nl_upper.py
git add nl_upper/nl_upper.py
git commit -m "Make nl_upper.py executable"

# 6. GitHub Actions ワークフロー追加
git add .github/workflows/test.yml
git commit -m "Set up GitHub Actions workflow for automated testing"

# 7. テスト追加
git add .github/workflows/test.yml
git commit -m "Include additional test cases for standard input and file input"

# 8. テスト比較の微修正
git add .github/workflows/test.yml
git commit -m "Adjust test comparison formatting for readability"

# 9. README 更新（テスト内容追記）
git add nl_upper/README.md
git commit -m "Update README: add test description and workflow badges"

# 10. README 文言の微調整（柔らかい表現など）
git add nl_upper/README.md
git commit -m "Refine README text for clarity and easier understanding"

