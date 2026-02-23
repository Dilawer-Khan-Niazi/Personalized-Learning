INTEREST_ANALOGIES = {
    "Football": "Imagine two football players who are perfectly in sync — if one moves left, the other mirrors it instantly, no matter how far apart they are.",
    "Gaming": "Think of two game characters that are always linked — whatever one does, the other automatically does the same, even in different game worlds.",
    "Space": "Imagine two stars on opposite sides of the galaxy that always spin in opposite directions — as if they're secretly connected.",
    "Business": "Think of two companies: whenever one makes a profit, the other automatically does too, no matter where in the world they are.",
    "AI": "Think of two neural networks trained together — when one updates a weight, the other reflects that update instantly."
}

def get_fallback_analogy(interests: list, topic: str) -> str:
    for interest in interests:
        if interest in INTEREST_ANALOGIES:
            return INTEREST_ANALOGIES[interest]
    return f"Think of {topic} like two mirrors facing each other — they always reflect each other's state."