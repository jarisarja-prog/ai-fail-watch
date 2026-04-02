AI_KEYWORDS = [
    "artificial intelligence",
    "generative ai",
    "machine learning",
    "llm",
    "large language model",
    "chatbot",
    "chatgpt",
    "openai",
    "anthropic",
    "claude",
    "gemini",
    "meta ai",
    "ai agent",
    "ai system",
    "ai tool",
    "künstliche intelligenz",
    "artificiell intelligens",
    "ai-system",
    "ai-verktyg",
    "ai-modell",
    "chatbot",
    
]

WEAK_AI_KEYWORDS = [
    " ai ",
    "ai-",
    " ai,",
    " ai.",
    " ai-powered",
    "ki",
]

FAIL_KEYWORDS = [
    "failed",
    "failure",
    "error",
    "errors",
    "flawed",
    "hallucination",
    "hallucinations",
    "hallucinated",
    "fake",
    "fabricated",
    "retracted",
    "retraction",
    "withdrawn",
    "backlash",
    "criticism",
    "criticized",
    "bias",
    "biased",
    "unsafe",
    "misleading",
    "unreliable",
    "lawsuit",
    "sue",
    "suing",
    "scandal",
    "fraud",
    "bug",
    "bugs",
    "harm",
    "risk",
    "risks",
    "leak",
    "leaked",
    "security",
    "delusion",
    "delusions",
    "wrecked",
    "complaint",
    "copyright",
    "violate",
    "violated",
    "breach",
    "breached",
    "takedown",
    "danger",
    "dangerous",
    "privacy",
    "surveillance",
    "unmask",
    "unmasking",
    "expose",
    "exposed",
    "gescheitert",
    "fehler",
    "kritik",
    "halluzination",
    # 🇸🇪 RUOTSI
"fel",
"problem",
"problematiskt",
"kritik",
"kritiskt",
"risk",
"risker",
"fara",
"farlig",
"skandal",
"stämning",
"stämmer",
"läcka",
"läckte",
"läckta",
"misslyckades",
"misslyckande",
"brist",
"brister",
"brott",
"integritet",
"övervakning",
# 🇫🇮 SUOMI
"virhe",
"virheet",
"ongelma",
"ongelmat",
"epäonnistui",
"epäonnistuminen",
"kritiikki",
"riski",
"riskit",
"vaara",
"vaarallinen",
"skandaali",
"kanne",
"oikeusjuttu",
"vuoto",
"vuoti",
"vuotanut",
"tietovuoto",
"tietoturva",
"tietosuoja",
"yksityisyys",
"valvonta",
"harhaanjohtava",
"luotettavuus",
"petos",
"huijaus",
]

STRONG_FAIL_KEYWORDS = [
    "hallucination",
    "hallucinations",
    "hallucinated",
    "fake",
    "fabricated",
    "retracted",
    "retraction",
    "withdrawn",
    "fraud",
    "lawsuit",
    "scandal",
    "unsafe",
    "unreliable",
    "leak",
    "leaked",
    "security",
    "breach",
    "breached",
    "delusion",
    "delusions",
    "wrecked",
    "violated",
    "takedown",
    "privacy",
    "surveillance",
    "unmask",
    "halluzination",
    "läcka",
    "läckte",
    "skandal",
    "stämning",
    "integritet",
    "övervakning",
    # 🇫🇮 SUOMI
"vuoto",
"tietovuoto",
"oikeusjuttu",
"skandaali",
"petos",
"tietosuoja",
"yksityisyys",
"valvonta",
]

LOW_VALUE_PATTERNS = [
    "commentisfree",
    "| letters",
    " letters",
    "opinion",
    "editorial",
    "review",
    "tv and radio",
]

OFF_TOPIC_PATTERNS = [
    "tv series",
    "sitcom",
    "celebrity",
    "radio show",
]

FIRST_PERSON_REVIEW_PATTERNS = [
    "i wore ",
    "i tried ",
    "i tested ",
    "for a month",
    "feeling like a creep",
]

RESEARCH_PATTERNS = [
    "citation",
    "citations",
    "reference",
    "references",
    "paper",
    "papers",
    "research",
    "scientific",
    "science",
    "study",
    "studies",
    "journal",
    "academic",
    "academia",
]


def score_entry(text: str) -> int:
    text = (text or "").lower()

    strong_ai_hits = sum(1 for w in AI_KEYWORDS if w in text)
    weak_ai_hits = sum(1 for w in WEAK_AI_KEYWORDS if w in text)
    fail_hits = sum(1 for w in FAIL_KEYWORDS if w in text)
    strong_fail_hits = sum(1 for w in STRONG_FAIL_KEYWORDS if w in text)
    research_hits = sum(1 for w in RESEARCH_PATTERNS if w in text)

    # vaadi oikea AI-osuma (ei pelkkä "ai" sivulauseessa)
    if strong_ai_hits == 0:
        return 0

    if fail_hits == 0:
     return 0

    score = (
        strong_ai_hits * 4
        + weak_ai_hits * 1
        + fail_hits * 3
        + strong_fail_hits * 5
        + research_hits * 2
    )

    for pattern in LOW_VALUE_PATTERNS:
        if pattern in text:
            score -= 8

    for pattern in OFF_TOPIC_PATTERNS:
        if pattern in text:
            score -= 8

    for pattern in FIRST_PERSON_REVIEW_PATTERNS:
        if pattern in text:
            score -= 12

    return max(score, 0)


def is_low_value_entry(title: str, summary: str, link: str, source: str) -> bool:
    combined = " ".join([
        title or "",
        summary or "",
        link or "",
        source or "",
    ]).lower()

    bad_patterns = [
        "commentisfree",
        "| letters",
        " letters",
        "opinion",
        "editorial",
        "review",
        "tv and radio",
        "i wore ",
        "i tried ",
        "i tested ",
        "for a month",
        "feeling like a creep",
    ]

    return any(p in combined for p in bad_patterns)