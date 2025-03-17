from flask import Blueprint, request, jsonify
from services.ai_service import chat_with_user

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "Message requis"}), 400

    response = chat_with_user(user_message)
    return jsonify({"response": response})
