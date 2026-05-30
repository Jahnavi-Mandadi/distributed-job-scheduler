from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def check_scheduled_dags():
    print("Checking scheduled DAGs...")

def start_scheduler():
    print("start_scheduler called")

    scheduler.add_job(
        check_scheduled_dags,
        "interval",
        seconds=10
    )

    scheduler.start()

    print("Scheduler Started")