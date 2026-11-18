from flask import Blueprint, jsonify, request
from models import db, Alert, Incident

alerting_bp = Blueprint('alerting', __name__, url_prefix='/api/alerts')

@alerting_bp.route('/', methods=['GET'])
def get_alerts():
    alerts = Alert.query.order_by(Alert.created_at.desc()).all()
    return jsonify([{
        "id": a.id, "rule_id": a.rule_id, "rule_name": a.rule_name,
        "target": a.target_host, "severity": a.severity, "status": a.status
    } for a in alerts])

@alerting_bp.route('/', methods=['POST'])
def create_alert():
    data = request.json
    new_alert = Alert(
        rule_id=data.get('rule_id'), rule_name=data.get('rule_name'),
        source_ip=data.get('source_ip'), target_host=data.get('target_host'),
        severity=data.get('severity', 'P3')
    )
    db.session.add(new_alert)
    db.session.commit()
    return jsonify({"message": "Alerte enregistrée", "id": new_alert.id}), 201

@alerting_bp.route('/<int:alert_id>/escalate', methods=['POST'])
def escalate_alert(alert_id):
    alert = Alert.query.get_or_404(alert_id)
    if alert.incident_id:
        return jsonify({"error": "Déjà escaladée"}), 400
        
    incident = Incident(title=f"Incident lié à {alert.rule_name}", severity=alert.severity)
    db.session.add(incident)
    db.session.flush()
    
    alert.incident_id = incident.id
    alert.status = "ESCALATED"
    db.session.commit()
    return jsonify({"message": "Incident créé", "incident_id": incident.id}), 201
