from flask import Blueprint, request, jsonify
from extensions import db
from .models import Equipement

bp = Blueprint("equipements", __name__, url_prefix="/api/equipements")

@bp.get("/")
def lister():
    return jsonify([{
        "id": e.id, "nom": e.nom, "ip": e.ip, "os": e.os,
        "statut": e.statut,
        "derniere_communication": e.derniere_communication
    } for e in Equipement.query.all()])

@bp.post("/")
def ajouter():
    d = request.get_json()
    e = Equipement(nom=d["nom"], ip=d["ip"], os=d.get("os"))
    db.session.add(e)
    db.session.commit()
    return jsonify({"id": e.id}), 201

@bp.delete("/<int:id>")
def supprimer(id):
    e = Equipement.query.get_or_404(id)
    db.session.delete(e)
    db.session.commit()
    return "", 204