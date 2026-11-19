from flask import Blueprint, jsonify, render_template
from models import db, Alert, Incident
from sqlalchemy import func
import psutil

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard_view():
    return render_template('dashboard.html')

@dashboard_bp.route('/api/dashboard/metrics', methods=['GET'])
def get_metrics():
    alerts_by_severity = db.session.query(Alert.severity, func.count(Alert.id)).group_by(Alert.severity).all()
    open_incidents = Incident.query.filter(Incident.status.in_(['NEW', 'IN_PROGRESS', 'ESCALATED'])).count()
    
    return jsonify({
        "alerts": dict(alerts_by_severity),
        "open_incidents": open_incidents
    })

@dashboard_bp.route('/api/dashboard/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "cpu_usage": psutil.cpu_percent(interval=0.5),
        "memory_usage": psutil.virtual_memory().percent
    })
