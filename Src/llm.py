from google import genai
import os


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_answer(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents=prompt,
    )

    return response.text