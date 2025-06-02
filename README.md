# openai-to-z-fuwa

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

---

## OpenAI to Z Challenge - Archaeological AI Exploration

### Checkpoint #2 & #3 Summary

This repository presents my ongoing exploration for the "OpenAI to Z Challenge". I utilized NDVI and RGB composite analysis from satellite imagery to identify vegetation anomalies that may point to undiscovered archaeological sites in the Amazon and beyond.

### 🚁 Data & Methods

* NDVI anomaly mapping using Landsat data
* Custom mask generation to identify candidate zones
* GeoJSON boundary definition for detailed zone analysis
* Markdown reports for O1–O5 locations

### 🌿 A Personal Story: How It All Began

While walking in a wide park with my Shiba Inu "Fuwa" and poodle "Coco", something unexpected happened. At a certain spot—where nothing looked unusual—Fuwa suddenly laid down and refused to move. As Shiba Inus are genetically closer to wolves, I wondered: was she sensing something I couldn’t perceive?

That moment stayed with me.
Later, while looking at maps, I noticed I too had a strange pull toward certain locations. Could it be coincidence? Intuition? I decided to trust it—and began scanning satellite maps, comparing terrain textures, and reading archaeological papers.

I even paid attention to typos and chance moments. Because in archaeological discovery, the starting point is often uncertain. Serendipity may be evidence in disguise.

### 🧪 Exploratory Insights

This repository reflects a mix of:

* Scientific analysis
* Environmental observation
* AI-assisted anomaly detection
* Human and animal intuition

### 🔗 Outputs

* `checkpoint/checkpoint#2/...`: NDVI + GeoJSON + Markdown
* `checkpoint/checkpoint#3/...`: Enhanced region targeting, refined anomaly categorization

### 🧠 Why This Matters

This project explores the possibility that **intuitive perception—whether human or canine—can work alongside AI models** to uncover meaningful patterns in geospatial data. Early-stage insights are shared to inspire and support fellow participants.

---

### #KGNINJA

> Maybe we don’t always need to know *why* something feels important—sometimes we just need to follow it.
