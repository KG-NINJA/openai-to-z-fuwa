import os
from PIL import Image


def export_ndvi_image(lat, lon, size=(256, 256), output_dir="output/images"):
    """Mock export of an NDVI image for the given coordinates."""
    os.makedirs(output_dir, exist_ok=True)
    filename = f"ndvi_{lat}_{lon}.png"
    path = os.path.join(output_dir, filename)
    # Simple placeholder image
    img = Image.new("RGB", size, (0, 128, 0))
    img.save(path)
    return path


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Mock NDVI export")
    parser.add_argument("lat", type=float)
    parser.add_argument("lon", type=float)
    parser.add_argument("--output", default="output/images")
    args = parser.parse_args()
    result = export_ndvi_image(args.lat, args.lon, output_dir=args.output)
    print(result)

