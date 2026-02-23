from dilawer_module import run_content_generation

user_profile = {
    "reading_level": "Beginner",
    "education_level": "School",
    "interests": ["Football", "Gaming"]
}

topic_analysis = {
    "topic": "Quantum Entanglement",
    "core_concepts": ["quantum states", "entanglement", "superposition"],
    "complexity_score": 8.5,
    "technical_terms": ["wave function", "probability amplitude"]
}

result = run_content_generation(user_profile, topic_analysis)

import json
print(json.dumps(result, indent=2))