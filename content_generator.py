from groq import Groq
import json
import os
from dotenv import load_dotenv
from prompt_builder import build_prompt

# Force load .env from the same folder as this file
dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(dotenv_path=dotenv_path)

api_key = os.getenv("GROQ_API_KEY")
print(f"Loaded from: {dotenv_path}")
print(f"API Key: {api_key[:15] if api_key else 'NOT FOUND'}")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file!")

client = Groq(api_key=api_key)

def generate_content(user_profile: dict, topic_analysis: dict, attempt: int = 1) -> dict:
    prompt = build_prompt(user_profile, topic_analysis)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are an educational content generator. Always respond in valid JSON only. No markdown, no extra text."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    raw_text = response.choices[0].message.content.strip()

    if raw_text.startswith("```"):
        raw_text = raw_text.split("```")[1]
        if raw_text.startswith("json"):
            raw_text = raw_text[4:]
    raw_text = raw_text.strip()

    content = json.loads(raw_text)
    return content