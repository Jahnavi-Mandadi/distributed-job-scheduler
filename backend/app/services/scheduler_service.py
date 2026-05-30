from apscheduler.schedulers.background import BackgroundScheduler
from app.models.dag_run_model import DagRun

from  app.extensions import db  

scheduler = BackgroundScheduler()


def check_scheduled_dags(app):

    with app.app_context():

        from app.models.dag_model import Dag

        print("Checking scheduled DAGs...")

        dags = Dag.query.filter_by(
            is_active=True
        ).all()

        print(f"Found {len(dags)} active DAGs")

        for dag in dags:

            print(
                f"Creating DagRun for DAG{dag.name}"
            )
            dag_run=DagRun(
                dag_id=dag.id,
                state="running"

            )
            db.session.add(dag_run)

        db.session.commit()
        print("DagRuns created successfully")


def start_scheduler(app):

    print("start_scheduler called")

    scheduler.add_job(
        check_scheduled_dags,
        "interval",
        seconds=10,
        args=[app]
    )

    scheduler.start()

    print("Scheduler Started")