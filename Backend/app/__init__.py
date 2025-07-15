from flask import Flask
<<<<<<< HEAD

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def create_app():
   
  
  
    app = Flask(__name__, static_folder='../static',template_folder="../templates")
    app.secret_key = 'your-secret-key'  # required for session to work
=======

def create_app():
    app = Flask(__name__, template_folder="../templates")
    app.secret_key = 'your-secret-key'  # required for session to work

    from app.routes import chatbot_bp  # ✅ import from routes.py
    app.register_blueprint(chatbot_bp)
>>>>>>> d970e6d7db84c93091c5fc4422157941eae9f541

    from app.routes import chatbot_bp  # ✅ import from routes.py
    app.register_blueprint(chatbot_bp)
    CORS(app)
    return app
