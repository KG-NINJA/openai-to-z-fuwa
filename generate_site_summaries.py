"""Generate one-line summaries for candidate archaeological sites.

This script reads a JSON file containing candidate sites and outputs a
Markdown file summarizing them. Each summary is a single short sentence
mentioning the evidence found.
"""

import json
from pathlib import Path
from typing import List, Dict


def load_candidates(json_path: str) -> List[Dict[str, str]]:
    """Load candidate sites from a JSON file."""
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def truncate_text(text: str, max_words: int) -> str:
    """Return the text truncated to a maximum number of words."""
    words = text.split()
    return " ".join(words[:max_words])


def generate_summary(evidence: str, max_words: int = 4) -> str:
    """Create a short declarative summary from evidence."""
    truncated = truncate_text(evidence, max_words)
    return f"Found {truncated}; suggests archaeological significance."


def generate_summaries(candidates: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Generate a one-line summary for each candidate site."""
    results = []
    for site in candidates:
        site_name = site.get("site_name", "Unknown Site")
        evidence = site.get("evidence", "")
        image_path = site.get("image_path", "")
        summary = generate_summary(evidence)
        results.append({
            "site_name": site_name,
            "summary": summary,
            "image_path": image_path,
        })
    return results


def write_markdown(summaries: List[Dict[str, str]], output_path: str) -> None:
    """Write the summaries to a Markdown file."""
    lines = []
    for item in summaries:
        lines.append(f"### {item['site_name']}")
        lines.append(f"> \"{item['summary']}\"")
        lines.append(f"Evidence: ![]({item['image_path']})")
        lines.append("")
    Path(output_path).write_text("\n".join(lines), encoding="utf-8")
    print(f"Markdown saved to {output_path}")


def main(json_path: str = "candidates.json", output_path: str = "summaries.md") -> None:
    candidates = load_candidates(json_path)
    summaries = generate_summaries(candidates)
    write_markdown(summaries, output_path)


if __name__ == "__main__":
    main()
