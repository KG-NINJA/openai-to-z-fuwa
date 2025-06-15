import unittest
import json
import os

class TestResultsFile(unittest.TestCase):
    def test_results_json_exists(self):
        self.assertTrue(os.path.exists('output/results.json'))

if __name__ == '__main__':
    unittest.main()
