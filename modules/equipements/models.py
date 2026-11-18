from datetime import datetime
from extensions import db

class Equipement(db.Model):
    __tablename__ = "equipements"
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    ip = db.Column(db.String(45), nullable=False)
    os = db.Column(db.String(100))
    statut = db.Column(db.String(20), default="non_supervise")
    wazuh_agent_id = db.Column(db.String(10), unique=True)
    derniere_communication = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)