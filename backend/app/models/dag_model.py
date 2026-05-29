from app.extensions import db

class Dag(db.Model):
    __tablename__="dags"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    schedule=db.Column(db.String(100),nullable=False)
    description=db.Column(db.String(300))
    is_active=db.Column(db.Boolean,default=True)


    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "schedule":self.schedule,
            "description":self.description,
            "is_active":self.is_active
        }