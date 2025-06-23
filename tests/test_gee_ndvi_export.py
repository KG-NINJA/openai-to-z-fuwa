import os
import tempfile
import unittest
from unittest import mock

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



if __name__ == "__main__":
    unittest.main()
