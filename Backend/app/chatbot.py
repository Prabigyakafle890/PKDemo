def get_response(message, user_type, department=None):
    message = message.lower()

    general_responses = {
        'admission': "Admissions are open! Visit our website or contact the front desk.",
        'contact': "You can reach us at 01-1234567 or email info@padmakanya.edu.np.",
        'courses': "We offer programs in BSc, BBS, BA, and B.Ed."
    }

    student_responses = {
        'routine': f"{department} class routine will be updated soon.",
        'exam': "Exams are scheduled for next month.",
        'result': "Results will be published in the student portal."
    }

    if user_type == 'student':
        for keyword, response in student_responses.items():
            if keyword in message:
                return response
        return "Hello student! You can ask about routine, exams, or results."

    elif user_type == 'general':
        for keyword, response in general_responses.items():
            if keyword in message:
                return response
        return "Hi there! I can help with general college queries like admission or contact info."

    else:
        return "Sorry, I didn't understand that. Can you rephrase?"