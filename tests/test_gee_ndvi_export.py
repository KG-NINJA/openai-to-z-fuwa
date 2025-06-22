import os
import unittest
import tempfile

from scripts import gee_ndvi_export
from types import SimpleNamespace


class FakeGeometry:
    @staticmethod
    def Point(lon, lat):
        class _Geom:
            def buffer(self, radius):
                return self

            def bounds(self):
                return self

        return _Geom()


class FakeImage:
    def normalizedDifference(self, bands):
        return self

    def rename(self, name):
        return self


class FakeCollection:
    def __init__(self, name=None):
        pass

    def filterBounds(self, bbox):
        return self

    def filterDate(self, start, end):
        return self

    def filter(self, *_):
        return self

    def median(self):
        return FakeImage()


class FakeFilter:
    @staticmethod
    def lt(a, b):
        return None


class FakeEE(SimpleNamespace):
    Geometry = FakeGeometry
    ImageCollection = FakeCollection
    Filter = FakeFilter


class TestGeeNdviExport(unittest.TestCase):
    def test_export_creates_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # Patch the ee and geemap modules to avoid Earth Engine calls
            gee_ndvi_export.ee = FakeEE()

            def fake_export_image(*args, filename=None, **kwargs):
                with open(filename, "w") as f:
                    f.write("")

            gee_ndvi_export.geemap.ee_export_image = fake_export_image

            path = gee_ndvi_export.export_site_ndvi(
                "test_site", 0.5, -60.5, tmpdir
            )
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path.endswith('.png'))


if __name__ == '__main__':
    unittest.main()
