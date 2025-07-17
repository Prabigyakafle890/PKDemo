from flask import Blueprint, request, jsonify, session, render_template
from app.chatbot import get_response

from app.auth import check_user_type

chatbot_bp = Blueprint('chatbot_bp', __name__)

@chatbot_bp.route("/")
def home():
    return render_template("index.html")

@chatbot_bp.route("/guest")
def guest():
    return render_template("guest.html")

@chatbot_bp.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@chatbot_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get("email", "")
    user_type = check_user_type(email)
    session["user_type"] = user_type
    return jsonify({"status": "success", "user_type": user_type})

# ✅ merged route from chatbot_routes
@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_msg = data.get('message', '')
    email = data.get('email', '')
    department = data.get('department', None)

    user_type = 'student' if email.endswith('@padmakanya.edu.np') else 'general'
    response = get_response(user_msg, user_type, department)
    return jsonify({'response': response})
