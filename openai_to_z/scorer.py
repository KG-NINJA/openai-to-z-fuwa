"""Score candidate sites."""

from __future__ import annotations

import logging
from typing import Dict

logging.basicConfig(level=logging.INFO)


def compute_tap_score(summary: Dict[str, int]) -> float:
    """Return a tentative archaeological potential score."""
    clusters = summary.get("cluster_count", 0)
    size = summary.get("max_cluster_size", 0)
    score = clusters * 0.6 + (size / 50.0) * 0.4
    logging.info("TAP score %.2f from %d clusters and size %d", score, clusters, size)
    return round(score, 2)
