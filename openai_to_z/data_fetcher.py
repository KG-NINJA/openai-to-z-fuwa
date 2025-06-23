"""Data fetching utilities for the OpenAI to Z pipeline."""

from __future__ import annotations

import logging
from typing import Dict, Tuple

import numpy as np

# In a real pipeline these would pull from Google Earth Engine.
# Here we simulate data for offline testing.

logging.basicConfig(level=logging.INFO)


def fetch_site_data(lat: float, lon: float) -> Dict[str, np.ndarray]:
    """Return mock NDVI, soil, DEM, and river distance arrays for a site."""
    logging.info("Fetching data for (%.4f, %.4f)", lat, lon)
    rng = np.random.default_rng(seed=int((lat + lon) * 1000) & 0xFFFF)
    ndvi = rng.random((100, 100))
    soil = rng.random((100, 100))
    dem = rng.random((100, 100)) * 200
    river = rng.random((100, 100)) * 5
    return {"ndvi": ndvi, "soil": soil, "dem": dem, "river_dist": river}
