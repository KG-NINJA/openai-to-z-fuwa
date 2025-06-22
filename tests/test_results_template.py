import os
import json
import unittest

from scripts import report_generator


class TestResultsAndTemplate(unittest.TestCase):
    def test_results_json_and_template_render(self):
        path = os.path.join('output', 'results.json')
        self.assertTrue(os.path.exists(path), 'results.json missing')
        with open(path, 'r') as f:
            data = json.load(f)

        for key in ['max_ndvi', 'candidate_count', 'image_path']:
            self.assertIn(key, data)

        markdown = report_generator.render_markdown(report_generator.TEMPLATE_PATH, data)
        self.assertIsInstance(markdown, str)
        self.assertGreater(len(markdown), 0)


if __name__ == '__main__':
    unittest.main()
