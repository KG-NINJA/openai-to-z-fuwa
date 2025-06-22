import os
import numpy as np
import matplotlib.pyplot as plt
import json

def run_analysis(location):
    # NDVIデータのロード
    ndvi_path = f"./ndvi_tiles/{location}/ndvi.npy"
    if not os.path.exists(ndvi_path):
        print(f"⚠️ NDVI file not found for {location}: {ndvi_path}")
        return

    ndvi_data = np.load(ndvi_path)
    max_ndvi = float(ndvi_data.max())

    # NDVIの閾値から候補マスクを生成（例：0.85以上を候補とする）
    candidate_threshold = 0.85
    candidate_mask = ndvi_data > candidate_threshold
    candidate_count = int(candidate_mask.sum())

    # 出力先ディレクトリ
    output_img_dir = f"./output/images/{location}"
    os.makedirs(output_img_dir, exist_ok=True)

    # 候補地マップ描画
    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(ndvi_data, cmap='Greens')
    y, x = np.where(candidate_mask)
    if candidate_count > 0:
        ax.scatter(x, y, c='red', s=12, label='Candidate')
        ax.legend()
    ax.set_title(f"Candidate Map - {location}")
    ax.axis('off')
    plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)

    img_path = os.path.join(output_img_dir, "candidate_map.png")
    plt.savefig(img_path, dpi=300, bbox_inches='tight')
    plt.close()

    # 統計データの保存
    results = {
        "location": location,
        "max_ndvi": max_ndvi,
        "candidate_count": candidate_count,
        "image_path": img_path
    }
    result_path = f"./output/{location}_results.json"
    with open(result_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"✅ {location}: Analysis done. Results saved to {result_path} and candidate map generated.")

if __name__ == "__main__":
    # 全地点を一気に処理
    locations = ["O1", "O2", "O3", "O4", "O5"]
    for loc in locations:
        run_analysis(loc)
