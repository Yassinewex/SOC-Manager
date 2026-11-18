print("SOC-Manager starting")
import os
from flask import Flask
from extensions import db

app = Flask(__name__)

# Database: PostgreSQL ila kayn DATABASE_URL, sinon SQLite (bach tkhdm bla docker)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///soc.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Modules
from modules.equipements.routes import bp as equipements_bp
app.register_blueprint(equipements_bp)

from modules.logs.routes import bp as logs_bp
app.register_blueprint(logs_bp)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "SOCManager Platform Online"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)