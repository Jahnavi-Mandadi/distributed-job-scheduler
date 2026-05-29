from flask import Blueprint,jsonify

from app.models.dag_run_model import DagRun
from app.models.task_run_model import TaskRun 

monitoring_bp=Blueprint("monitoring",__name__)

@monitoring_bp.route("/dag_runs",methods=['GET'])
def get_dag_runs():

    dag_runs=DagRun.query.all()

    return jsonify([
        run.to_dict()
        for run in dag_runs
    ])

@monitoring_bp.route("/task_runs",methods=['GET'])

def get_task_runs():

    task_runs=TaskRun.query.all()

    return jsonify([
        run.to_dict()
        for run in task_runs
    ])
