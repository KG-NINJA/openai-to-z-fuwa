"""Site analysis utilities."""

from __future__ import annotations

import logging
from typing import Dict, Tuple

import numpy as np
from scipy import ndimage
from skimage import measure

logging.basicConfig(level=logging.INFO)


def compute_anomalies(data: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
    """Compute Z-score anomalies for NDVI and derive candidate mask."""
    ndvi = data["ndvi"]
    mean = float(ndvi.mean())
    std = float(ndvi.std())
    z = (ndvi - mean) / (std if std else 1)
    mask = z > 2.0
    logging.info("NDVI mean %.3f std %.3f -> %d anomalies", mean, std, mask.sum())
    return {"zscore": z, "candidate_mask": mask}


def cluster_candidates(mask: np.ndarray) -> np.ndarray:
    """Return labeled clusters for candidate mask."""
    labeled, num = ndimage.label(mask)
    logging.info("Identified %d candidate clusters", num)
    return labeled


def summarize_clusters(labels: np.ndarray) -> Dict[str, int]:
    """Return count and largest cluster size."""
    props = measure.regionprops(labels)
    sizes = [p.area for p in props]
    return {"cluster_count": len(sizes), "max_cluster_size": max(sizes) if sizes else 0}
