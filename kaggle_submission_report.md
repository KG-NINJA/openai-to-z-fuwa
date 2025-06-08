
# Kaggle Submission Report: NDVI Anomaly Detection

This report provides an overview of the methods and findings from our NDVI anomaly detection project, part of the "OpenAI to Z Challenge."

## Included Sites
We analyzed NDVI time-series data and computed Z-scores for 5 candidate sites:

- **O1**
- **O2**
- **O3** (accidentally rediscovered via typo!)
- **O4**
- **O5**

## Methodology Summary

```python
# NDVI Z-score calculation pseudocode
ndvi_stack = load_ndvi_time_series()
mean = ndvi_stack.mean(axis=0)
std = ndvi_stack.std(axis=0)
zscore = (ndvi_stack[-1] - mean) / std
anomaly_mask = zscore > 1.5
```

- NDVI computed from Landsat 8 imagery (via Google Earth Engine)
- Z-score threshold: **1.5**
- Anomalies converted to polygons and exported as GeoJSON
- Visuals rendered with matplotlib and rasterio

## Discovery Highlight: O3
A "typo" while processing the sites led to a significant re-analysis of Site O3, resulting in a breakthrough discovery.

## Output Files
Included in each results directory:
- `*_ndvi_zscore.png`: Heatmap of NDVI anomalies
- `*_anomaly.geojson`: Polygon features above threshold
- `*_report.md`: Markdown-formatted analysis
- `ndvi_summary.csv`: Overall statistics

## Author
**KG_NINJA_JAPAN**

Find more details and access the code repository [here](https://github.com/KG-NINJA/openai-to-z-fuwa/tree/main/checkpoint).

