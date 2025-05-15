from flask import Flask
import os

def create_app():
    app = Flask(__name__, template_folder='../templates')  # <-- Ruta relativa
    return app

app = create_app()