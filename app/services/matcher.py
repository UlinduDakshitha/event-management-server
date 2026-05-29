from typing import Optional, Dict


def find_best_session(professional_focus: str) -> Optional[Dict]:
    """Return a simple best-match session dict based on `professional_focus` text.

    This is a lightweight placeholder matcher: it checks for keywords in a
    small static sessions list and returns the first reasonable match.
    """
    if not professional_focus:
        return None

    query = professional_focus.lower()

    sessions = [
        {"title": "AI in Healthcare", "tags": ["ai", "healthcare", "ml"]},
        {"title": "Modern Web Development", "tags": ["web", "javascript", "frontend", "backend"]},
        {"title": "Data Engineering", "tags": ["data", "etl", "pipeline"]},
    ]

    # direct tag match
    for s in sessions:
        for tag in s["tags"]:
            if tag in query:
                return s

    # title word match
    for s in sessions:
        for word in s["title"].lower().split():
            if word in query:
                return s

    # fallback: return the first session
    return sessions[0]
def find_best_session(user_text: str) -> str:
    text = user_text.lower()

    if "ai" in text or "automation" in text or "predictive" in text:
        return "SESSION_5 - The Resilient Supply Chain & SCM Innovations"

    if "logistics" in text or "digital" in text or "transportation" in text:
        return "SESSION_3 - Industry Keynote (Outlook & Challenges on Digital Logistics & Supply Chain)"

    if "implementation" in text or "integration" in text or "deployment" in text:
        return "SESSION_4 - A Practical Guide to Successful Implementation"

    if "leadership" in text or "panel" in text or "case study" in text:
        return "SESSION_8 - Strategies in Action: Insights from Industry Leaders"

    return "SESSION_7 - Insights from Digital Evolution"