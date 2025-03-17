from flask import Blueprint, request, send_file
from services.export_service import export_to_pdf

export_bp = Blueprint("export", __name__)

@export_bp.route("/export_pdf", methods=["POST"])
def export_pdf():
    data = request.json
    scenario_id = data.get("scenario_id")

    if not scenario_id:
        return jsonify({"error": "Scenario ID requis"}), 400

    file_path = export_to_pdf(scenario_id)
    return send_file(file_path, as_attachment=True)
