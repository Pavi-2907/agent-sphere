from groq import Groq

from backend.app.core.config import GROQ_API_KEY


client = Groq(api_key=GROQ_API_KEY)


def generate_response(question: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI career guidance assistant. "
                    "Provide clear, practical, and structured advice "
                    "for users who want to build careers in AI and software engineering."
                ),
            },
            {
                "role": "user",
                "content": question,
            },
        ],
    )

    return response.choices[0].message.content