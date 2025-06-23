"""Generate Markdown reports using OpenAI."""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Dict, List

import openai

TEMPLATE_PATH = Path("templates/template.md")

logging.basicConfig(level=logging.INFO)


def build_prompt(context: Dict) -> str:
    """Return a prompt for GPT including toponym clues."""
    parts = [
        "You are a helpful archaeological assistant generating a Markdown report.",
        "Include a dedicated section titled 'Toponymic and Local-Legend Insights'."
    ]
    if context.get("toponym_clues"):
        clues_json = json.dumps(context["toponym_clues"], indent=2, ensure_ascii=False)
        parts.append(
            "Interpret these place names and speculate on their archaeological significance:\n" + clues_json
        )
    else:
        parts.append("No legend-rich toponyms were detected around the site.")
    return "\n".join(parts)


def render_markdown(context: Dict) -> str:
    """Call OpenAI to generate a report body."""
    prompt = build_prompt(context)
    logging.info("Requesting GPT to generate report")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as exc:
        logging.error("OpenAI request failed: %s", exc)
        return "GPT generation failed."


def write_report(context: Dict, out_path: Path) -> None:
    """Generate Markdown from GPT and save to file."""
    markdown = render_markdown(context)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(markdown, encoding="utf-8")
    logging.info("Report written to %s", out_path)
