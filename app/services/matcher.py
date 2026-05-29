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