import unittest
import json
import os

class TestResultsFile(unittest.TestCase):
    def test_results_json_exists(self):
        self.assertTrue(os.path.exists('results/results.json'))
        with open('results/results.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.assertIn('abstract', data)

if __name__ == '__main__':
    unittest.main()
