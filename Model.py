from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    address = db.Column(db.String(300))
    username = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    avatar = db.Column(db.String(500))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

