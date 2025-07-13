from flask import Flask
from flask_cors import CORS
from app.routes import chatbot_routes

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable cross-origin requests (important for frontend)

    # Register routes
    app.register_blueprint(chatbot_routes)

    return app
