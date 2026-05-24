# 🧠 Task 5 — Mental Health Support Chatbot
**DevelopersHub Corporation | AI/ML Engineering Internship**

---

## 📌 Objective
Build a chatbot that provides **supportive and empathetic responses** for people experiencing stress, anxiety, and emotional difficulties — using a fine-tuned language model.

---

## 📦 Dataset
**EmpatheticDialogues** by Facebook AI
- 25,000+ real human conversations
- 32 different emotion categories (sad, anxious, angry, joyful, lonely, etc.)
- Source: [HuggingFace — empathetic_dialogues](https://huggingface.co/datasets/empathetic_dialogues)

---

## 🤖 Model
**DistilGPT2** — a lightweight distilled version of GPT-2, fine-tuned for empathetic conversation.

---

## ⚙️ What Was Done

1. Loaded and explored the EmpatheticDialogues dataset (EDA — emotion distribution, utterance lengths)
2. Formatted prompts with emotion context:
   ```
   Emotion: sad
   User: I feel so alone lately.
   Bot: I understand how you feel.
   ```
3. Fine-tuned DistilGPT2 using Hugging Face `Trainer` API (3 epochs, lr=5e-5)
4. Built keyword-based emotion detector from user input
5. Added **safety filters** — detects harmful keywords and redirects to crisis resources
6. Built interactive command-line chatbot interface

---

## 📊 Key Results

| Metric | Value |
|--------|-------|
| Epochs | 3 |
| Batch Size | 8 |
| Training Samples | 5,000 |
| Perplexity (after fine-tuning) | Decreased from baseline |
| Safety Filter | ✅ Active |

- Fine-tuning on emotional dialogues shifted the model tone to be warmer and more empathetic
- Safety filters successfully intercept harmful inputs and return crisis resources (988 Lifeline)
- Emotion-conditioned prompts helped guide response tone effectively

---

## 🛡️ Safety Features
- Detects keywords like "hurt yourself", "self-harm", etc.
- Returns crisis message with **988 Suicide & Crisis Lifeline**
- Never encourages harmful behavior

---

## 🚀 How to Run

1. Open `Task5_Mental_Health_Chatbot.ipynb` in **Google Colab**
2. Enable GPU: *Runtime → Change runtime type → T4 GPU*
3. Run all cells in order
4. Interact with the chatbot in the last cell

### Dependencies
```
transformers
datasets
accelerate
torch
pandas
matplotlib
seaborn
```
> All install automatically in the notebook.

---

## 📂 File
```
Task5_Mental_Health_Chatbot.ipynb
```
