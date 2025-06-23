"""Pipeline orchestration."""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Dict

from . import cli, data_fetcher, analyzer, scorer, toponym_analyzer, report_writer
import yaml

CONFIG_PATH = Path(__file__).resolve().parent / "config.yaml"
logging.basicConfig(level=logging.INFO)


def load_config() -> Dict:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def run(args: cli.CliArgs) -> Dict:
    config = load_config()
    out_dir = Path(args.out_dir or config.get("output_dir", "output")) / args.site_id
    logging.info("Output directory: %s", out_dir)
    data = data_fetcher.fetch_site_data(args.lat, args.lon)
    anomalies = analyzer.compute_anomalies(data)
    labels = analyzer.cluster_candidates(anomalies["candidate_mask"])
    summary = analyzer.summarize_clusters(labels)
    tap = scorer.compute_tap_score(summary)
    result = {
        "site_id": args.site_id,
        "lat": args.lat,
        "lon": args.lon,
        "tap_score": tap,
        **summary,
    }
    if args.include_toponyms:
        clues = toponym_analyzer.extract_toponym_clues(args.lat, args.lon, int(config.get("radius_km", 10) * 1000))
        result["toponym_clues"] = clues
    out_dir.mkdir(parents=True, exist_ok=True)
    result_path = out_dir / "results.json"
    result_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    logging.info("Results saved to %s", result_path)
    report_path = out_dir / "report.md"
    report_writer.write_report(result, report_path)
    return result


def main(cli_args=None) -> None:
    args = cli.parse_args(cli_args)
    run(args)


if __name__ == "__main__":
    main()
