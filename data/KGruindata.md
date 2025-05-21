# Hidden Geometry in the Jungle: Using GEDI + GPT to Trace Unnatural Forest Patterns

## 🧭 Project Summary

This project combines satellite data and AI reasoning to uncover **geometrically unnatural vegetation patterns** in the Amazon and Cerrado regions of Brazil.  
Using **NASA’s GEDI LiDAR** and **IBAMA’s TerraBrasilis deforestation polygons**, I collaborated with GPT-4 to identify five regions where human activity has altered vegetation in ways that are both **legally significant and visually distinct**.

The analysis was driven by a simple intuition: _if nature draws with randomness, then straight lines, sharp corners, and perfect circles are likely signatures of us_.

---

## 🛰️ Tools and Data Sources

- **GEDI LIDAR** (NASA)
- **TerraBrasilis Deforestation Polygons** (INPE)
- **Google Earth Engine**
- **NDVI (Normalized Difference Vegetation Index)** imagery
- **RGB Composite Visualization**
- **OpenAI GPT-4** for interpretation, anomaly detection, scripting

---

## 🔍 Methodology

1. Filtered and visualized **NDVI + RGB** satellite composites using Google Earth Engine.
2. Overlaid **deforestation polygons** and **GEDI elevation profiles** to locate unnatural flat clearings.
3. Used GPT-4 to help interpret anomalies, refine the spatial logic, and generate explanations.
4. Identified five key regions that show abnormal vegetation signatures near water margins — legally protected zones.

---

## 📌 Key Locations Identified

| Location | Coordinates | Pattern |
|---------|-------------|---------|
| Ji-Paraná, RO | ~10.9°S, 61.9°W | Fishbone roads & rectangular clearings |
| São Félix do Xingu, PA | ~6.6°S, 52.0°W | Aggressive inland clearing along river |
| Santarém, PA | ~3.0°S, 55.0°W | Grid-like agriculture near Tapajós |
| Sinop, MT | ~11.8°S, 55.5°W | Checkerboard farms in flat terrain |
| Correntina, BA | ~13.3°S, 44.6°W | Circular irrigation in Cerrado savanna |

---

## 🤖 How GPT Helped

GPT-4 was not just a code-writing assistant — it **interpreted patterns**, generated hypotheses, and even offered metaphors (e.g. “arcade gem collectors” as GPU power misuse) that sparked further investigation.  
It helped overlay data, spot outliers, and question assumptions I would have missed.

---

## 🌱 Why This Matters

These patterns aren't just artifacts — they are **evidence of land use, legal circumvention, and ecological stress**.  
With AI, we can **democratize satellite intelligence** and help more people see what’s hidden in plain sight.

---

## 🧪 What’s Next

I’m turning this workflow into a **desktop-ready NDVI anomaly monitor** using Python & Earth Engine API.  
If you're interested in uncovering stories hidden in forest data, **follow this project or buy me a coffee** ☕.

---
All spatial analysis is based on `amazon_ndvi_2023_c2_masked.tif`, which filters out clouds and invalid pixels to enhance the clarity of detected anomalies.  
For reproducibility, both raw and masked NDVI data are provided in the `data/` folder.


*Author: KG, Osaka 🇯🇵*  
*Tools used: GPT-4, Earth Engine, GEDI, TerraBrasilis, Folium, Python, Colab*

> _Curiosity, caffeine, and code — this is what let me see the scars beneath the green._
