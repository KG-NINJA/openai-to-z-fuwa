import os
import tempfile
import unittest
from unittest import mock

from scripts import gee_ndvi_export


class TestGeeNdviExport(unittest.TestCase):
    @mock.patch("geemap.ee_export_image")
    def test_export_creates_file(self, mock_export):
        def fake_export(image, filename, **kwargs):
            with open(filename, "w") as f:
                f.write("test")
        mock_export.side_effect = fake_export

        fake_ee = mock.MagicMock()
        point = mock.MagicMock()
        point.buffer.return_value.bounds.return_value = "bbox"
        fake_ee.Geometry.Point.return_value = point
        collection = mock.MagicMock()
        collection.filterBounds.return_value = collection
        collection.filterDate.return_value = collection
        collection.filter.return_value = collection
        median = mock.MagicMock()
        collection.median.return_value = median
        median.normalizedDifference.return_value.rename.return_value = "img"
        fake_ee.ImageCollection.return_value = collection
        fake_ee.Filter.lt.return_value = None

        with mock.patch.object(gee_ndvi_export, "ee", fake_ee):
            with tempfile.TemporaryDirectory() as tmpdir:
                path = gee_ndvi_export.export_site_ndvi("Site", 0.5, -60.5, tmpdir)
                self.assertTrue(os.path.exists(path))
                self.assertTrue(path.endswith("_ndvi_2023.png"))

    @mock.patch("scripts.gee_ndvi_export.ee.Initialize", side_effect=Exception("Auth fail"))
    def test_initialize_failure_exits(self, mock_init):
        with self.assertRaises(SystemExit):
            gee_ndvi_export.initialize_earthengine()


if __name__ == "__main__":
    unittest.main()
