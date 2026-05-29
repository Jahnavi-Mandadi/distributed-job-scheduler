from app.extensions import db

class DagRun(db.Model):
    __tablename__="dag_runs"

    id=db.Column(db.Integer,primary_key=True)

    dag_id=db.Column(
        db.Integer,
        db.ForeignKey("dags.id"),
        nullable=False   
    )

    state=db.Column(
        db.String(20),
        default="running"
    )

    def to_dict(self):
        return{
            "id":self.id,
            "dag_id":self.dag_id,
            "state":self.state
        }