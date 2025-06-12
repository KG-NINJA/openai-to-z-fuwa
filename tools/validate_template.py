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
