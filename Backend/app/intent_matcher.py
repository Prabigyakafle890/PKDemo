import re

# Expanded and cleaned intent map
intent_keywords = {
    "admission": ["admission", "enroll", "apply", "registration", "form"],
    "results": ["result", "marksheet", "grade", "score", "gpa"],
    "finance": ["salary", "budget", "funding", "audit", "expense", "fee"],
    "courses": ["course", "subject", "curriculum", "syllabus"],
    "timetable": ["schedule", "timetable", "class time", "routine"],
    "general": []  # fallback intent
}

restricted_intents = {"finance"}  # Set makes lookup faster

def detect_intent(message):
    """Detect intent from message text."""
    message = message.lower()
    for intent, keywords in intent_keywords.items():
        for keyword in keywords:
            if re.search(rf'\b{re.escape(keyword)}\b', message):
                return intent
    return "general"

def is_allowed(intent, user_type):
    """Check if the user is allowed to access info of this intent."""
    return not (intent in restricted_intents and user_type == "guest")
