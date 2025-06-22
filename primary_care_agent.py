import os
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

with open("gpt_system_prompt.txt", "r") as f:
    system_prompt = f.read()

os.makedirs("conversations", exist_ok=True)

messages = [{"role": "system", "content": system_prompt}]

transcript = []


def run_agent(user_input):
    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.5
        )

        reply = response.choices[0].message.content

        messages.append({"role": "assistant", "content": reply})

        return reply

    except Exception as e:
        print(f"Error communicating with OpenAI API: {e}")


if __name__ == "__main__":
    print("Primary Care Agent (Type 'exit' to quit)\n")
    opening = "Hi, can you describe the symptoms that brought you in today?"
    print(f"Agent: {opening}")
    transcript.append(f"Agent: {opening}")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        reply = run_agent(user_input)
        print(f"\nAgent: {reply}\n")

        transcript.append(f"You: {user_input}")
        transcript.append(f"Agent: {reply}")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"conversations/conversation_{timestamp}.txt"

    with open(filename, "w") as f:
        f.write("\n\n".join(transcript))

    print(f"\n Conversation saved to {filename}")
