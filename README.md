# Personalized-Learning
# Personalized Learning — AI Content Generation Module

An intelligent system that generates personalized explanations of complex topics based on a user's reading level, educational background, and interests.

## Project Overview

This is a group project split across four modules:

| Module | Owner |
|--------|-------|
| Frontend (UI/UX) | Team Member 01|
| Backend & Database (FastAPI + PostgreSQL) | Team Member 02 |
| NLP & Topic Analysis (spaCy) | Team Member 03 |
| **AI Content Generation (LLM)** | **Dilawer Khan** |

---

## Dilawer's Module — AI Content Generation

This module takes a user profile and topic analysis as input, then uses an LLM to generate a personalized, readable explanation of the topic.

### Files

```
├── dilawer_module.py        # Main entry point
├── content_generator.py     # Calls Groq LLM API
├── prompt_builder.py        # Builds dynamic prompts
├── vocabulary_control.py    # Simplifies complex words
├── analogy_system.py        # Interest-based analogies
├── regeneration_handler.py  # Handles readability mismatch
├── test_dilawer.py          # Local testing
├── .env.example             # Environment variable template
```

### Setup

1. Clone the repo
```bash
git clone https://github.com/Dilawer-Khan-Niazi/Personalized-Learning.git
cd Personalized-Learning
```

2. Install dependencies
```bash
pip install groq python-dotenv
```

3. Create your `.env` file
```bash
cp .env.example .env
```
Then open `.env` and add your Groq API key. Get one free at https://console.groq.com

```
GROQ_API_KEY=your_groq_api_key_here
```

4. Run the test
```bash
python test_dilawer.py
```

### Sample Output

```json
{
  "title": "Quantum Entanglement Made Simple",
  "introduction": "Imagine two footballs connected in a way that...",
  "main_explanation": "In the quantum world, tiny particles...",
  "analogy": "Think of it like playing a video game with a friend...",
  "summary": "Quantum entanglement is a phenomenon where...",
  "difficulty_level": "Beginner"
}
```

### Integration (For Paras)

Import and call the main function from your FastAPI route:

```python
from dilawer_module import run_content_generation

result = run_content_generation(user_profile, topic_analysis)
```

**Input format:**
```python
user_profile = {
    "reading_level": "Beginner",       # Beginner / Intermediate / Advanced
    "education_level": "School",        # School / Undergraduate / Graduate
    "interests": ["Football", "Gaming"]
}

topic_analysis = {
    "topic": "Quantum Entanglement",
    "core_concepts": ["quantum states", "entanglement"],
    "complexity_score": 8.5,
    "technical_terms": ["wave function"]
}
```

**Output:** JSON with keys — `title`, `introduction`, `main_explanation`, `analogy`, `summary`, `difficulty_level`
