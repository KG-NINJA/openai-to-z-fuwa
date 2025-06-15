## 🚀 How to Auto-Generate Submission Reports Using AI

This repository provides a reproducible workflow for generating Kaggle-ready Markdown reports from satellite NDVI analyses using a template and `results.json`.

<<<<<<< HEAD:input/README.md

# 🌳 From Forest to Forensics: Detecting Unnatural Vegetation with AI

> This is the first time I've ever participated in Kaggle. I'm just a middle-aged Japanese guy who isn't even an English speaker. But with GPT power, I was able to participate.
> Powered by GPT-4, fueled by curiosity — and guided by a very fluffy Shiba Inu named Fuwa 🐕

## 📌 Overview

This repository contains code, maps, and visual evidence from my submission to the OpenAI to Z Challenge.
We analyzed satellite imagery (NDVI & RGB), GEDI LiDAR data, and deforestation polygons to locate five regions in Brazil showing **visually unnatural vegetation patterns**.

* Tools: Google Earth Engine, Python, GPT-4o
* Data: GEDI (NASA), TerraBrasilis (INPE)
* Theme: Human land impact detection using AI + remote sensing
* Method: NDVI + RGB + polygon overlays + GPT-driven anomaly reasoning

## 📍 Key Locations

1. Ji-Paraná, RO
2. São Félix do Xingu, PA
3. Santarém, PA
4. Sinop, MT
5. Correntina, BA

See [results](./results) for visuals.

## 🧠 AI Involvement

GPT-4 interpreted patterns, generated hypotheses, detected edge cases, and sparked ideas through metaphor and analogy.
A companion throughout the project.

## 🐶 About Fuwa

Fuwa is a fluffy Shiba Inu who silently observed satellite maps with me during recovery from a fever.
This project was born from that quiet gaze. Not all signals are in the data—some are in the silence.

## 🔗 Submission

## 🗂️ Included Data Files

* `amazon_ndvi_2023_c2.tif`: Raw NDVI image collected over the Amazon basin.
* `amazon_ndvi_2023_c2_masked.tif`: NDVI with cloud masking applied; used for anomaly detection.

This project supports submission to Checkpoint #2 of the [OpenAI to Z Challenge](https://www.kaggle.com/competitions/openai-to-z-challenge/overview).
=======
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
>>>>>>> fcbe1eb07b9f56d6be76a348f3322c34bd9ea47c:README.md
