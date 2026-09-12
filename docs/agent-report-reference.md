# Report generation requirements

Read only for pipeline/report-generation work. These output goals do not require a new report for unrelated development tasks. Workflow execution and external actions remain governed by the root instructions.

[AGENTS.md](../AGENTS.md) governs authorization, stopping, scope and current
verification commands. This reference adds no authority.

# Codex Instructions

## 実行コマンド（パイプライン変更時のみ）
pip install -r requirements.txt
python run_pipeline.py
python -m unittest discover

## コミットメッセージ方針
Describe the scoped change. Use an analysis-report update message with a timestamp only when regenerating that report.

## 🧠 Mission Statement
Use AI to identify and communicate potential archaeological anomalies in vegetation patterns via satellite data in the Amazon.

## 🎯 Output Goals (report-generation tasks only)
- Produce high-quality Markdown report (`generated_report.md`)
- Include summary, coordinates, supporting visuals
- Follow clear scientific narrative, with light poetic tone where suitable

## 📈 Report Sections
- Abstract
- Background
- Methodology
- Key Findings (per candidate site)
- Visuals (NDVI, masks, GeoJSON overlays)
- Interpretation
- Conclusion & Future Work
