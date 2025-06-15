<<<<<<< HEAD
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
=======
import sys
import re
import jinja2


def check_old_placeholders(content):
    """Return any single-brace placeholders from legacy templates."""
    pattern = re.compile(r"(?<![{%]){[^{}%]+}(?![}%])")
    return pattern.findall(content)


def main(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    old = check_old_placeholders(content)
    if old:
        print("Old-style placeholders found:", ", ".join(old))
        sys.exit(1)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    try:
        env.get_template(path)
    except jinja2.TemplateSyntaxError as e:
        print(f"Template syntax error in {path}: {e}")
        sys.exit(1)
    print(f"{path} is valid.")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python tools/validate_template.py <template>')
        sys.exit(1)
    main(sys.argv[1])
>>>>>>> fcbe1eb07b9f56d6be76a348f3322c34bd9ea47c
