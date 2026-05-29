def build_invitation_prompt(visitor_name: str, professional_focus: str, matched_session: dict) -> str:
    return f"""
You are a professional B2B event email writer.

Write a concise, polished invitation email for:
Visitor Name: {visitor_name}
Visitor Interest: {professional_focus}

Rules:
- Use ONLY the session information provided below.
- Do NOT invent or change speakers, times, titles, or topics.
- Do NOT mention any session not provided here.
- If something is missing, do not guess.

Session Information:
- Time: {matched_session.get("time", "N/A")}
- Title: {matched_session.get("title", "N/A")}
- Speaker: {matched_session.get("speaker", "N/A")}
- Description: {matched_session.get("description", "N/A")}

Return only the email body.
"""