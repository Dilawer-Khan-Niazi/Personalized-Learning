from content_generator import generate_content
from vocabulary_control import apply_vocabulary_control
from analogy_system import get_fallback_analogy

def run_content_generation(user_profile: dict, topic_analysis: dict) -> dict:
    # Step 1: Generate content
    content = generate_content(user_profile, topic_analysis)
    
    # Step 2: Apply vocabulary control
    content = apply_vocabulary_control(content, user_profile["reading_level"])
    
    # Step 3: Add fallback analogy if analogy is missing or weak
    if not content.get("analogy") or len(content["analogy"]) < 20:
        content["analogy"] = get_fallback_analogy(user_profile["interests"], topic_analysis["topic"])
    
    return content