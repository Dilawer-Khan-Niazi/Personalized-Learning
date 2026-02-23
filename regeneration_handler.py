from content_generator import generate_content
from vocabulary_control import apply_vocabulary_control

def regenerate_if_needed(user_profile: dict, topic_analysis: dict, readability_score: float, target_score: float, max_attempts: int = 3) -> dict:
    
    attempt = 1
    content = generate_content(user_profile, topic_analysis, attempt)
    content = apply_vocabulary_control(content, user_profile["reading_level"])

    while readability_score < target_score and attempt < max_attempts:
        print(f"Readability mismatch. Score: {readability_score}. Regenerating... (Attempt {attempt+1})")
        
        # Make the prompt stricter each time
        user_profile["extra_instruction"] = "Use even simpler words. Shorter sentences. No technical jargon."
        
        attempt += 1
        content = generate_content(user_profile, topic_analysis, attempt)
        content = apply_vocabulary_control(content, user_profile["reading_level"])

        # Paras will recalculate readability — for now simulate it
        readability_score = readability_score + 10  # placeholder until Paras integrates

    return content