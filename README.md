# Primary Care GPT Agent

This project simulates a primary care consultation using a GPT-4o-powered agent. It guides patients through symptom intake, assessment, recommendation, and follow-up while ensuring safe escalation for emergency symptoms. The system runs entirely in the terminal and maintains an in-memory session transcript.

## Features

-   Empathetic, structured language based on system prompt rules
-   Differentiates between mild and emergency symptoms
-   Responds with 3-step self-care plans or urgent escalation
-   Handles unclear or gibberish input gracefully
-   Saves full transcripts to a local folder

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/primary-care-agent.git
cd primary-care-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your API key

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your-api-key-here
```

### 4. Run the agent

```bash
python primary_care_agent.py
```

### 5. Example session

The agent will greet you and begin asking about your symptoms. Type `exit` to end the session. A `.txt` transcript will be saved in the `conversations/` folder.

## File Overview

| File / Folder           | Description                                                 |
| ----------------------- | ----------------------------------------------------------- |
| `primary_care_agent.py` | Main CLI script to interact with the GPT agent              |
| `gpt_system_prompt.txt` | System prompt defining empathy, structure, and escalation   |
| `documents/`            | System design doc, validation plan, and reflection          |
| `transcripts/`          | 2 sample conversations (one mild, one emergency)            |
| `conversations/`        | Auto-generated folder that stores transcripts from sessions |
| `requirements.txt`      | Python dependencies (`openai`, `python-dotenv`)             |

## Technologies

-   Python 3.10+
-   GPT-4o via OpenAI API
