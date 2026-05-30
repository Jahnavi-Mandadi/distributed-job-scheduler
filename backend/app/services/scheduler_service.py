from apscheduler.schedulers.background import BackgroundScheduler

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
                f"DAG ID={dag.id}, Name={dag.name}"
            )


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