import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


system_prompt = "You are a helpful yet friendly AI primary care agent"
user_input = "I've been feeling tired late, what should I do?"

try:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0.5
    )

    reply = response.choices[0].message.content
    print("\n AI primary care agent response: ")
    print(reply)

except Exception as e:
    print(f"Error communicating with OpenAI API: {e}")
