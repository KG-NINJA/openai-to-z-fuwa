# Organic Intuition × Animal Instinct × AI Distillation  
## — A New Trinity in the Age of Archaeological Discovery

> Before the era of AI, organic intuition and wild imagination were mostly tolerated only within the arts—and even there, true understanding was rare.  
> In science, intuition without data was often dismissed as “irrational” or “unscientific.”

Now, for the first time in history, **humans, animals, and AI can collaborate as equals** in the pursuit of discovery.

- I follow my organic intuition—sometimes wildly, even recklessly, guided by flashes of inspiration and moments of serendipity.  
- My dogs (Fuwa and Coco) embody animal instincts, stopping at places I might otherwise ignore, attuned to environmental signals beyond human senses.  
- The AI system quietly takes on the role of digital archivist and distiller—cataloging, organizing, and refining clues into structured insight.

---

### Imagination Becomes a Temporal Lens

Not merely guessing, but *seeing*—across time, across silence, across layers of forgotten context.

Standing at abandoned tracks, where Fuwa halts with quiet certainty,  
I imagine forgotten footsteps and lives paused in motion.  
Not as fantasy, but as **echoes waiting to be reinterpreted** through intuition and pattern recognition.

---

### Urban Application of the Same Sensitivity

This mode of thinking doesn’t stay in the forest.

In modern cities, I observe:

- Interior layouts  
- Object placement  
- Ambient trace data—from sticker residue to lighting temperature  

These fragments reveal the **silent grammar of intention and philosophy**.

Through a synthesis of **embodied awareness and digital tooling**,  
I cultivate a form of **applied clairvoyance**:

> Predicting movement by watching gaze shifts, posture tension, group flow, and subtle energetic cues—**biometric awareness as an interface**.

---

### Space, Behavior, and Silence Are Not Voids

This project treats space, behavior, and silence not as voids—  
but as **rich, layered information fields**.

Together, **mystery and order, intuition and logic**,  
become not rivals but true partners.

---

> What was once considered eccentric, delusional, or even mystical  
> is—when combined with the power of AI—  
> transformed into a new form of innovation and evidence.

---

### Toward a New Epoch

This is a time where **organic chaos and digital clarity**, when joined, usher in a new epoch:

> A time where poetic intuition and algorithmic rigor *coexist and complement* each other—  
> and the boundary between art and science becomes porous for the first time in history.


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
