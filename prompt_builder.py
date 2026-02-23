def build_prompt(user_profile: dict, topic_analysis: dict) -> str:
    topic = topic_analysis["topic"]
    reading_level = user_profile["reading_level"]        # Beginner / Intermediate / Advanced
    education = user_profile["education_level"]          # School / Undergraduate / Graduate
    interests = ", ".join(user_profile["interests"])     # e.g. Football, Gaming
    core_concepts = ", ".join(topic_analysis["core_concepts"])
    technical_terms = ", ".join(topic_analysis["technical_terms"])

    # Adjust word count based on reading level
    word_count = {"Beginner": 200, "Intermediate": 350, "Advanced": 500}.get(reading_level, 300)

    prompt = f"""
You are an intelligent educational assistant. Explain the topic "{topic}" to a {reading_level} level learner.

Learner background: {education} student
Learner interests: {interests}
Key concepts to cover: {core_concepts}
Avoid using these technical terms without explanation: {technical_terms}

Instructions:
- Use simple vocabulary appropriate for a {reading_level} learner
- Use analogies or examples related to {interests}
- Keep the explanation around {word_count} words
- Do NOT use complex mathematics
- Structure your response EXACTLY in this JSON format:

{{
  "title": "...",
  "introduction": "...",
  "main_explanation": "...",
  "analogy": "...",
  "summary": "...",
  "difficulty_level": "{reading_level}"
}}
"""
    return prompt