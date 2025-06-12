import json
import jinja2

class NAUndefined(jinja2.Undefined):
    def __str__(self):
        return "N/A"

    def __getattr__(self, name):
        return "N/A"

    def __iter__(self):
        return iter([])

    def __call__(self, *args, **kwargs):
        return "N/A"

TEMPLATE_PATH = "template.md"
JSON_PATH = "results.json"
OUTPUT_PATH = "generated_report.md"

def main():
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader("."),
        undefined=NAUndefined,
        autoescape=False,
        keep_trailing_newline=True,
    )
    template = env.get_template(TEMPLATE_PATH)

    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    rendered = template.render(**data)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(rendered)

    print(rendered)

if __name__ == '__main__':
    main()
