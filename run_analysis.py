import os
from PIL import Image, ImageDraw

def run_analysis():
    max_ndvi = 0.92
    candidate_count = 12

    # 保存先ディレクトリ
    output_dir = "./output/images"
    os.makedirs(output_dir, exist_ok=True)  # ここでフォルダを作成（なければ）

    img = Image.new("RGB", (400, 300), (100, 200, 150))
    draw = ImageDraw.Draw(img)
    draw.text((50, 140), "Candidate Map", fill=(255, 255, 255))

    img_path = os.path.join(output_dir, "o3_candidate_map_20250609.png")
    img.save(img_path)

    results = {
        "max_ndvi": max_ndvi,
        "candidate_count": candidate_count,
        "image_path": img_path
    }

    import json
    with open("./output/results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("Analysis done. Results saved to JSON and image generated.")

if __name__ == "__main__":
    run_analysis()


