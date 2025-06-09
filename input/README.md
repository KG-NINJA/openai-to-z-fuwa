# openai-to-z-fuwa
## Abstract – OpenAI to Z Challenge Submission by KG-NINJA

Guided by the silent discipline of a modern-day ninja, this research merges satellite NDVI analysis, ancient expedition texts, and geometric signal mapping to reveal unseen traces of Amazonian history. Like tracking a footprint in the mist, our primary candidate near Óbidos (-1.9348, -55.5153) emerged through vegetation anomalies and precise GeoJSON zoning. Drawing on the harmony between AI and nature, we used Google Earth Engine to detect subtle breaks in green density—clues to forgotten civilizations. Historical maps and native oral traditions acted as our scrolls, aligning with the shadows on the land. This method, tested across O1–O5 sites, is quiet but sharp—repeatable, scalable, and always respectful of the forest’s secrets. Every insight, like a thrown shuriken, is precise and intentional. The project is documented in full on GitHub, echoing the principle of open learning and collective skill. Our goal is not conquest but connection—to let AI serve as a silent ally in uncovering lost knowledge. In the shadows of data, we listen.


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
