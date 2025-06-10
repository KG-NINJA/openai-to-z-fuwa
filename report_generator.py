import json

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
