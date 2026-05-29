def generate_email(prompt: str) -> str:
    return f"""Dear Visitor,

Thank you for your interest in our event.

Based on your profile, we recommend the most relevant session in the agenda.

Best regards,
Event Team
"""


def generate_email_draft(prompt: str) -> str:
    return generate_email(prompt)