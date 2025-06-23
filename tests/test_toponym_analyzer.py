import unittest
from unittest.mock import patch, MagicMock

from openai_to_z import toponym_analyzer


class TestToponymAnalyzer(unittest.TestCase):
    def test_extract_toponym_clues(self):
        fake_node = MagicMock()
        fake_node.tags = {"name": "Monte dos Mortos"}
        fake_node.lat = -2.099
        fake_node.lon = -55.599

        fake_result = MagicMock()
        fake_result.nodes = [fake_node]

        with patch.object(toponym_analyzer.overpy, "Overpass") as mock_overpass:
            mock_overpass.return_value.query.return_value = fake_result
            clues = toponym_analyzer.extract_toponym_clues(-2.1, -55.6, radius=5000)

        self.assertGreater(len(clues), 0)


if __name__ == "__main__":
    unittest.main()
