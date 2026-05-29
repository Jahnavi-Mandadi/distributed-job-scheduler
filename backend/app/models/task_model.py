from app.extensions import db

class Task(db.Model):
    __tablename__="tasks"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    task_type=db.Column(db.String(50),nullable=False)
    command=db.Column(db.String(300))
    dependency_task_id=db.Column(db.Integer,nullable=True)
    dag_id=db.Column(
        db.Integer,
        db.ForeignKey("dags.id"),
        nullable=False
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "task_type": self.task_type,
            "command": self.command,
            "dependency_task_id": self.dependency_task_id,
            "dag_id": self.dag_id
        }