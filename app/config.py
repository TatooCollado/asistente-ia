import os

class Config:
    
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    if not GEMINI_API_KEY:
        raise ValueError("No se encontró GEMINI_API_KEY en las variables de entorno.")
