from pathlib import Path
from datetime import datetime
import html
import re
import feedparser

from feeds import FEEDS
from scorer import score_entry, is_low_value_entry


def strip_html(text: str) -> str:
    text = text or ""
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def categorize_item(text: str) -> str:
    text = (text or "").lower()

    if any(w in text for w in ["lawsuit", "sue", "suing", "copyright", "violated", "kanne", "oikeusjuttu", "stämning"]):
        return "legal"

    if any(w in text for w in ["leak", "leaked", "security", "breach", "takedown", "vuoto", "tietovuoto", "tietoturva", "läcka"]):
        return "security"

    if any(w in text for w in ["privacy", "surveillance", "unmask", "integritet", "övervakning", "yksityisyys", "valvonta"]):
        return "privacy"

    if any(w in text for w in ["hallucination", "hallucinated", "fake", "fabricated", "halluzination"]):
        return "hallucination"

    if any(w in text for w in ["citation", "citations", "reference", "references", "paper", "research", "journal", "academic"]):
        return "research integrity"

    if any(w in text for w in ["school", "pupils", "teachers", "education", "students", "oppiminen", "koulu", "skola", "elever"]):
        return "education"

    return "general"


def fetch_entries():
    items = []

    for url in FEEDS:
        feed = feedparser.parse(url)
        source = feed.feed.get("title", url)

        for entry in feed.entries:
            title = entry.get("title", "")
            summary_raw = entry.get("summary", "") or entry.get("description", "")
            summary = strip_html(summary_raw)
            link = entry.get("link", "")

            if is_low_value_entry(title, summary, link, source):
                continue

            combined = f"{title}\n{summary}\n{link}\n{source}"
            score = score_entry(combined)

            if score >= 12:
                items.append({
                    "title": title,
                    "summary": summary,
                    "link": link,
                    "source": source,
                    "score": score,
                    "category": categorize_item(combined),
                })

    unique = {}
    for item in items:
        unique[item["link"]] = item

    items = list(unique.values())
    items.sort(key=lambda x: x["score"], reverse=True)
    return items[:10]


def make_markdown(items):
    today = datetime.now().strftime("%Y-%m-%d")
    lines = [f"# AI Fail Watch – {today}", ""]

    if not items:
        lines.append("No strong AI failure articles found today.")
        lines.append("")
        return "\n".join(lines)

    for i, item in enumerate(items, start=1):
        lines.append(f"## {i}. {item['title']}")
        lines.append(f"**Source:** {item['source']}")
        lines.append(f"**Category:** {item['category']}")
        lines.append(f"**Score:** {item['score']}")
        lines.append(f"**Link:** {item['link']}")
        lines.append("")
        if item["summary"]:
            lines.append(item["summary"])
            lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def make_html(items):
    today = datetime.now().strftime("%Y-%m-%d")

    cards = []
    for i, item in enumerate(items, start=1):
        title = html.escape(item["title"])
        source = html.escape(item["source"])
        category = html.escape(item["category"])
        score = html.escape(str(item["score"]))
        link = html.escape(item["link"])
        summary = html.escape(item["summary"])

        card = f"""
        <article class="card">
            <div class="meta-top">#{i}</div>
            <h2><a href="{link}" target="_blank" rel="noopener noreferrer">{title}</a></h2>
            <div class="meta">
                <span><strong>Source:</strong> {source}</span>
                <span><strong>Category:</strong> {category}</span>
                <span><strong>Score:</strong> {score}</span>
            </div>
            <p>{summary}</p>
            <p><a class="readmore" href="{link}" target="_blank" rel="noopener noreferrer">Open article ↗</a></p>
        </article>
        """
        cards.append(card)

    if not cards:
        cards_html = """
        <article class="card">
            <h2>No strong AI failure articles found today.</h2>
        </article>
        """
    else:
        cards_html = "\n".join(cards)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Fail Watch – {today}</title>
    <style>
        :root {{
            --bg: #0b1020;
            --panel: #131a2a;
            --text: #e8edf7;
            --muted: #9aa6bf;
            --accent: #6ea8fe;
            --border: #26324a;
        }}

        * {{
            box-sizing: border-box;
        }}

        body {{
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.55;
        }}

        .wrap {{
            max-width: 980px;
            margin: 0 auto;
            padding: 32px 20px 60px;
        }}

        header {{
            margin-bottom: 28px;
        }}

        h1 {{
            margin: 0 0 8px;
            font-size: 2rem;
        }}

        .subtitle {{
            color: var(--muted);
            font-size: 1rem;
        }}

        .card {{
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 20px;
            margin-bottom: 18px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.22);
        }}

        .meta-top {{
            color: var(--muted);
            font-size: 0.92rem;
            margin-bottom: 8px;
        }}

        h2 {{
            margin: 0 0 10px;
            font-size: 1.25rem;
        }}

        .meta {{
            display: flex;
            flex-wrap: wrap;
            gap: 14px;
            color: var(--muted);
            font-size: 0.95rem;
            margin-bottom: 14px;
        }}

        p {{
            margin: 0 0 12px;
        }}

        a {{
            color: var(--accent);
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}

        .readmore {{
            font-weight: bold;
        }}

        footer {{
            margin-top: 30px;
            color: var(--muted);
            font-size: 0.9rem;
        }}
    </style>
</head>
<body>
    <div class="wrap">
        <header>
            <h1>AI Fail Watch</h1>
            <div class="subtitle">Daily AI failure report • {today}</div>
        </header>

        {cards_html}

        <footer>
            Generated automatically from selected RSS feeds.
        </footer>
    </div>
</body>
</html>
"""


def main():
    items = fetch_entries()

    md_output = make_markdown(items)
    html_output = make_html(items)

    Path("data").mkdir(exist_ok=True)
    Path("data/latest.md").write_text(md_output, encoding="utf-8")
    Path("data/index.html").write_text(html_output, encoding="utf-8")

    print("Done. Wrote data/latest.md and data/index.html")


if __name__ == "__main__":
    main()