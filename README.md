# AI Fail Watch

Bot project for tracking AI failures, problems, hallucinations, and broken promises from international news sources.

## What it does

- Reads selected RSS feeds
- Looks for AI-related failure signals
- Scores articles based on relevance
- Writes a daily Markdown report to `data/latest.md`

## Sources

Current sources include:
- Nature
- Ars Technica
- The Guardian

## Run locally

```bash
python -m pip install -r requirements.txt
python app.py