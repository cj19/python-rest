from models.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, username='', email=''):
        self.username = username
        self.email = email

    def __repr__(self):
        return 'Username: {}, email: {}.'.format(self.username, self.email)

