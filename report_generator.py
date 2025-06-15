import json
<<<<<<< HEAD

def generate_report_from_template(template_path, output_path, variables):
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    for key, val in variables.items():
        template = template.replace(f"{{{{{key}}}}}", str(val))
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(template)
    print(f"Report generated: {output_path}")

if __name__ == "__main__":
    with open("./output/results.json", "r") as f:
        variables = json.load(f)
    generate_report_from_template("template.md", "generated_report.md", variables)
=======
import os
import re
from datetime import datetime
import subprocess


def parse_template_keys(template_path):
    """Extract placeholder keys from the template."""
    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()
    return set(re.findall(r"{(.*?)}", content))

def generate_report_from_template(template_path, output_path, variables):
    keys = parse_template_keys(template_path)
    missing = []
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # add default variables
    variables.setdefault(
        "generation_date", datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    try:
        commit_hash = (
            subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])
            .decode()
            .strip()
        )
    except Exception:
        commit_hash = "unknown"
    variables.setdefault("commit_hash", commit_hash)

    for key in keys:
        if key not in variables:
            missing.append(key)
            value = "N/A"
        else:
            value = variables[key]
        template = template.replace(f"{{{key}}}", str(value))

    if missing:
        print("Missing keys in results.json:", ", ".join(missing))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(template)
    print(f"Report generated: {output_path}")

def load_variables(json_path):
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)
    print(f"Results file not found: {json_path}")
    return {}


if __name__ == "__main__":
    vars_path = os.path.join("output", "results.json")
    variables = load_variables(vars_path)
    generate_report_from_template(
        "template.md",
        "generated_report.md",
        variables,
    )
>>>>>>> fcbe1eb07b9f56d6be76a348f3322c34bd9ea47c
