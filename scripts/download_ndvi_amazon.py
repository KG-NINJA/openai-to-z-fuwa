import os
import ee
import geemap

"""Download yearly median NDVI for the Amazon basin.

This script requires Google Earth Engine authentication. Run `earthengine authenticate`
before executing. NDVI images for each year from 2015 through 2024 are exported
as GeoTIFFs in the current directory.
"""

def main():
    # Initialize Earth Engine
    ee.Initialize()

    # Approximate Amazon basin bounding box
    amazon_basin = ee.Geometry.BBox(-74.0, -20.0, -50.0, 5.0)

    collection = ee.ImageCollection('MODIS/006/MOD13A2').select('NDVI')

    for year in range(2015, 2025):
        start = f"{year}-01-01"
        end = f"{year}-12-31"
        image = collection.filterDate(start, end).median()
        filename = f"amazon_ndvi_{year}.tif"
        print(f"Exporting {filename} ...")
        geemap.ee_export_image(
            image,
            filename=filename,
            region=amazon_basin,
            scale=1000,
            file_per_band=False,
        )

if __name__ == "__main__":
    main()
