
import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

# Locate the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_ROOT / ".env"

# Load environment variables
load_dotenv(ENV_FILE, override=True)

SYSTEM_PROMPT = """
You are an AI Career Guidance Assistant for a Student Placement Portal.

Help students with:
1. Python, SQL, and DSA learning.
2. Resume and project improvement.
3. Aptitude and interview preparation.
4. Communication and soft skills.
5. Career planning and placement readiness.
6. Technical and HR interview preparation.

Give practical, beginner-friendly answers in simple English.
Never guarantee a placement or salary.
Never invent a student's placement prediction.
"""


def get_chatbot_response(messages):
    # Read the key using its environment variable name
    api_key = os.getenv("GROQ_API_KEY")
    model_name = os.getenv(
        "GROQ_MODEL",
        "openai/gpt-oss-20b"
    )

    if not api_key:
        raise ValueError(
            f"GROQ_API_KEY is missing. Check: {ENV_FILE}"
        )

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            *messages[-12:]
        ],
        temperature=0.5,
        max_completion_tokens=800
    )

    return response.choices[0].message.content
