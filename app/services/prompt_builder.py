def build_prompt(name: str, professional_focus: str, matched_session: dict) -> str:
    return f"""
Write a professional B2B invitation email.

Visitor Name: {name}
Visitor Focus: {professional_focus}

Matched Session:
- Session ID: {matched_session["id"]}
- Time: {matched_session["time"]}
- Title: {matched_session["title"]}
- Speaker: {matched_session["speaker"]}
- Keywords: {", ".join(matched_session["keywords"])}
- Description: {matched_session["description"]}

Rules:
- Use only the matched session facts above.
- Do not invent any new speakers, times, topics, or agenda items.
- Keep the tone professional, concise, and persuasive.
- Make the email sound personalized to the visitor's focus.
"""