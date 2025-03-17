from flask import Flask
from routes.scenario import scenario_bp
from routes.images import images_bp
from routes.chat import chat_bp
from routes.layout import layout_bp
from routes.export import export_bp

app = Flask(__name__)

# Enregistrement des routes API
app.register_blueprint(scenario_bp, url_prefix="/api/scenario")
app.register_blueprint(images_bp, url_prefix="/api/images")
app.register_blueprint(chat_bp, url_prefix="/api/chat")
app.register_blueprint(layout_bp, url_prefix="/api/layout")
app.register_blueprint(export_bp, url_prefix="/api/export")

@app.route("/")
def home():
    return {"message": "Bienvenue sur l'API MangaAI"}

if __name__ == "__main__":
    app.run(debug=True, port=5000)
