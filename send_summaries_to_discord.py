import argparse
import os
import re
from pathlib import Path
from typing import List, Dict

import requests


SITE_HEADER = re.compile(r"^### (.+)")
SUMMARY_LINE = re.compile(r'^>\s*"(.+)"')
IMAGE_LINE = re.compile(r'!\[]\((.+)\)')


def parse_summaries(md_path: str) -> List[Dict[str, str]]:
    """Parse summaries.md into structured data."""
    lines = Path(md_path).read_text(encoding="utf-8").splitlines()
    items: List[Dict[str, str]] = []
    i = 0
    while i < len(lines):
        header = SITE_HEADER.match(lines[i])
        if header:
            site_name = header.group(1).strip()
            summary = ""
            image_path = ""
            if i + 1 < len(lines):
                m = SUMMARY_LINE.match(lines[i + 1].strip())
                if m:
                    summary = m.group(1)
            if i + 2 < len(lines):
                m = IMAGE_LINE.search(lines[i + 2])
                if m:
                    image_path = m.group(1)
            items.append({
                "site_name": site_name,
                "summary": summary,
                "image_path": image_path,
            })
            i += 3
        else:
            i += 1
    return items


def send_to_discord(webhook_url: str, site: Dict[str, str]) -> None:
    """Send a single site summary to Discord."""
    content = f"### {site['site_name']}\n> \"{site['summary']}\"\nEvidence:"
    files = None
    if site.get("image_path") and Path(site["image_path"]).exists():
        files = {
            "file": (Path(site["image_path"]).name, open(site["image_path"], "rb"))
        }
    resp = requests.post(webhook_url, data={"content": content}, files=files)
    resp.raise_for_status()


def main(md_path: str = "summaries.md", webhook_url: str | None = None) -> None:
    if not webhook_url:
        webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        raise SystemExit("Discord webhook URL not provided")

    for site in parse_summaries(md_path):
        send_to_discord(webhook_url, site)
        print(f"Sent {site['site_name']} to Discord")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send site summaries to Discord")
    parser.add_argument("--md", default="summaries.md", help="Path to summaries.md")
    parser.add_argument("--webhook", default=None, help="Discord webhook URL")
    args = parser.parse_args()
    main(args.md, args.webhook)
