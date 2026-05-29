def build_invitation_prompt(visitor_name: str, professional_focus: str, matched_session: dict) -> str:
    return f"""
You are a professional B2B event email writer.

Write a short, polished invitation email for:
- Visitor Name: {visitor_name}
- Visitor Interest: {professional_focus}

Use ONLY the session details below.
Do NOT invent or add any information that is not in the session data.
Do NOT hallucinate speakers, times, topics, or claims.
Do NOT mention sessions other than the matched one.

Matched Session Data:
- Time: {matched_session.get("time", "N/A")}
- Title: {matched_session.get("title", "N/A")}
- Speaker: {matched_session.get("speaker", "N/A")}
- Description: {matched_session.get("description", "N/A")}

Write in a professional, warm, B2B conference invitation style.
Keep it concise and persuasive.
"""