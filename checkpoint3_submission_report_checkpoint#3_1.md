---
title: "Checkpoint #3 Submission - NDVI Z-score Analysis for O1 to O5"
date: 2025-05-29
author: "KG_NINJA_JAPAN"
---

## 🌿 NDVI Anomaly Detection for Hidden Archaeological Sites (O1–O5)

This submission contains the results of our third checkpoint investigation focusing on the Amazon region. We applied **Z-score-based anomaly detection** on NDVI satellite data across five candidate locations (O1 to O5) using Earth observation techniques and Python scripting.

Each subdirectory in the attached bundle includes:
- 📊 **NDVI Z-score visualization (PNG)**
- 🗺️ **Anomaly polygons above threshold in GeoJSON**
- 📝 **Markdown-based summary reports**
- 🧾 **CSV summary of Z-score statistics**

---

## 🧭 What Sparked This Investigation?

The story behind this checkpoint is as serendipitous as it is symbolic.

On this particular day, I intended to ask GPT to **re-analyze a location labeled `o3`**, a lowercase identifier in our tracking system. However, due to a minor typo — I accidentally wrote it in uppercase as `O3`.

This small error triggered GPT to search again with renewed attention... and surprisingly, it **led to deeper discoveries** in the region known as Óbidos.

Rather than a mistake, it turned out to be a **ninja-like sixth sense**, an intuitive decision that unearthed new insights. I call this "**Ninja Instinct**" — the kind of signal that AI and humans uncover together when logic and intuition align.

---

## 📂 Attached ZIP Contents

- `checkpoint_O1/` to `checkpoint_O5/`:
  - `*_ndvi_zscore.png`: NDVI Z-score map
  - `*_anomaly.geojson`: Detected high-Z-score polygons
  - `*_report.md`: Plain Markdown report
- `ndvi_summary.csv`: Full stats table

---

## 🔍 Method Overview

Z-score was calculated per pixel across NDVI time series. Regions where **Z > 1.5** were extracted and spatially encoded as polygons. Each anomaly represents statistically significant greenness deviations, which could point to:
- soil disruption
- buried structures
- or microclimate boundaries hinting at human-altered landscapes

---

## 🧠 Conclusion

Sometimes, errors guide us.  
Sometimes, instinct wins over planning.  
This submission is a tribute to that — where human intuition and AI analysis converged through a fortunate typo.

We hope you enjoy exploring our "O3 revelation".

— KG_NINJA_JAPAN  test
