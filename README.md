# openai-to-z-fuwa
# 🌳 From Forest to Forensics: Detecting Unnatural Vegetation with AI

> Powered by GPT-4, fueled by curiosity — and guided by a very fluffy Shiba Inu named Fuwa 🐕

## 📌 Overview

This repository contains code, maps, and visual evidence from my submission to the OpenAI to Z Challenge.  
We analyzed satellite imagery (NDVI & RGB), GEDI LiDAR data, and deforestation polygons to locate five regions in Brazil showing **visually unnatural vegetation patterns**.

- Tools: Google Earth Engine, Python, GPT-4
- Data: GEDI (NASA), TerraBrasilis (INPE)
- Theme: Human land impact detection using AI + remote sensing
- Method: NDVI + RGB + polygon overlays + GPT-driven anomaly reasoning

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

- `amazon_ndvi_2023_c2.tif`: Raw NDVI image collected over the Amazon basin.
- `amazon_ndvi_2023_c2_masked.tif`: NDVI with cloud masking applied; used for anomaly detection.

This project supports submission to Checkpoint #2 of the [OpenAI to Z Challenge](https://www.kaggle.com/competitions/openai-to-z-challenge/overview).

