def generate_response(message, user_type, department=None):
    message = message.lower()

    if user_type == 'student':
        if 'routine' in message:
            return f"{department} class routine will be updated soon."
        elif 'exam' in message:
            return "Exams are scheduled for next month."
        else:
            return "Hello student! You can ask about routine, exams, or results."

    elif user_type == 'general':
        if 'admission' in message:
            return "Admissions are open! Visit our website or contact the front desk."
        else:
            return "Hi there! I can help with general college queries like admission or contact info."

    else:
        return "Sorry, I didn't understand that. Can you rephrase?"
