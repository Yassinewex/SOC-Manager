from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Incident(db.Model):
    __tablename__ = 'incidents'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    severity = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(20), default='NEW') # NEW, IN_PROGRESS, RESOLVED, CLOSED
    assignee = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # علاقة مع التنبيهات
    alerts = db.relationship('Alert', backref='incident', lazy=True)

class Alert(db.Model):
    __tablename__ = 'alerts'
    id = db.Column(db.Integer, primary_key=True)
    rule_id = db.Column(db.String(50), nullable=False)
    rule_name = db.Column(db.String(255))
    source_ip = db.Column(db.String(45))
    target_host = db.Column(db.String(100))
    severity = db.Column(db.String(10), nullable=False) # P1, P2, P3, P4
    score = db.Column(db.Float, default=0.0)
    status = db.Column(db.String(20), default='NEW')
    mitre_tactic = db.Column(db.String(100))
    mitre_technique = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    incident_id = db.Column(db.Integer, db.ForeignKey('incidents.id'), nullable=True)
