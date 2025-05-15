# app.py
import os
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from dotenv import load_dotenv

# Carga variables de entorno desde .env
load_dotenv()

app = Flask(__name__)

# Configurar API Key de Gemini desde variables de entorno
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY no encontrado en variables de entorno.")

genai.configure(api_key=api_key)

# Modelo gratuito
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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)