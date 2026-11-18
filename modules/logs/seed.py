from datetime import datetime, timedelta
from extensions import db
from .models import LogEvent

def seed_demo():
    now = datetime.utcnow()
    for i in range(6):
        db.session.add(LogEvent(
            timestamp=now - timedelta(minutes=i),
            source="ssh", utilisateur="admin", ip_source="203.0.113.50",
            event_type="auth_failure",
            message="Failed password for admin from 203.0.113.50"))
    db.session.add(LogEvent(
        timestamp=now, source="ssh", utilisateur="yassine",
        ip_source="192.168.1.20", event_type="auth_success",
        message="Accepted password for yassine from 192.168.1.20"))
    db.session.commit()