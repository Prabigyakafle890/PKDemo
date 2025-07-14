from app.intent_matcher import detect_intent, is_allowed
from models.gemma_loader import generate_gemma_response

def get_response(user_input, user_type):
    intent = detect_intent(user_input)

    if not is_allowed(intent, user_type):
        return "This information is restricted to institutional users."

    return generate_gemma_response(user_input)
