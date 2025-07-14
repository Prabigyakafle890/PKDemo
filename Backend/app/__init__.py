from flask import Flask

def create_app():
    app = Flask(__name__, template_folder="../templates")
    app.secret_key = 'your-secret-key'  # required for session to work

    from app.routes import chatbot_bp  # ✅ import from routes.py
    app.register_blueprint(chatbot_bp)

    return app
