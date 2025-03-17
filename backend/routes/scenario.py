from flask import Blueprint, request, jsonify

scenario_bp = Blueprint("scenario", __name__)

@scenario_bp.route("/generate_scenario", methods=["POST"])
def generate_story():
    data = request.json
    title = data.get("title")
    description = data.get("description")

    if not title or not description:
        return jsonify({"error": "Titre et description requis"}), 400

    scenario = f"Scénario généré : {title} - {description} (exemple fictif)"
    
    return jsonify({"scenario": scenario})
