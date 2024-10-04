# SQLAlchemy converts the models class in to a DB Table
from app import db


# defining a database model
class Person(db.Model):
    """This is the model class Person"""

    __tablename__ = "people"
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer)
    job = db.Column(db.Text)

    def __repr__(self):
        return f"Person with name {self.name} and ange {self.age}"
