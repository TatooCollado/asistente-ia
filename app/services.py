# app/services.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carga variables de entorno desde .env (solo una vez al importar este módulo)
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("No se encontró GEMINI_API_KEY en las variables de entorno.")

# Configuro Gemini con la API key
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

def get_ai_response(prompt: str) -> str:
    """
    Envía el prompt a Gemini y devuelve la respuesta en texto plano.
    Levanta errores claros en caso de fallas o prompt inválido.
    """
    if not prompt or not prompt.strip():
        raise ValueError("El prompt no puede estar vacío.")
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Podés agregar aquí logging si querés
        raise RuntimeError(f"Error al comunicarse con Gemini: {e}")
