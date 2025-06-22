import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

with open("gpt_system_prompt.txt", "r") as f:
    system_prompt = f.read()


def run_agent(user_input):
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
        return reply

    except Exception as e:
        print(f"Error communicating with OpenAI API: {e}")


if __name__ == "__main__":
    print("Primary Care Agent (Type 'exit' to quit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    reply = run_agent(user_input)
    print(f"Agent: {reply} ")
