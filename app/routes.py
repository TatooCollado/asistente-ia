from flask import Blueprint, request, jsonify, render_template
from .services import get_ai_response, init_gemini

main_bp = Blueprint("main", __name__)

# Inicializa Gemini al cargar las rutas
init_gemini()

@main_bp.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@main_bp.route("/api/preguntar", methods=["POST"])
def preguntar():
    data = request.get_json(force=True)
    prompt = data.get("prompt")

    if prompt is None:
        return jsonify({"error": "Se requiere el parámetro 'prompt'"}), 400
    
    try:
        respuesta = get_ai_response(prompt)
        return jsonify({"respuesta": respuesta})
    except ValueError as ve:  # Errores de validación
        return jsonify({"error": str(ve)}), 400
    except RuntimeError as re:  # Errores de Gemini
        return jsonify({"error": str(re)}), 503
    except Exception as e:  # Otros errores
        return jsonify({"error": "Error interno del servidor"}), 500
