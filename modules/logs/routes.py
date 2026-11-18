from flask import Blueprint, request, jsonify
from sqlalchemy import func
from extensions import db
from .models import LogEvent
from .seed import seed_demo

bp = Blueprint("logs", __name__, url_prefix="/api/logs")

def to_dict(e):
    return {"id": e.id, "timestamp": e.timestamp, "source": e.source,
            "utilisateur": e.utilisateur, "ip_source": e.ip_source,
            "event_type": e.event_type, "message": e.message}

@bp.get("/")
def rechercher():
    q = LogEvent.query
    if v := request.args.get("user"):      q = q.filter(LogEvent.utilisateur == v)
    if v := request.args.get("ip"):        q = q.filter(LogEvent.ip_source == v)
    if v := request.args.get("type"):      q = q.filter(LogEvent.event_type == v)
    if v := request.args.get("source"):    q = q.filter(LogEvent.source == v)
    if v := request.args.get("date_from"): q = q.filter(LogEvent.timestamp >= v)
    if v := request.args.get("date_to"):   q = q.filter(LogEvent.timestamp <= v)
    page = request.args.get("page", 1, type=int)
    p = q.order_by(LogEvent.timestamp.desc()).paginate(page=page, per_page=50)
    return jsonify([to_dict(e) for e in p.items])

@bp.get("/suspicious-ips")
def ips_suspectes():
    rows = (db.session.query(LogEvent.ip_source, func.count())
            .filter(LogEvent.event_type == "auth_failure")
            .group_by(LogEvent.ip_source)
            .having(func.count() > 5).all())
    return jsonify([{"ip": ip, "echecs": n} for ip, n in rows])

@bp.post("/seed")
def seed():
    seed_demo()
    return jsonify({"ok": True})