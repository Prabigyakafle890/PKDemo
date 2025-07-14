import re

# Intent keywords map (you will replace with DB data or ML later)
intent_keywords = {
    "admission": ["admission", "enroll", "apply"],
    "results": ["result", "marksheet", "grade"],
    "finance": ["salary", "budget", "funding", "audit"],
    "general": []
}

restricted_intents = ["finance"]

def detect_intent(message):
    message = message.lower()
    for intent, keywords in intent_keywords.items():
        for keyword in keywords:
            if re.search(r'\b' + keyword + r'\b', message):
                return intent
    return "general"

def is_allowed(intent, user_type):
    if intent in restricted_intents and user_type == "guest":
        return False
    return True
