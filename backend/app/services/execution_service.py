from app.extensions import db

from app.models.task_model import Task
from app.models.task_run_model import TaskRun

from workflows.extract import run as extract_run
from workflows.transform import run as transform_run
from workflows.load import run as load_run
from workflows.validate import run as validate_run



def get_runnable_tasks(dag_run_id):

    print("Checking runnable tasks...")
    runnable_tasks=[]

    task_runs=TaskRun.query.filter_by(
        dag_run_id=dag_run_id
    ).all()

    print(f"Total Task Runs: {len(task_runs)}")

    for task_run in task_runs:

        print(
            f"TaskRun={task_run.id}, State={task_run.state}"
            )
        if task_run.state!="pending":
            continue
        task=Task.query.get(task_run.task_id)
        dependency_id=task.dependency_task_id

        if dependency_id is None:
            runnable_tasks.append(task_run)
        else:
            dependency_run=TaskRun.query.filter_by(
                dag_run_id=dag_run_id,
                task_id=dependency_id
            ).first()

            if (
                dependency_run and dependency_run.state=='success'
            ):
                runnable_tasks.append(task_run)

    print(f"Runnable Tasks Found: {len(runnable_tasks)}")
    return runnable_tasks

def execute_task(task_run):
    
    task=Task.query.get(
        task_run.task_id
    )

    print(f"Executing {task.name}")

    task_run.state="running"

    db.session.commit()

    try:
        if task.name=="Extract Booking Data":
            extract_run()

        elif task.name=="Transform Booking Data":

            import pandas as pd
            df=pd.read_csv(
                "data/hotel_bookings.csv"
            )
            transform_run(df)

        elif task.name=="Validate Booking Data":
             
            import pandas as pd
            df=pd.read_csv(
                "data/hotel_bookings.csv"
            )
            validate_run(df)
        
        elif task.name=="Load Reservation Data":
            import pandas as pd

            df=pd.read_csv(
                "data/hotel_bookings.csv"
            )
            
            load_run(df)
        task_run.state="success"
    except Exception as e:
        print(str(e))

        task_run.state="failed"
    db.session.commit()