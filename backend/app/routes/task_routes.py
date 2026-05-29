from flask import Blueprint,request,jsonify

from app.extensions import db
from app.models.task_model import Task

task_bp=Blueprint("tasks",__name__)

@task_bp.route("/tasks",methods=["POST"])
def create_task():
    data=request.get_json()

    name=data.get("name")
    task_type=data.get("task_type")
    command=data.get("command")
    dag_id=data.get("dag_id")
    dependency_task_id=data.get("dependency_task_id")

    if not name or not task_type or not dag_id:
        return jsonify({"error":"Required fields are missing"}),400
    
    task=Task(
        name=name,
        task_type=task_type,
        command=command,
        dag_id=dag_id,
        dependency_task_id=dependency_task_id
    )

    db.session.add(task)
    db.session.commit()

    return jsonify(task.to_dict()),201

@task_bp.route("/tasks",methods=["GET"])
def get_tasks():
    tasks=Task.query.all()
    return jsonify ([task.to_dict() for task in tasks])


 

