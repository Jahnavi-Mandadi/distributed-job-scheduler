from app import create_app
from  app.extensions import db

from app.models.dag_model import Dag
from app.models.task_model import Task
from app.models.dag_run_model import DagRun
from app.models.task_run_model import TaskRun
from app.services.scheduler_service import start_scheduler


app=create_app()

with app.app_context():
    db.create_all()
    start_scheduler(app)


if __name__=="__main__":
    
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
