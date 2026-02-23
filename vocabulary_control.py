# A small list of complex words and their simple replacements
COMPLEX_TO_SIMPLE = {
    "utilize": "use",
    "facilitate": "help",
    "subsequently": "then",
    "phenomenon": "event",
    "instantaneously": "instantly",
    "probability amplitude": "chance value",
    "wave function": "energy pattern",
    "superposition": "being in two states at once"
}

def simplify_vocabulary(text: str, reading_level: str) -> str:
    if reading_level != "Beginner":
        return text  # Only apply for beginners
    
    for complex_word, simple_word in COMPLEX_TO_SIMPLE.items():
        text = text.replace(complex_word, simple_word)
    
    return text

def apply_vocabulary_control(content: dict, reading_level: str) -> dict:
    content["main_explanation"] = simplify_vocabulary(content["main_explanation"], reading_level)
    content["introduction"] = simplify_vocabulary(content["introduction"], reading_level)
    return content