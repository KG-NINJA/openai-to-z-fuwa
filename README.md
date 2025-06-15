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
   - Write these values and file names to `outputs/results.json`.

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

3. **Generate the final report**
   - Run `python scripts/report_generator.py` to create `generated_report.md` and a PDF (if pandoc is installed).
