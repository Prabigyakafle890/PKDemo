# app/intent_responses.py
from app.dataloader import load_college_data

college_data = load_college_data()

def get_response_for_intent(intent, user_input):
    for row in college_data:
        if row["intent"] == intent:
            return row["response"]
    return "Sorry, I didn't understand that."
