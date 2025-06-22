import sys
import re
import jinja2

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


def check_required_placeholders(content: str):
    missing = []
    for key in REQUIRED_KEYS:
        pattern = r"\{\{" + key + r"\}\}"
        if not re.search(pattern, content):
            missing.append(key)
    return missing


def check_old_placeholders(content: str):
    """Return any single-brace placeholders from legacy templates."""
    pattern = re.compile(r"(?<![{%]){[^{}%]+}(?![}%])")
    return pattern.findall(content)


def validate_template(path: str) -> bool:
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ File not found: {path}")
        return False

    missing = check_required_placeholders(content)
    if missing:
        print("❌ Missing placeholders in template:")
        for key in missing:
            print(f"  - {{{{{key}}}}}")
        return False

    old = check_old_placeholders(content)
    if old:
        print("Old-style placeholders found:", ", ".join(old))
        return False

    env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
    try:
        env.get_template(path)
    except jinja2.TemplateSyntaxError as e:
        print(f"Template syntax error in {path}: {e}")
        return False

    print("✅ All required placeholders are present and template syntax is valid.")
    return True


if __name__ == "__main__":
    template_path = sys.argv[1] if len(sys.argv) > 1 else "template.md"
    if not validate_template(template_path):
        sys.exit(1)
