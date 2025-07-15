from flask import Flask

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def create_app():
   
  
  
    app = Flask(__name__, static_folder='../static',template_folder="../templates")
    app.secret_key = 'your-secret-key'  # required for session to work

    from app.routes import chatbot_bp  # ✅ import from routes.py
    app.register_blueprint(chatbot_bp)
    CORS(app)
    return app
