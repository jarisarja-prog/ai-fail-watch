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
        return "Legal"

    if any(w in text for w in ["leak", "leaked", "security", "breach", "takedown", "vuoto", "tietovuoto", "tietoturva", "läcka"]):
        return "Security"

    if any(w in text for w in ["privacy", "surveillance", "unmask", "integritet", "övervakning", "yksityisyys", "valvonta"]):
        return "Privacy"

    if any(w in text for w in ["hallucination", "hallucinated", "fake", "fabricated", "halluzination"]):
        return "Hallucination"

    if any(w in text for w in ["citation", "citations", "reference", "references", "paper", "research", "journal", "academic"]):
        return "Research integrity"

    if any(w in text for w in ["school", "pupils", "teachers", "education", "students", "oppiminen", "koulu", "skola", "elever"]):
        return "Education"

    return "General"


def explain_fail(category: str) -> str:
    mapping = {
        "Legal": "Legal risk: AI use triggered legal or copyright issues.",
        "Security": "Security failure: data leak, breach or system exposure.",
        "Privacy": "Privacy risk: user data or identity may be exposed.",
        "Hallucination": "AI hallucination: the system produced false information.",
        "Research integrity": "Research issue: unreliable, fabricated or unverified results.",
        "Education": "Education risk: AI may be weakening learning or thinking skills.",
        "General": "General AI-related risk or failure signal.",
    }
    return mapping.get(category, "")


def detect_language(source: str, title: str, summary: str) -> str:
    combined = f"{source} {title} {summary}".lower()

    if any(x in combined for x in ["helsingin sanomat", "yle", "tekoäly", "tietoturva", "yksityisyys", "oppiminen"]):
        return "FI"
    if any(x in combined for x in ["svt", "sveriges radio", "artificiell intelligens", "integritet", "övervakning"]):
        return "SV"
    return "EN"


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
                category = categorize_item(combined)
                items.append({
                    "title": title,
                    "summary": summary,
                    "link": link,
                    "source": source,
                    "score": score,
                    "category": category,
                    "category_explainer": explain_fail(category),
                    "lang": detect_language(source, title, summary),
                })

    unique = {}
    for item in items:
        unique[item["link"]] = item

    items = list(unique.values())
    items.sort(key=lambda x: x["score"], reverse=True)
    return items[:30]


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
        lines.append(f"**Language:** {item['lang']}")
        lines.append(f"**Score:** {item['score']}")
        lines.append(f"**Link:** {item['link']}")
        lines.append("")
        if item["summary"]:
            lines.append(item["summary"])
            lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def category_class(category: str) -> str:
    mapping = {
        "Legal": "cat-legal",
        "Security": "cat-security",
        "Privacy": "cat-privacy",
        "Hallucination": "cat-hallucination",
        "Research integrity": "cat-research",
        "Education": "cat-education",
        "General": "cat-general",
    }
    return mapping.get(category, "cat-general")


def make_top_card(item: dict) -> str:
    title = html.escape(item["title"])
    source = html.escape(item["source"])
    category = html.escape(item["category"])
    score = html.escape(str(item["score"]))
    link = html.escape(item["link"])
    summary = html.escape(item["summary"])
    lang = html.escape(item["lang"])
    explainer = html.escape(item["category_explainer"])
    cat_class = category_class(item["category"])

    return f"""
    <section class="hero-card" data-lang="{lang}">
        <div class="hero-label">Top fail of the day</div>
        <h2><a href="{link}" target="_blank" rel="noopener noreferrer">{title}</a></h2>
        <div class="meta">
            <span class="badge {cat_class}">{category}</span>
            <span class="badge lang">{lang}</span>
            <span><strong>Source:</strong> {source}</span>
            <span class="score-big">🔥 {score}</span>
        </div>
        <p class="why">{explainer}</p>
        <p>{summary}</p>
        <a class="readmore" href="{link}" target="_blank" rel="noopener noreferrer">Read article ↗</a>
    </section>
    """


def make_cards(items: list[dict]) -> str:
    cards = []

    for i, item in enumerate(items, start=1):
        title = html.escape(item["title"])
        source = html.escape(item["source"])
        category = html.escape(item["category"])
        score = html.escape(str(item["score"]))
        link = html.escape(item["link"])
        summary = html.escape(item["summary"])
        lang = html.escape(item["lang"])
        explainer = html.escape(item["category_explainer"])
        cat_class = category_class(item["category"])

        cards.append(f"""
        <article class="card" data-lang="{lang}" onclick="openLink('{link}')">
            <div class="card-top">
                <span class="rank">#{i}</span>
                <span class="badge {cat_class}">{category}</span>
                <span class="badge lang">{lang}</span>
                <span class="score-big">🔥 {score}</span>
            </div>

            <h3><a href="{link}" target="_blank" rel="noopener noreferrer" onclick="event.stopPropagation()">{title}</a></h3>

            <div class="meta">
                <span><strong>Source:</strong> {source}</span>
            </div>

            <p class="why"><em>{explainer}</em></p>
            <p>{summary}</p>

            <a class="readmore" href="{link}" target="_blank" rel="noopener noreferrer" onclick="event.stopPropagation()">Open article ↗</a>
        </article>
        """)

    return "\n".join(cards)


def make_archive_index():
    archive_dir = Path("archive")
    archive_dir.mkdir(exist_ok=True)

    files = sorted(archive_dir.glob("*.html"), reverse=True)

    links = []
    for f in files:
        day = f.stem
        links.append(f'<li><a href="archive/{f.name}">{day}</a></li>')

    links_html = "\n".join(links) if links else "<li>No archived reports yet.</li>"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Fail Watch Archive</title>
    <style>
        body {{
            margin: 0;
            font-family: Inter, Arial, sans-serif;
            background: #0b1020;
            color: #eaf0fb;
            line-height: 1.6;
        }}
        .wrap {{
            max-width: 900px;
            margin: 0 auto;
            padding: 32px 18px 60px;
        }}
        h1 {{
            margin-top: 0;
        }}
        a {{
            color: #6ea8fe;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .back {{
            display: inline-block;
            margin-bottom: 20px;
        }}
        .card {{
            background: #121a2b;
            border: 1px solid #26324a;
            border-radius: 16px;
            padding: 20px;
        }}
        ul {{
            margin: 0;
            padding-left: 20px;
        }}
        li {{
            margin-bottom: 10px;
        }}
    </style>
</head>
<body>
    <div class="wrap">
        <a class="back" href="index.html">← Back to latest report</a>
        <h1>AI Fail Watch Archive</h1>
        <div class="card">
            <ul>
                {links_html}
            </ul>
        </div>
    </div>
</body>
</html>
"""


def make_archive_page(items, day: str):
    cards = []

    if not items:
        cards_html = "<p>No archived items for this day.</p>"
    else:
        for i, item in enumerate(items, start=1):
            title = html.escape(item["title"])
            source = html.escape(item["source"])
            category = html.escape(item["category"])
            score = html.escape(str(item["score"]))
            link = html.escape(item["link"])
            summary = html.escape(item["summary"])
            lang = html.escape(item["lang"])
            explainer = html.escape(item["category_explainer"])
            cat_class = category_class(item["category"])

            cards.append(f"""
            <article class="card" data-lang="{lang}" onclick="openLink('{link}')">
                <div class="card-top">
                    <span class="rank">#{i}</span>
                    <span class="badge {cat_class}">{category}</span>
                    <span class="badge lang">{lang}</span>
                    <span class="score-big">🔥 {score}</span>
                </div>
                <h3><a href="{link}" target="_blank" rel="noopener noreferrer" onclick="event.stopPropagation()">{title}</a></h3>
                <div class="meta">
                    <span><strong>Source:</strong> {source}</span>
                </div>
                <p class="why"><em>{explainer}</em></p>
                <p>{summary}</p>
                <a class="readmore" href="{link}" target="_blank" rel="noopener noreferrer" onclick="event.stopPropagation()">Open article ↗</a>
            </article>
            """)

        cards_html = "\n".join(cards)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Fail Watch Archive – {day}</title>
    <style>
        :root {{
            --bg: #0b1020;
            --panel: #121a2b;
            --text: #eaf0fb;
            --muted: #9aa8c7;
            --border: #26324a;
            --accent: #6ea8fe;
            --shadow: 0 12px 30px rgba(0,0,0,0.28);
        }}
        body {{
            margin: 0;
            font-family: Inter, Arial, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.55;
        }}
        .wrap {{
            max-width: 1100px;
            margin: 0 auto;
            padding: 28px 18px 60px;
        }}
        a {{
            color: var(--accent);
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .toplinks {{
            margin-bottom: 20px;
            display: flex;
            gap: 16px;
            flex-wrap: wrap;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 18px;
        }}
        .card {{
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 18px;
            box-shadow: var(--shadow);
            cursor: pointer;
        }}
        .card-top {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            align-items: center;
            margin-bottom: 10px;
        }}
        .rank {{
            color: var(--muted);
            font-size: 0.9rem;
            font-weight: 700;
        }}
        .badge {{
            display: inline-block;
            padding: 5px 10px;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 700;
            border: 1px solid transparent;
        }}
        .lang {{
            background: rgba(255,255,255,0.05);
            color: var(--text);
            border-color: var(--border);
        }}
        .score-big {{
            font-size: 1.02rem;
            font-weight: 800;
            color: #fca5a5;
        }}
        .cat-legal {{ background: rgba(239,68,68,0.14); color: #fecaca; border-color: rgba(239,68,68,0.35); }}
        .cat-security {{ background: rgba(251,146,60,0.14); color: #fed7aa; border-color: rgba(251,146,60,0.35); }}
        .cat-privacy {{ background: rgba(6,182,212,0.14); color: #a5f3fc; border-color: rgba(6,182,212,0.35); }}
        .cat-hallucination {{ background: rgba(236,72,153,0.14); color: #fbcfe8; border-color: rgba(236,72,153,0.35); }}
        .cat-research {{ background: rgba(139,92,246,0.14); color: #ddd6fe; border-color: rgba(139,92,246,0.35); }}
        .cat-education {{ background: rgba(34,197,94,0.14); color: #bbf7d0; border-color: rgba(34,197,94,0.35); }}
        .cat-general {{ background: rgba(110,168,254,0.14); color: #bfdbfe; border-color: rgba(110,168,254,0.35); }}
        .meta {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px 14px;
            color: var(--muted);
            font-size: 0.92rem;
            margin-bottom: 14px;
        }}
        .why {{
            color: #bcd0f5;
        }}
    </style>
</head>
<body>
    <div class="wrap">
        <div class="toplinks">
            <a href="../index.html">← Latest report</a>
            <a href="../archive.html">All archive days</a>
        </div>
        <h1>Archive – {day}</h1>
        <div class="grid">
            {cards_html}
        </div>
    </div>

    <script>
        function openLink(url) {{
            window.open(url, '_blank');
        }}
    </script>
</body>
</html>
"""


def make_trend(items):
    cats = {}
    for i in items:
        cats[i["category"]] = cats.get(i["category"], 0) + 1

    if not cats:
        return ""

    top = max(cats, key=cats.get)
    count = cats[top]

    return f"""
    <div class="trend">
        🔎 Trend today: <strong>{top}</strong> ({count} cases)
    </div>
    """


def make_html(items):
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")
    updated = now.strftime("%Y-%m-%d %H:%M")

    hero_html = ""
    list_html = ""
    trend_html = make_trend(items)

    if items:
        hero_html = make_top_card(items[0])
        remaining = items[1:]
        if remaining:
            list_html = make_cards(remaining)
    else:
        hero_html = """
        <section class="hero-card">
            <div class="hero-label">Daily report</div>
            <h2>No strong AI failure articles found today.</h2>
            <p>Try again later when more source feeds have updated.</p>
        </section>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Fail Watch – {today}</title>
    <style>
        :root {{
            --bg: #0b1020;
            --panel: #121a2b;
            --panel-2: #182235;
            --text: #eaf0fb;
            --muted: #9aa8c7;
            --border: #26324a;
            --accent: #6ea8fe;
            --shadow: 0 12px 30px rgba(0,0,0,0.28);
        }}

        * {{
            box-sizing: border-box;
        }}

        body {{
            margin: 0;
            font-family: Inter, Arial, sans-serif;
            background:
                radial-gradient(circle at top left, rgba(110,168,254,0.10), transparent 35%),
                radial-gradient(circle at top right, rgba(139,92,246,0.10), transparent 30%),
                var(--bg);
            color: var(--text);
            line-height: 1.55;
        }}

        .wrap {{
            max-width: 1100px;
            margin: 0 auto;
            padding: 28px 18px 60px;
        }}

        header {{
            margin-bottom: 26px;
        }}

        .topbar {{
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            gap: 12px;
            align-items: center;
            margin-bottom: 18px;
        }}

        .brand {{
            font-size: 2.1rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            margin: 0;
        }}

        .sub {{
            color: var(--muted);
            font-size: 1rem;
            margin-top: 8px;
        }}

        .status {{
            color: var(--muted);
            font-size: 0.95rem;
            background: rgba(255,255,255,0.04);
            border: 1px solid var(--border);
            border-radius: 999px;
            padding: 8px 12px;
        }}

        .filters {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 18px;
        }}

        .filters button {{
            padding: 8px 14px;
            border-radius: 10px;
            border: 1px solid var(--border);
            background: var(--panel-2);
            color: var(--text);
            cursor: pointer;
            font-weight: 700;
        }}

        .filters button:hover {{
            border-color: var(--accent);
        }}

        .trend {{
            margin-top: 15px;
            color: var(--muted);
            font-size: 0.95rem;
        }}

        .hero-card {{
            background: linear-gradient(180deg, rgba(110,168,254,0.10), rgba(255,255,255,0.02)), var(--panel);
            border: 1px solid rgba(110,168,254,0.3);
            border-radius: 18px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: var(--shadow);
        }}

        .hero-label {{
            display: inline-block;
            font-size: 0.82rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--accent);
            margin-bottom: 12px;
        }}

        h2, h3 {{
            margin: 0 0 12px;
            line-height: 1.25;
        }}

        .hero-card h2 {{
            font-size: 2rem;
        }}

        h3 {{
            font-size: 1.15rem;
        }}

        .meta {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px 14px;
            align-items: center;
            color: var(--muted);
            font-size: 0.92rem;
            margin-bottom: 14px;
        }}

        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 18px;
        }}

        .card {{
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 18px;
            box-shadow: var(--shadow);
            cursor: pointer;
        }}

        .card-top {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            align-items: center;
            margin-bottom: 10px;
        }}

        .rank {{
            color: var(--muted);
            font-size: 0.9rem;
            font-weight: 700;
        }}

        .badge {{
            display: inline-block;
            padding: 5px 10px;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 700;
            border: 1px solid transparent;
        }}

        .lang {{
            background: rgba(255,255,255,0.05);
            color: var(--text);
            border-color: var(--border);
        }}

        .score-big {{
            font-size: 1.02rem;
            font-weight: 800;
            color: #fca5a5;
        }}

        .cat-legal {{ background: rgba(239,68,68,0.14); color: #fecaca; border-color: rgba(239,68,68,0.35); }}
        .cat-security {{ background: rgba(251,146,60,0.14); color: #fed7aa; border-color: rgba(251,146,60,0.35); }}
        .cat-privacy {{ background: rgba(6,182,212,0.14); color: #a5f3fc; border-color: rgba(6,182,212,0.35); }}
        .cat-hallucination {{ background: rgba(236,72,153,0.14); color: #fbcfe8; border-color: rgba(236,72,153,0.35); }}
        .cat-research {{ background: rgba(139,92,246,0.14); color: #ddd6fe; border-color: rgba(139,92,246,0.35); }}
        .cat-education {{ background: rgba(34,197,94,0.14); color: #bbf7d0; border-color: rgba(34,197,94,0.35); }}
        .cat-general {{ background: rgba(110,168,254,0.14); color: #bfdbfe; border-color: rgba(110,168,254,0.35); }}

        p {{
            margin: 0 0 14px;
            color: #dce6f7;
        }}

        .why {{
            color: #bcd0f5;
        }}

        a {{
            color: var(--accent);
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}

        .readmore {{
            font-weight: 700;
        }}

        .section-title {{
            margin: 28px 0 14px;
            font-size: 1.05rem;
            color: var(--muted);
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }}

        footer {{
            margin-top: 32px;
            padding-top: 18px;
            border-top: 1px solid var(--border);
            color: var(--muted);
            font-size: 0.92rem;
        }}

        @media (max-width: 700px) {{
            .brand {{
                font-size: 1.75rem;
            }}

            .hero-card h2 {{
                font-size: 1.4rem;
            }}

            .hero-card,
            .card {{
                padding: 16px;
            }}
        }}
    </style>
</head>
<body>
    <div class="wrap">
        <header>
            <div class="topbar">
                <div>
                    <h1 class="brand">AI Fail Watch</h1>
                    <div class="sub">Daily tracking of leaks, lawsuits, hallucinations, privacy failures and other AI risks.</div>
                </div>
                <div class="status">Last updated: {updated}</div>
            </div>

            <div class="filters">
                <button onclick="filterLang('ALL')">ALL</button>
                <button onclick="filterLang('EN')">EN</button>
                <button onclick="filterLang('FI')">FI</button>
                <button onclick="filterLang('SV')">SV</button>
            </div>

            {trend_html}
        </header>

        {hero_html}

        <div class="section-title">More signals</div>
        <section class="grid">
            {list_html}
        </section>

        <div class="section-title">Archive</div>
        <p><a href="archive.html">Open archive of older reports ↗</a></p>

        <footer>
            Generated automatically from selected RSS feeds.  
            Built to track what goes wrong in AI — not just what gets launched.
        </footer>
    </div>

    <script>
        function filterLang(lang) {{
            const cards = document.querySelectorAll('.card');
            const hero = document.querySelector('.hero-card');

            if (hero) {{
                if (lang === 'ALL' || hero.dataset.lang === lang) {{
                    hero.style.display = 'block';
                }} else {{
                    hero.style.display = 'none';
                }}
            }}

            cards.forEach(card => {{
                if (lang === 'ALL' || card.dataset.lang === lang) {{
                    card.style.display = 'block';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}

        function openLink(url) {{
            window.open(url, '_blank');
        }}
    </script>
</body>
</html>
"""


def main():
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")

    items = fetch_entries()

    latest_items = items[:10]
    archive_items = items[10:]

    md_output = make_markdown(latest_items)
    html_output = make_html(latest_items)

    Path("data").mkdir(exist_ok=True)
    Path("archive").mkdir(exist_ok=True)

    Path("data/latest.md").write_text(md_output, encoding="utf-8")
    Path("index.html").write_text(html_output, encoding="utf-8")

    archive_day_html = make_archive_page(archive_items, today)
    Path(f"archive/{today}.html").write_text(archive_day_html, encoding="utf-8")

    archive_index_html = make_archive_index()
    Path("archive.html").write_text(archive_index_html, encoding="utf-8")

    print("Done. Wrote data/latest.md, index.html, archive.html and daily archive page")


if __name__ == "__main__":
    main()