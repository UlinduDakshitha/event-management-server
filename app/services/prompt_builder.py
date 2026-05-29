def build_prompt(name: str, professional_focus: str, matched_session: str) -> str:
    return f"""
Write a professional B2B invitation email.

Visitor Name: {name}
Visitor Focus: {professional_focus}
Matched Session: {matched_session}

Rules:
- Use only the matched session details.
- Do not invent fake topics, times, speakers, or agenda items.
- Keep it concise, polished, and corporate.
- The email must sound personalized and relevant.
"""