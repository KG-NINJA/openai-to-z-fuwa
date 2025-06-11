import json
import jinja2

class NAUndefined(jinja2.Undefined):
    def __str__(self):
        return 'N/A'
    def __getattr__(self, name):
        return 'N/A'
    def __iter__(self):
        return iter([])
    def __call__(self, *args, **kwargs):
        return 'N/A'

TEMPLATE_PATH = 'template.md'
JSON_PATH = 'results.json'
OUTPUT_PATH = 'generated_report.md'

def main():
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template_str = f.read()
    # convert single-brace placeholders like {foo} to Jinja2 style {{ foo }}
    import re
    template_str = re.sub(r'(?<!\{)\{([a-zA-Z0-9_]+)\}(?!\})', r'{{ \1 }}', template_str)
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Ensure lists exist for loop sections
    if 'sites' not in data or not isinstance(data['sites'], list) or not data['sites']:
        data['sites'] = [{
            'id': 'N/A',
            'name': 'N/A',
            'coords': {'lat': 'N/A', 'lon': 'N/A'},
            'max_ndvi': 'N/A',
            'candidate_count': 'N/A',
            'historical_reference': 'N/A',
            'serendipity_log': 'N/A',
            'intuition_trace': 'N/A',
            'insight_log': 'N/A'
        }]
    if 'additional_candidates' not in data or not isinstance(data['additional_candidates'], list) or not data['additional_candidates']:
        data['additional_candidates'] = [{
            'name': 'N/A',
            'coords': {'lat': 'N/A', 'lon': 'N/A'},
            'reason': 'N/A'
        }]

    env = jinja2.Environment(undefined=NAUndefined)
    template = env.from_string(template_str)
    rendered = template.render(**data)
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(rendered)
    print(rendered)

if __name__ == '__main__':
    main()
