import os
import google.generativeai as genai
from dotenv import load_dotenv

# Estado global controlado
GEMINI_READY = False
model = None

def init_gemini():
    """Inicialización diferida de Gemini"""
    global GEMINI_READY, model
    
    load_dotenv()  # Solo carga .env cuando se llama
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("⚠️ Gemini desactivado: Falta GEMINI_API_KEY")
        return
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-pro")
        GEMINI_READY = True
        print("✅ Gemini configurado correctamente")
    except Exception as e:
        print(f"❌ Error configurando Gemini: {str(e)}")

def get_ai_response(prompt: str) -> str:
    """Versión segura para producción"""
    if not prompt or not prompt.strip():
        raise ValueError("El prompt no puede estar vacío")
    
    if not GEMINI_READY:
        raise RuntimeError("Servicio Gemini no disponible (configuración faltante o inválida)")
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise RuntimeError(f"Error en Gemini: {str(e)}")