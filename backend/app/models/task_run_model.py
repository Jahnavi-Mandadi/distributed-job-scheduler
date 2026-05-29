from app.extensions import db

class TaskRun(db.Model):
    __tablename__="task_runs"

    id=db.Column(db.Integer,primary_key=True)

    task_id=db.Column(
        db.Integer,
        db.ForeignKey("tasks.id"),
        nullable=False
    )

    dag_run_id=db.Column(
        db.Integer,
        db.ForeignKey("dag_runs.id"),
        nullable=False
    )

    state=db.Column(
        db.String(50),
        default="pending"
    )

    def to_dict(self):
        return{
            "id":self.id,
            "task_id":self.task_id,
            "dag_run_id":self.dag_run_id,
            "state":self.state
        }