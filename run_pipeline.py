# -*- coding: utf-8 -*-
import argparse
import json
import os
import subprocess
import sys
from datetime import datetime

import run_analysis

def print_and_log(msg):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now}] {msg}")

def run_command(command, desc=""):
    try:
        print_and_log(f"{desc} 実行: {command}")
        subprocess.run(command, check=True, shell=True)
        print_and_log(f"{desc} 完了")
    except subprocess.CalledProcessError:
        print_and_log(f"{desc} 失敗")
        sys.exit(1)

DEFAULT_SITES = ["O1", "O2", "O3", "O4", "O5"]

def merge_results(site):
    site_path = os.path.join("output", f"{site}_results.json")
    if not os.path.exists(site_path):
        print_and_log(f"⚠️ Results file not found for {site}: {site_path}")
        return
    with open(site_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    results_path = os.path.join("output", "results.json")
    if os.path.exists(results_path):
        with open(results_path, "r", encoding="utf-8") as f:
            merged = json.load(f)
    else:
        merged = {}

    merged.update(data)

    with open(results_path, "w", encoding="utf-8") as f:
        json.dump(merged, f, indent=2)


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", help="Process a single site")
    parsed = parser.parse_args(args)

    sites = [parsed.site] if parsed.site else DEFAULT_SITES

    # 1. 解析の実行
    for site in sites:
        print_and_log(f"Running analysis for {site}")
        run_analysis.run_analysis(site)
        merge_results(site)

    # 2. レポート生成
    run_command("python scripts/report_generator.py", desc="レポート生成")

if __name__ == "__main__":
    print_and_log("===== OpenAI to Z 自動パイプライン開始 =====")
    main()
    print_and_log("===== 完了 =====")
