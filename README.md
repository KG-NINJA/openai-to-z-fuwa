
# Organic Intuition × Animal Instinct × AI Distillation  
## — A New Trinity in the Age of Archaeological Discovery

> *Before the era of AI, organic intuition and wild imagination were mostly tolerated only within the arts—and even there, true understanding was rare. In science, intuition without data was often dismissed as “irrational” or “unscientific.”*

Now, for the first time in history, **humans, animals, and AI can collaborate as equals** in the pursuit of discovery.  
- I follow my organic intuition—sometimes wildly, even recklessly, guided by flashes of inspiration and moments of serendipity.
- My dogs (Fuwa and Coco) embody animal instincts, stopping at places I might otherwise ignore, attuned to environmental signals beyond human senses.
- Meanwhile, the AI system quietly takes on the role of digital archivist and distiller—cataloging, organizing, and purifying each clue into structured knowledge.

Together, **mystery and order, intuition and logic**, become not rivals but true partners.

> What was once considered eccentric, delusional, or even mystical is—when combined with the power of AI—transformed into a new form of innovation and evidence.

This project is living proof that **organic chaos and digital clarity**, when joined, usher in a new epoch:
> A time where poetic intuition and algorithmic rigor *coexist and complement* each other—  
> and the boundary between art and science becomes porous for the first time in history.

---

### 日本語バージョン

# 有機的直感 × 動物的感性 × AIデータ蒸留  
## ― 歴史上はじめての“三位一体”時代へ

> *AI登場以前、“有機的な暴走”や妄想的な直感は芸術の世界でしか許されず、それすら理解者は少数派でした。科学の世界では「非合理」「非科学的」として排除されがちでした。*

今、**人間＋動物＋AI**が協力し合うことで、誰も踏み入れたことのない発見の地平へ。

- 私は、時に暴走しつつも直感と偶然を信じて道を選ぶ。
- 愛犬（ふわ・ココ）は人間には察知できない場所で立ち止まり、動物的なセンサーとなる。
- その裏でAIは、データを淡々と整然と蒸留・管理し、混沌の中から構造化された知見を生み出す。

これまでは相反すると思われてきた「神秘性と整然性」「直感と論理」は、今や両立しうるパートナー。

> かつては奇人変人扱いされた発想も、AIという補完存在が加わることで、はじめて新しい証拠と創造性の源泉となる。

このプロジェクトは、**有機的な混沌とデジタルの整然**が交わることで、芸術と科学の境界が溶け始める、人類史上初の新時代が始まった証です。

---


## 🚀 How to Auto-Generate Submission Reports Using AI

This repository provides a reproducible workflow for generating Kaggle-ready Markdown reports from satellite NDVI analyses using a template and `results.json`.

**Key steps for full or semi-automated report generation (including AI auto-filling of summaries, interpretations, etc.):**

---
## 🛠️ Development Notes & Testing

- [x] Automated download of yearly median NDVI (MODIS, 2015–2024) for the Amazon basin using Google Earth Engine (`scripts/download_ndvi_amazon.py`)
- [x] One-line install: `pip install -r requirements.txt`
- [x] Analysis pipeline reproducible via `python run_pipeline.py`
- [x] Unit test framework included (`python -m unittest discover`)
- [!] Note: Network access to pypi.org or Google Earth Engine may be restricted in some environments.

### Step-by-step AI Automation Workflow

1. **Prepare your analysis output**
   - Run your pipeline (e.g., `run_analysis.py`) to calculate key values (e.g., `max_ndvi`, `candidate_count`) and generate output files (`ndvi_chart.png`, `geojson_file`, etc.).
   - Write these values and file names to `results.json`.

2. **Auto-fill missing report sections using GPT (Codex/GPT-4o/ChatGPT etc.)**
   - For any fields in `results.json` that remain `"N/A"` (such as `abstract`, `key_findings`, `interpretation`, `conclusion`), use an LLM to auto-generate content.
   - You can use the following prompt (for OpenAI, Claude, Gemini, or similar):

<details>
<summary>Sample AI Prompt</summary>

```text
Below is a Markdown template for a Kaggle submission and a JSON object with placeholders ("N/A").
For every key in the JSON that is "N/A", generate plausible content (AI summary, findings, interpretations, conclusions, etc.).
Fill all fields, using the context and filled values where available, and return the completed JSON object only.

Markdown template:
---
# {site_name} NDVI Anomaly Detection Report
...
## Footnote
{footnote}
---

Partial JSON:
{
  "site_name": "Obidos South NDVI Analysis",
  "abstract": "N/A",
  "background": "N/A",
  "methodology": "NDVI anomaly detection was performed using Landsat 8 imagery.",
  "key_findings": "N/A",
  "ndvi_chart": "o3_ndvi_chart.png",
  "geojson_file": "o3_ndvi_candidates.geojson",
  "interpretation": "N/A",
  "conclusion": "N/A",
  "generation_date": "2025-06-11 17:11",
  "commit_hash": "a1b2c3d4",
  "max_ndvi": 0.82,
  "candidate_count": 4,
  "footnote": "N/A"
}
