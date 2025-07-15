from flask import Blueprint, request, jsonify, session, render_template
from app.chatbot import get_response
from app.auth import check_user_type

chatbot_bp = Blueprint('chatbot_bp', __name__)

@chatbot_bp.route("/")
def home():
    return render_template("index.html")  # main landing page

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

@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    user_type = session.get("user_type", "guest")
    response = get_response(user_input, user_type)
    return jsonify({"response": response})
