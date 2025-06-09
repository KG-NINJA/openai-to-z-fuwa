import re
import sys

REQUIRED_KEYS = [
    "abstract",
    "background",
    "methodology",
    "dataset_info",
    "area_coordinates",
    "ndvi_threshold",
    "z_score_cutoff",
    "key_findings",
    "ndvi_chart",
    "mask_image",
    "interpretation",
    "conclusion",
    "generation_date",
    "commit_hash",
]

def validate_template(template_path):
    try:
        with open(template_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ File not found: {template_path}")
        return False

    missing_keys = []
    for key in REQUIRED_KEYS:
        pattern = r"\{\{" + key + r"\}\}"
        if not re.search(pattern, content):
            missing_keys.append(key)

    if missing_keys:
        print("❌ Missing placeholders in template:")
        for key in missing_keys:
            print(f"  - {{{{{key}}}}}")
        return False
    else:
        print("✅ All required placeholders are present in the template.")
        return True

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "template.md"
    validate_template(path)
