"""Toponym clue extraction using Overpass API."""

from __future__ import annotations

import logging
from typing import List, Dict

from geopy.distance import geodesic
import overpy

logging.basicConfig(level=logging.INFO)

KEYWORDS = [
    "teso", "cemitério", "morada", "monte", "dos mortos", "altar",
    "ilha", "cacique", "encantado", "antigo"
]


def extract_toponym_clues(lat: float, lon: float, radius: int = 10000) -> List[Dict]:
    """Return a list of toponym clues near the provided coordinates."""
    api = overpy.Overpass()
    query = f"""
    (
      node["name"](around:{radius},{lat},{lon});
    );
    out center;
    """
    try:
        logging.info("Querying Overpass API for toponyms near (%s, %s)", lat, lon)
        result = api.query(query)
        matches: List[Dict] = []
        for node in result.nodes:
            name = node.tags.get("name", "")
            lower = name.lower()
            found = [kw for kw in KEYWORDS if kw in lower]
            if found:
                dist = geodesic((lat, lon), (node.lat, node.lon)).km
                matches.append({
                    "name": name,
                    "coordinates": [node.lat, node.lon],
                    "matched_keywords": found,
                    "distance_km": round(dist, 2)
                })
        logging.info("Found %d toponym clues", len(matches))
        return matches
    except Exception as exc:  # Overpass may fail or be offline
        logging.error("Toponym extraction failed: %s", exc)
        return []
