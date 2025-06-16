# 🗂 Codex-Powered File Organizer for Kaggle Projects

> “Let Codex clean your desk, so your mind can explore the jungle.”  
> — KG_NINJA

## 🔍 Overview

Managing a multi-modal Kaggle project like **OpenAI to Z** means handling messy directories:

- 🛰 Satellite images (NDVI, RGB)
- 📊 Analytical results (GeoTIFF, CSV, PNG)
- 🧠 AI-generated reports (Markdown, PDF)
- 🧪 Code & scripts (Python, CLI)

To maintain clarity, I used **OpenAI Codex** to create an intelligent file organizer that:

- 📦 Sorts by semantic file type
- 📝 Renames files with readable conventions
- 📂 Moves them into logical subfolders
- 🧠 Requires no manual drag-and-drop

---

## ⚙️ Prerequisites

| Requirement | Description |
|------------|-------------|
| 🧠 Codex access | ChatGPT Pro, Copilot Workspace, or API |
| 🐍 Python ≥ 3.10 | Local runtime for execution |
| 📁 `/results/` folder | Where raw outputs are dumped |

Example starting structure:
results/
├── o3_ndvi_zscore.png
├── o3_ndvi_candidates.geojson
├── obidos_zscore_stats.csv
├── ndvi_stack_raw.tif
├── report.md

python
コピーする
編集する

---

## ✨ Codex Prompt

```python
"""
Organize files in /results/ folder.
Rules:
- *.png → visuals/
- *.geojson → maps/
- *.csv → metrics/
- *.md → reports/
- *.tif → raw_data/
Also, rename any file starting with 'o3_' → 'ObidosSouth_'
"""
Codex auto-generates the following script:

python
コピーする
編集する
import os, shutil

file_map = {
    '.png': 'visuals',
    '.geojson': 'maps',
    '.csv': 'metrics',
    '.md': 'reports',
    '.tif': 'raw_data'
}

root = 'results'
for fname in os.listdir(root):
    ext = os.path.splitext(fname)[1]
    if ext in file_map:
        new_dir = os.path.join(root, file_map[ext])
        os.makedirs(new_dir, exist_ok=True)
        new_name = fname.replace('o3_', 'ObidosSouth_')
        shutil.move(os.path.join(root, fname), os.path.join(new_dir, new_name))
✅ Output Structure
After running the Codex-generated script:

コピーする
編集する
results/
├── visuals/
│   └── ObidosSouth_ndvi_zscore.png
├── maps/
│   └── ObidosSouth_ndvi_candidates.geojson
├── metrics/
│   └── ObidosSouth_zscore_stats.csv
├── reports/
│   └── ObidosSouth_report.md
├── raw_data/
│   └── ObidosSouth_ndvi_stack_raw.tif
🧪 Bonus Codex Tasks
You can prompt Codex to do even more:

"Summarize all CSVs into one table."

"Generate README.md describing each result."

"Find orphaned files not referenced in reports."

Let Codex automate the boring parts — so you can focus on uncovering lost cities. 🏛

🤖 Why Use Codex?
Benefit	Description
🔍 Clarity	Know exactly where every file lives
📜 Structure	Supports reproducibility and clean commits
⛩ Harmony	Intuition + automation = creative flow
🛠 Automation	Avoid grunt work, think big

🔗 Resources
GitHub repo: openai-to-z-fuwa

Challenge: OpenAI to Z - Kaggle

Author: @KG_NINJA_JAPAN

🙏 Epilogue
Even in chaotic data jungles, order is possible—with a little help from Codex and some ninja intuition.

#KGNINJA #OpenAItoZ #ArchaeologyAI #Codex
