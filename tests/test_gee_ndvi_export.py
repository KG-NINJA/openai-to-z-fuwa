import os
import tempfile
import unittest
from unittest import mock

try:
    from scripts import gee_ndvi_export
except Exception:
    gee_ndvi_export = None
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
    def test_slugify(self):
        if not gee_ndvi_export:
            self.skipTest('gee_ndvi_export unavailable')
        self.assertEqual(gee_ndvi_export.slugify('A B/C'), 'a_b_c')

    def test_export_site_ndvi_mocked(self):
        if not gee_ndvi_export:
            self.skipTest('gee_ndvi_export unavailable')
        with mock.patch.object(gee_ndvi_export, 'ee', FakeEE):
            with mock.patch.object(gee_ndvi_export.geemap, 'ee_export_image') as mock_export:
                out = gee_ndvi_export.export_site_ndvi('Site', 0.0, 0.0, 'out')
                self.assertTrue(out.endswith('.png'))
                mock_export.assert_called_once()
if __name__ == "__main__":
    unittest.main()

