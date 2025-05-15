from flask import Blueprint, request, jsonify, render_template
from .services import get_ai_response

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET"])
def home():
    return render_template("index.html")  # O podés sacar si usás frontend separado

@main_bp.route("/api/preguntar", methods=["POST"])
def preguntar():
    data = request.get_json(force=True)
    prompt = data.get("prompt")

    if prompt is None:
        return jsonify({"error": "No se recibió el parámetro 'prompt'."}), 400
    
    try:
        respuesta = get_ai_response(prompt)
        return jsonify({"respuesta": respuesta})
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except RuntimeError as re:
        return jsonify({"error": str(re)}), 500
    except Exception as e:
        return jsonify({"error": "Error inesperado."}), 500
