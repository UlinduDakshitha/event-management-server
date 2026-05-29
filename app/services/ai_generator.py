import os
from openai import OpenAI

def generate_email_draft(prompt: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set")

    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model="gpt-5.5",
        input=prompt
    )
    return response.output_text