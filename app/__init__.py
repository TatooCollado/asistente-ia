from flask import Flask
from .routes import main_bp
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()  # Carga variables de entorno desde .env

    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    app.register_blueprint(main_bp)
    
    return app
