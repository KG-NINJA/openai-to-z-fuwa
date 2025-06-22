import os

import re
import json
import logging
import argparse

import pandas as pd
import ee
import geemap

"""Export Sentinel-2 NDVI images for a list of sites.

The input CSV must contain `site_name`, `latitude`, and `longitude` columns.
For each site, a 1 km × 1 km bounding box is generated and the 2023
Sentinel-2 SR image collection is used to compute a median NDVI image.
Each result is exported as a PNG.
"""

logging.basicConfig(level=logging.INFO, format="%(message)s")


def slugify(text: str) -> str:
    """Return a filesystem-friendly slug."""
    return re.sub(r"\W+", "_", text.strip()).strip("_").lower()


def export_site_ndvi(site_name: str, lat: float, lon: float, out_dir: str) -> str:
    """Export NDVI image for a single site and return the output filename."""
    bbox = ee.Geometry.Point(lon, lat).buffer(500).bounds()

    collection = (
        ee.ImageCollection("COPERNICUS/S2_SR")
        .filterBounds(bbox)
        .filterDate("2023-01-01", "2023-12-31")
        .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 20))
    )

    ndvi = collection.median().normalizedDifference(["B8", "B4"]).rename("NDVI")

    os.makedirs(out_dir, exist_ok=True)
    filename = os.path.join(out_dir, f"{slugify(site_name)}_ndvi_2023.png")

    logging.info(f"Exporting {site_name} -> {filename}")
    geemap.ee_export_image(ndvi, filename=filename, region=bbox, scale=10, file_per_band=False)

    return filename


def main(csv_path: str, out_dir: str) -> None:
    ee.Initialize()
    df = pd.read_csv(csv_path)

    mapping = {}
    for _, row in df.iterrows():
        name = row["site_name"]
        lat = row["latitude"]
        lon = row["longitude"]
        output_file = export_site_ndvi(name, lat, lon, out_dir)
        mapping[name] = output_file

    logging.info("\nExport mappings:")
    logging.info(json.dumps(mapping, indent=2))

    logging.info("\nMarkdown table:\n")
    logging.info("| Site | NDVI |")
    logging.info("| --- | --- |")
    for site, path in mapping.items():
        logging.info(f"| {site} | ![]({path}) |")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export Sentinel-2 NDVI images for sites from CSV")
    parser.add_argument("csv", help="CSV file with site_name, latitude, longitude")
    parser.add_argument("--out", default="output/site_ndvi", help="Directory to store output images")
    args = parser.parse_args()

    main(args.csv, args.out)

