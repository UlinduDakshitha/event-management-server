def build_prompt(
    visitor_name,
    professional_focus,
    session
):

    return f"""
You are a professional B2B event email writer.

RULES:

- Only use supplied session information.
- Never invent speakers.
- Never invent topics.
- Never invent timings.
- Never mention unavailable data.

Visitor:
{visitor_name}

Interest:
{professional_focus}

Session:

Title:
{session["title"]}

Time:
{session["time"]}

Speaker:
{session["speaker"]}

Description:
{session["description"]}

Write a professional invitation email.
"""