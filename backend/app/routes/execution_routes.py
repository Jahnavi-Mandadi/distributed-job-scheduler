from flask import Blueprint,jsonify

from app.extensions import db

from app.models.task_model import Task
from app.models.dag_run_model import DagRun
from app.models.task_run_model import TaskRun

from app.services.execution_service import (get_runnable_tasks,execute_task)

execution_bp=Blueprint("execution",__name__)


@execution_bp.route("/run_dag/<int:dag_id>",methods=['POST'])
def run_dag(dag_id):
    print("Day6 Execution Started")

    dag_run=DagRun(dag_id=dag_id)

    db.session.add(dag_run)
    db.session.commit()

    tasks= Task.query.filter_by(dag_id=dag_id).all()

    for task in tasks:
        task_run=TaskRun(
            task_id=task.id,
            dag_run_id=dag_run.id
        )

        db.session.add(task_run)

    db.session.commit()

    #Orchestration loop
    while True:

        runnable_tasks=get_runnable_tasks(dag_run.id)

        if not runnable_tasks:
            break

        for  task_run in runnable_tasks:
            execute_task(task_run)

    failed_tasks =TaskRun.query.filter_by(
        dag_run_id=dag_run.id,
        state='failed'
    ).all()

    if failed_tasks:
        dag_run.state='failed'
    else:
        dag_run.state='success'
    
    db.session.commit()
    

    return jsonify({
        "message":"DAG Executed Succesfully",
        "dag_run_id":dag_run.id

    })
