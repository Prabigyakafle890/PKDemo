from flask import Blueprint, request, jsonify
from app.chatbot import generate_response

chatbot_routes = Blueprint('chatbot_routes', __name__)

@chatbot_routes.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_msg = data.get('message', '')
    user_type = data.get('user_type', 'general')  # "student" or "general"
    department = data.get('department', None)

    reply = generate_response(user_msg, user_type, department)
    return jsonify({"reply": reply})
