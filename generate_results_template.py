import re
import json
import os

TEMPLATE_PATH = "template.md"
OUTPUT_JSON = os.path.join("output", "results.json")

def extract_placeholders(template_path):
    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()
    # {placeholder} の形をすべて抽出（重複も拾うのでsetで一意化）
    placeholders = set(re.findall(r"{([\w\-]+)}", content))
    return sorted(placeholders)

def generate_default_json(placeholders):
    # すべて "N/A" で埋める
    return {k: "N/A" for k in placeholders}

def main():
    if not os.path.exists(TEMPLATE_PATH):
        print(f"テンプレートファイル '{TEMPLATE_PATH}' が見つかりません。")
        return
    placeholders = extract_placeholders(TEMPLATE_PATH)
    if not placeholders:
        print("テンプレートに {placeholder} が見つかりませんでした。")
        return
    default_json = generate_default_json(placeholders)
    os.makedirs("output", exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(default_json, f, indent=2, ensure_ascii=False)
    print(f"{len(placeholders)} 個の項目を持つ '{OUTPUT_JSON}' を生成しました。")
    print(f"項目例: {placeholders[:3]} ...")

if __name__ == "__main__":
    main()
