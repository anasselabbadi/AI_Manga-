from flask import Blueprint, request, jsonify
from services.image_processing import generate_image

images_bp = Blueprint("images", __name__)

@images_bp.route("/generate_image", methods=["POST"])
def generate_manga_image():
    data = request.json
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Le prompt est requis"}), 400

    image_url = generate_image(prompt)
    return jsonify({"image_url": image_url})
