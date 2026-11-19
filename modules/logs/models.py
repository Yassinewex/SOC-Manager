from extensions import db

class LogEvent(db.Model):
    __tablename__ = "log_events"
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True)
    source = db.Column(db.String(30), index=True)
    equipement_id = db.Column(db.Integer, db.ForeignKey("equipements.id"), index=True)
    utilisateur = db.Column(db.String(100), index=True)
    ip_source = db.Column(db.String(45), index=True)
    event_type = db.Column(db.String(50), index=True)
    message = db.Column(db.Text)
    raw = db.Column(db.JSON)