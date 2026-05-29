def build_prompt(name: str, professional_focus: str, matched_session: str) -> str:
    return f"""
You are a professional B2B email writer.

Write a polished invitation email for:
- Name: {name}
- Professional focus: {professional_focus}
- Matched session: {matched_session}

Rules:
- Use only the matched session information.
- Do not invent fake topics, times, or speakers.
- Keep the tone professional and concise.
- Do not mention anything that is not grounded in the given session.
"""