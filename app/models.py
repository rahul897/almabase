from app import db

class User(db.Model):
    email = db.Column(db.String(120), primary_key=True)
    source = db.Column(db.String(30),nullable=False)
    destination = db.Column(db.String(30),nullable=False)
    time = db.Column(db.DateTime,nullable=False)
    traveltime = db.Column(db.Integer,nullable=False)
    level = db.Column(db.Integer,nullable=False,default=5)
    checked = db.Column(db.Boolean,nullable=False,default=False)

    def __repr__(self):
        return '<User {}>'.format(self.email)

class Action(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime,nullable=False)
    email = db.Column(db.String(120),nullable=False)
    api = db.Column(db.String,nullable=False)