from flask import Blueprint, request, jsonify

from app.extensions import db
from app.models.dag_model import Dag

dag_bp = Blueprint("dags", __name__)


@dag_bp.route("/dags", methods=["POST"])
def create_dag():

    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    name = data.get("name")
    schedule = data.get("schedule")
    description = data.get("description")

    if not name or not schedule:
        return jsonify({"error": "Name and schedule required"}), 400

    new_dag = Dag(
        name=name,
        schedule=schedule,
        description=description
    )

    db.session.add(new_dag)
    db.session.commit()

    return jsonify(new_dag.to_dict()),201

@dag_bp.route("/dags",methods=["GET"])
def get_dags():
    dags=Dag.query.all()
    return jsonify([dag.to_dict() for dag in dags]),200