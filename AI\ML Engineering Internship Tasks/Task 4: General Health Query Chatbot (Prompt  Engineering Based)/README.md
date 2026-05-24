# General Health Query Chatbot
### Internship Project — Task 4

---

## Project Overview

A Python-based conversational chatbot that answers general health questions
using OpenAI's GPT-3.5 Turbo API. The project demonstrates:

- **Prompt Engineering** — crafting a safe, friendly medical assistant persona
- **LLM API Integration** — using OpenAI's Python SDK
- **Safety Filtering** — multi-layer protection against harmful responses
- **Conversational Memory** — maintaining chat history across turns

---

## Setup Instructions

### Step 1 — Install Python
Make sure Python 3.8 or higher is installed.
Download from: https://www.python.org/downloads/

### Step 2 — Install Dependencies
```
pip install -r requirements.txt
```

### Step 3 — Get Your OpenAI API Key
1. Go to https://platform.openai.com/api-keys
2. Create a new secret key
3. Copy it (starts with sk-...)

### Step 4 — Set Your API Key

Option A — Edit the script directly:
Open health_chatbot.py and replace "your-api-key-here" with your actual key.

Option B — Environment variable (recommended):

Windows:
  set OPENAI_API_KEY=sk-your-key-here

Linux/Mac:
  export OPENAI_API_KEY=sk-your-key-here

### Step 5 — Run the Chatbot
```
python health_chatbot.py
```

---

## How to Use

Once running, type your health question and press Enter:

  You: What causes a sore throat?
  You: Is paracetamol safe for children?
  You: How can I improve my sleep?

Special commands:
  history  — view conversation history
  clear    — start a new conversation
  exit     — quit the program

---

## Safety Layers

| Layer | Type              | What it does                                              |
|-------|-------------------|-----------------------------------------------------------|
| 1     | Emergency filter  | Detects keywords like "chest pain", goes to emergency SOS |
| 2     | Harmful filter    | Blocks dangerous queries before calling the API           |
| 3     | LLM-level safety  | System prompt keeps the model within safe boundaries      |
| 4     | Sensitive reminder| Appends "consult a doctor" to personal symptom queries    |

---

## API Configuration

- Model       : gpt-3.5-turbo
- Temperature : 0.5  (balanced accuracy + natural tone)
- Max tokens  : 500  (concise responses)
- Memory      : Last 10 conversation turns sent per request

