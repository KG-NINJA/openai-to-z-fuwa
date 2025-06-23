"""Command line interface for the pipeline."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Optional


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Amazon ruin detection pipeline")
    parser.add_argument("--lat", type=float, required=True, help="Latitude")
    parser.add_argument("--lon", type=float, required=True, help="Longitude")
    parser.add_argument("--site-id", default="site", help="Identifier for outputs")
    parser.add_argument("--include-toponyms", dest="include_toponyms", action="store_true", default=True, help="Search for toponyms")
    parser.add_argument("--no-include-toponyms", dest="include_toponyms", action="store_false", help="Skip toponym search")
    parser.add_argument("--out-dir", default=None, help="Base output directory")
    return parser


@dataclass
class CliArgs:
    lat: float
    lon: float
    site_id: str
    include_toponyms: bool
    out_dir: Optional[str]


def parse_args(args: Optional[list[str]] = None) -> CliArgs:
    parser = build_parser()
    ns = parser.parse_args(args)
    return CliArgs(
        lat=ns.lat,
        lon=ns.lon,
        site_id=ns.site_id,
        include_toponyms=ns.include_toponyms,
        out_dir=ns.out_dir,
    )
