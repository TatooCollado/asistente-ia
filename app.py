from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY no encontrado en variables de entorno.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route("/")  
def home():
    return render_template("index.html")

@app.route("/api/preguntar", methods=["POST"])
def preguntar():
    data = request.get_json()
    prompt = data.get("prompt", "").strip()
    if not prompt:
        return jsonify({"error": "El prompt no puede estar vacío."}), 400
    try:
        response = model.generate_content(prompt)
        return jsonify({"respuesta": response.text})
    except Exception as e:
        return jsonify({"error": f"Error al comunicarse con Gemini: {str(e)}"}), 500




