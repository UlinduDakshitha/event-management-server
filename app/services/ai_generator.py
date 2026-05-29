from openai import OpenAI

from app.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_email_draft(prompt: str) -> str:
    response = client.responses.create(
        model="gpt-5.5",
        instructions=(
            "You are a professional B2B invitation email writer. "
            "Use only the provided agenda information. "
            "Do not invent speakers, times, topics, or session details."
        ),
        input=prompt,
    )

    return response.output_text