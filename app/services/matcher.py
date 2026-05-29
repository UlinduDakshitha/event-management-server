from typing import Any


DEFAULT_SESSIONS: list[dict[str, Any]] = [
    {
        "id": "SESSION_5",
        "title": "The Resilient Supply Chain & SCM Innovations",
        "description": "AI, automation, and predictive approaches for supply chain resilience.",
        "keywords": ["ai", "automation", "predictive", "supply chain", "scm"],
    },
    {
        "id": "SESSION_3",
        "title": "Industry Keynote",
        "description": "Outlook and challenges on digital logistics and supply chain.",
        "keywords": ["logistics", "digital", "transportation", "supply chain"],
    },
    {
        "id": "SESSION_4",
        "title": "A Practical Guide to Successful Implementation",
        "description": "Implementation, integration, and deployment guidance.",
        "keywords": ["implementation", "integration", "deployment"],
    },
    {
        "id": "SESSION_8",
        "title": "Strategies in Action: Insights from Industry Leaders",
        "description": "Leadership, panel, and case study perspectives.",
        "keywords": ["leadership", "panel", "case study"],
    },
    {
        "id": "SESSION_7",
        "title": "Insights from Digital Evolution",
        "description": "Broad digital transformation themes and trends.",
        "keywords": ["digital", "evolution", "transformation"],
    },
]


def score_session(user_text: str, session: dict) -> int:
    text = user_text.lower()
    score = 0

    title = session.get("title", "").lower()
    description = session.get("description", "").lower()
    keywords = session.get("keywords", [])

    for keyword in keywords:
        if keyword in text:
            score += 3

    if any(word in text for word in title.split()):
        score += 2

    if any(word in text for word in description.split()):
        score += 1

    return score


def find_best_session(user_text: str, sessions: list[dict[str, Any]] | None = None):
    sessions = sessions or DEFAULT_SESSIONS
    best_session = None
    best_score = -1

    for session in sessions:
        score = score_session(user_text, session)
        if score > best_score:
            best_score = score
            best_session = session

    return best_session, best_score