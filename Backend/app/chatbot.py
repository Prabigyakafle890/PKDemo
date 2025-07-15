from app.intent_matcher import detect_intent, is_allowed
from app.intent_responses import get_response_for_intent  # new module you'll make

def get_response(user_input, user_type):
    intent = detect_intent(user_input)

    if not is_allowed(intent, user_type):
        return "🚫 This information is restricted to institutional users."

    return get_response_for_intent(intent, user_input)  # gets answer from Excel data

