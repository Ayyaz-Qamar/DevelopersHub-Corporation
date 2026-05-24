"""
=============================================================
  General Health Query Chatbot
  Internship Project - Task 4
  Tool: OpenAI GPT-3.5 Turbo API
  Features: Prompt Engineering + Safety Filters + Chat Memory
=============================================================
"""

import os
from openai import OpenAI

# ─────────────────────────────────────────────
#  1. CONFIGURATION
# ─────────────────────────────────────────────

# Put your OpenAI API key here OR set as environment variable:
#   Windows:  set OPENAI_API_KEY=sk-...
#   Linux/Mac: export OPENAI_API_KEY=sk-...
API_KEY = os.getenv("OPENAI_API_KEY", "your-api-key-here")

client = OpenAI(api_key=API_KEY)

# ─────────────────────────────────────────────
#  2. PROMPT ENGINEERING — System Prompt
# ─────────────────────────────────────────────

SYSTEM_PROMPT = """
You are a friendly, knowledgeable, and caring general health information assistant.

Your responsibilities:
- Provide clear, accurate, and easy-to-understand general health information
- Use a warm, empathetic, and non-alarmist tone at all times
- Explain medical terms in simple everyday language
- Keep responses concise (3-6 sentences usually), well-structured, and readable

STRICT SAFETY RULES you must ALWAYS follow:
1. NEVER diagnose any medical condition for the user
2. NEVER prescribe specific medications or dosages for a user's personal case
3. NEVER advise someone to stop taking prescribed medications
4. NEVER contradict established medical consensus or promote misinformation
5. ALWAYS recommend consulting a qualified doctor or healthcare professional
   when someone asks about personal symptoms or treatments
6. If someone mentions emergency symptoms (chest pain, stroke, severe bleeding,
   difficulty breathing, loss of consciousness), IMMEDIATELY tell them to call
   emergency services and do NOT answer the health question first
7. If someone shows signs of mental health crisis or mentions self-harm,
   respond with empathy, provide crisis helpline information, and encourage
   them to seek professional help immediately

Always end responses that involve personal symptoms or treatments with:
"⚕️ Please consult a qualified healthcare professional for advice specific to your situation."
"""

# ─────────────────────────────────────────────
#  3. SAFETY FILTERS (Client-Side)
# ─────────────────────────────────────────────

# Trigger immediate emergency response — no API call made
EMERGENCY_KEYWORDS = [
    "chest pain", "heart attack", "cant breathe", "can't breathe",
    "difficulty breathing", "stroke symptoms", "unconscious", "not breathing",
    "severe bleeding", "choking", "overdose", "poisoning", "seizure",
]

# Blocked topics — chatbot refuses to answer
HARMFUL_KEYWORDS = [
    "how to fake illness", "how to get drugs", "how to overdose",
    "lethal dose", "how to hurt myself", "how to harm", "how to poison",
]

# Topics that always get a "consult a doctor" reminder appended
SENSITIVE_KEYWORDS = [
    "my symptoms", "i have", "i feel", "i am experiencing", "should i take",
    "can i take", "my child has", "my baby", "am i pregnant", "is it cancer",
]


def check_emergency(text: str) -> bool:
    """Returns True if query contains emergency medical keywords."""
    lower = text.lower()
    return any(kw in lower for kw in EMERGENCY_KEYWORDS)


def check_harmful(text: str) -> bool:
    """Returns True if query matches harmful/blocked patterns."""
    lower = text.lower()
    return any(kw in lower for kw in HARMFUL_KEYWORDS)


def check_sensitive(text: str) -> bool:
    """Returns True if query is about personal symptoms (needs doctor reminder)."""
    lower = text.lower()
    return any(kw in lower for kw in SENSITIVE_KEYWORDS)


# ─────────────────────────────────────────────
#  4. CHATBOT CORE FUNCTIONS
# ─────────────────────────────────────────────

def get_emergency_response() -> str:
    return (
        "\n🚨 EMERGENCY ALERT 🚨\n"
        "This sounds like a medical emergency!\n"
        "Please call emergency services IMMEDIATELY:\n"
        "  • Pakistan: 115 (Rescue) / 1122 (Emergency)\n"
        "  • Or go to the nearest hospital Emergency Room\n"
        "Do NOT wait. Your safety comes first.\n"
    )


def get_harmful_response() -> str:
    return (
        "I'm sorry, but I'm unable to provide information on that topic.\n"
        "If you're going through a difficult time, please reach out:\n"
        "  • Umang helpline (Pakistan): 0317-4288665\n"
        "  • Or speak to a trusted doctor or counselor.\n"
        "You are not alone. 💙\n"
    )


def ask_llm(user_message: str, chat_history: list) -> str:
    """
    Sends the user message + full conversation history to GPT-3.5.
    Returns the assistant's reply as a string.
    """
    # Build messages list: system prompt + full history + new user message
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(chat_history)
    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5,       # Balanced: accurate but natural-sounding
        max_tokens=500,        # Keep responses concise
        top_p=0.9,
    )

    return response.choices[0].message.content.strip()


def process_query(user_input: str, chat_history: list) -> tuple[str, list]:
    """
    Main pipeline:
    1. Safety check (emergency / harmful)
    2. Call LLM if safe
    3. Append reminder if sensitive topic
    4. Update and return conversation history
    """
    user_input = user_input.strip()

    # Layer 1: Emergency filter
    if check_emergency(user_input):
        reply = get_emergency_response()
        # Still log to history but mark it
        chat_history.append({"role": "user", "content": user_input})
        chat_history.append({"role": "assistant", "content": reply})
        return reply, chat_history

    # Layer 2: Harmful content filter
    if check_harmful(user_input):
        reply = get_harmful_response()
        chat_history.append({"role": "user", "content": user_input})
        chat_history.append({"role": "assistant", "content": reply})
        return reply, chat_history

    # Layer 3: Call the LLM
    try:
        reply = ask_llm(user_input, chat_history)
    except Exception as e:
        reply = f"Sorry, there was an error connecting to the health assistant: {e}\nPlease check your API key and internet connection."
        return reply, chat_history

    # Layer 4: Append extra reminder for personal/sensitive queries
    if check_sensitive(user_input):
        if "⚕️" not in reply:  # Avoid duplicate reminder
            reply += "\n\n⚕️ Please consult a qualified healthcare professional for advice specific to your situation."

    # Update conversation history (keep last 10 turns to save tokens)
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "assistant", "content": reply})
    if len(chat_history) > 20:
        chat_history = chat_history[-20:]  # Keep last 10 user+assistant pairs

    return reply, chat_history


# ─────────────────────────────────────────────
#  5. MAIN CHAT LOOP
# ─────────────────────────────────────────────

def print_banner():
    print("=" * 60)
    print("       🩺  General Health Query Chatbot  🩺")
    print("       Powered by OpenAI GPT-3.5 Turbo")
    print("=" * 60)
    print("  ⚠️  DISCLAIMER: This chatbot provides general health")
    print("  information only. It is NOT a substitute for professional")
    print("  medical advice, diagnosis, or treatment.")
    print("=" * 60)
    print("  Type 'quit' or 'exit' to end the session.")
    print("  Type 'history' to see conversation history.")
    print("  Type 'clear' to start a new conversation.")
    print("=" * 60)
    print()


def print_example_queries():
    print("💡 Example questions you can ask:")
    examples = [
        "What causes a sore throat?",
        "Is paracetamol safe for children?",
        "How can I improve my sleep?",
        "What are the symptoms of diabetes?",
        "What foods are good for heart health?",
        "How does the immune system fight infections?",
        "What is the difference between a cold and the flu?",
        "How much water should I drink daily?",
    ]
    for i, q in enumerate(examples, 1):
        print(f"  {i}. {q}")
    print()


def run_chatbot():
    """Main function — runs the interactive chat loop."""
    print_banner()
    print_example_queries()

    chat_history = []

    print("Assistant: Hello! I'm your General Health Information Assistant.")
    print("           I can answer general health questions in a clear,")
    print("           friendly way. How can I help you today?\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nAssistant: Take care and stay healthy! Goodbye! 👋")
            break

        if not user_input:
            continue

        # Special commands
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("\nAssistant: Thank you for using the Health Assistant. Stay healthy! 👋")
            break

        if user_input.lower() == "clear":
            chat_history = []
            print("\nAssistant: Conversation cleared. Starting fresh! How can I help you?\n")
            continue

        if user_input.lower() == "history":
            if not chat_history:
                print("\n[No conversation history yet]\n")
            else:
                print("\n--- Conversation History ---")
                for msg in chat_history:
                    role = "You" if msg["role"] == "user" else "Assistant"
                    print(f"{role}: {msg['content'][:120]}{'...' if len(msg['content']) > 120 else ''}")
                print("----------------------------\n")
            continue

        # Process the health query
        print("\nAssistant: ", end="", flush=True)
        reply, chat_history = process_query(user_input, chat_history)
        print(reply)
        print()


# ─────────────────────────────────────────────
#  6. ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    run_chatbot()
