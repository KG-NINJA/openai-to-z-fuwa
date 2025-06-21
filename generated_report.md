
## Abstract
{{ abstract }}

## Background
{{ background }}

## Methodology
{{ methodology }}

## Key Findings
{{ key_findings }}

## Visual Summary
![NDVI Chart]({{ ndvi_chart }})

## Candidate Map
Link: [{{ geojson_file }}]({{ geojson_file }})

## Candidate Sites
{% for site in sites %}
### Site {{ site.id }}: {{ site.name }}
- Coordinates: ({{ site.coords.lat }}, {{ site.coords.lon }})
- Max NDVI: {{ site.max_ndvi }}
- Candidate Count: {{ site.candidate_count }}
- Historical Reference: {{ site.historical_reference }}
- Serendipity Log: {{ site.serendipity_log }}
- Intuition Trace: {{ site.intuition_trace }}
- Insights: {{ site.insight_log }}
{% endfor %}

## Additional Candidate Sites
{% for c in additional_candidates %}
- Name: {{ c.name }}
- Coordinates: ({{ c.coords.lat }}, {{ c.coords.lon }})
- Reason: {{ c.reason }}
{% endfor %}

## Interpretation
{{ interpretation }}

## Conclusion
{{ conclusion }}

## Project Philosophy
{{ philosophy }}

## Empathy Statement
{{ empathy_statement }}

## Personal Reflection
{{ personal_reflection }}

## Humanity Perspective
{{ humanity_perspective }}

## AI Insight Assist
- {{ ai_insight_assist }}

## Footnote

