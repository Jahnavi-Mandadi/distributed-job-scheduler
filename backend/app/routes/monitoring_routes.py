from flask import Blueprint,jsonify

from app.models.dag_run_model import DagRun
from app.models.task_run_model import TaskRun 
from app.models.task_model import Task

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

    result=[]

    for task_run in task_runs:
        task=Task.query.get(task_run.task_id)

        result.append({
            "id":task_run.id,
            "task_id":task_run.task_id,
            "task_name":task.name,
            "dag_run_id":task_run.dag_run_id,
            "state":task_run.state
        })

    return jsonify(result)
