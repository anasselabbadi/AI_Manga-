from flask import Blueprint, request, jsonify
from services.layout_engine import generate_layout

layout_bp = Blueprint("layout", __name__)

@layout_bp.route("/generate_layout", methods=["POST"])
def create_layout():
    data = request.json
    scenario_id = data.get("scenario_id")

    if not scenario_id:
        return jsonify({"error": "Scenario ID requis"}), 400

    layout = generate_layout(scenario_id)
    return jsonify({"layout": layout})
