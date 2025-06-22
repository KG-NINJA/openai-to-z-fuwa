import os
import unittest
import tempfile

from scripts import gee_ndvi_export


class TestGeeNdviExport(unittest.TestCase):
    def test_export_creates_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = gee_ndvi_export.export_ndvi_image(0.5, -60.5, output_dir=tmpdir)
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path.endswith('.png'))


if __name__ == '__main__':
    unittest.main()
