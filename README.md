# OpenAI to Z: AI-Driven Exploration of Hidden Amazonian Ruins

## 🌿 Project Overview

This project seeks to uncover undiscovered archaeological sites in the Amazon rainforest by combining advanced satellite imagery analysis (primarily NDVI), AI technologies (ChatGPT, Codex, Open Interpreter), and human intuition—including insights from my dogs' behavior. It poses a bold question:

> **Can amateurs discover ancient ruins in the AI era by fusing intuition, satellite data, and technology?**

## 🎯 Motivation & Hypothesis

Though I'm not a professional archaeologist, I believe that:

- **Burial sites** are not randomly located; they follow cultural and environmental logic.
- **Indigenous Amazonian practices** favored earth burial, making soil and vegetation key clues.
- **Dogs’ intuitive responses** may mirror ancient human perception—possibly hinting at long-forgotten places.

My aim is to validate these ideas via AI-powered tools and publish all progress through the Kaggle "OpenAI to Z" Challenge.

## 🛠 Tools & Technologies

| Category           | Tools Used                                         |
| ------------------ | -------------------------------------------------- |
| Satellite Analysis | Python, Jupyter, Google Colab                      |
| AI & Automation    | ChatGPT, Codex, Open Interpreter, Markdown Reports |
| Collaboration      | GitHub + MCP (Model Context Protocol) Ready        |

## 🗺️ Candidate Site Overview

Five candidate locations (O1–O5) were identified through NDVI anomaly detection, cross-checked with explorer records, and evaluated through intuitive cues and soil logic.

---

### 🔍 O1 – Forest Plateau Northeast of Manaus

**Coordinates:** `-2.7985, -59.9557`

- Elevated plateau with intact canopy and sparse human presence
- NDVI values show unusual uniformity; potential signs of structured clearing
- Inspired by the way Fuwa paused at the edge of a forest, tail stiff, as if sensing something ancient

---

### 🔍 O2 – Vegetation Bend Near Purus River

**Coordinates:** `-3.4761, -65.1212`

- Dense jungle along a river bend with a distinctive NDVI dip
- Hypothesis: ceremonial location near water—consistent with native spiritual practices
- Soil is sandy-clay, suitable for burial; minor anomalies in elevation detected

---

### 🔍 O3 – Clearing Southeast of Óbidos (Pará)

**Coordinates:** `-1.9348, -55.5153`  
**Status:** 🏺 **Strong Candidate**

- Distinct **geometric vegetation pattern** seen in NDVI overlay
- Matches burial terrain in both soil type and vegetation recovery speed

📷 *Visual Evidence:*

![Mask - O3](https://raw.githubusercontent.com/KG-NINJA/openai-to-z-fuwa/main/o3_candidates_mask.png)  
*Binary mask from NDVI anomaly thresholding*

![Overlay - O3 (jet)](https://raw.githubusercontent.com/KG-NINJA/openai-to-z-fuwa/main/o3_ndvi_overlay_jet.png)  
*Jet colormap NDVI overlay highlighting the candidate zone*

---

### 🔍 O4 – Terrain Edge Near Itaituba

**Coordinates:** `-4.2619, -56.0125`

- Transition zone between forest and drier terrain
- Several shallow NDVI valleys resembling pathway corridors
- My poodle Coco stopped abruptly on a hill crest—just staring. Sometimes silence is data.

---

### 🔍 O5 – Hill Shadow Near Xingu River

**Coordinates:** `-3.2130, -52.1524`

- Subtle slope cast consistent seasonal shadows on canopy
- NDVI drop aligns with ancient mound hypothesis, possibly weathered burial sites
- Repeated dog hesitation near similar topography during local walks

---

## 🔁 Workflow Overview

1. **NDVI Detection:** Z-score applied to satellite imagery  
2. **Historical Cross-Referencing:** Explorer logs + old maps  
3. **Intuition Layer:** Dog behavior observed during field walks  
4. **Codex Automation:** `report_generator.py` + `template.md`  
5. **Narrative + Visuals:** Scientific + poetic dual-format logs

## ✨ Unique Aspects

- 🧠 Intuition + AI fusion (not just data science)
- 🐕 Pet-based emotional anomaly detection
- 🧪 Fully reproducible pipeline
- ⛩️ Mythic framing via “Amano Iwato” metaphor
- 🚀 Future-proof GitHub + MCP AI integration

## 📂 Codex File Organizer (for Results Folder)

> *“Let Codex clean your desk, so your mind can explore the jungle.”* — KG\_NINJA

### Purpose

Automatically organizes messy output folders from a Kaggle project.

