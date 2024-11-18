def main(args):
    content = args.get("content", "stranger")
    rating = moderate_content(content)
    return {"rating": rating}

import re

# Define keyword categories with weights
KEYWORDS = {
    "political": ["election", "government", "politics", "party", "vote"],
    "harassing": ["bully", "harass", "abuse", "stalk", "threat"],
    "racist": ["racism", "racist", "hate", "ethnic", "slur"],
    "threatening": ["kill", "attack", "bomb", "destroy", "assault"],
    "offensive": ["stupid", "idiot", "dumb", "ugly", "moron"],
}

WEIGHTS = {
    "political": 1,
    "harassing": 2,
    "racist": 3,
    "threatening": 4,
    "offensive": 2,
}

def moderate_content(text: str) -> int:
    # Normalize text to lowercase and remove special characters
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation

    score = 0
    for category, keywords in KEYWORDS.items():
        for keyword in keywords:
            occurrences = len(re.findall(rf'\b{keyword}\b', text))
            score += occurrences * WEIGHTS[category]

    return score
