import json
import os
import subprocess
import jinja2

TEMPLATE_PATH = os.path.join('templates', 'template.md')
JSON_PATH = os.path.join('outputs', 'results.json')
MD_PATH = 'generated_report.md'
PDF_PATH = 'generated_report.pdf'


def load_variables(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def render_markdown(template_path, variables):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(template_path)),
                             autoescape=False,
                             keep_trailing_newline=True)
    template = env.get_template(os.path.basename(template_path))
    return template.render(**variables)


def generate_report():
    data = load_variables(JSON_PATH)
    markdown = render_markdown(TEMPLATE_PATH, data)
    with open(MD_PATH, 'w', encoding='utf-8') as f:
        f.write(markdown)
    print(f'Markdown generated at {MD_PATH}')

    try:
        subprocess.run(['pandoc', MD_PATH, '-o', PDF_PATH], check=True)
        print(f'PDF generated at {PDF_PATH}')
    except Exception as e:
        print('PDF generation failed:', e)


if __name__ == '__main__':
    generate_report()
