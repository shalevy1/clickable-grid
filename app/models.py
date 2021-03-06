from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username

# class Grid(db.Model):
#     __tablename__ = 'grids'
#     x = db.Column(db.Integer)
#     y = db.Column(db.Integer)
#     grid_type = db.Column(db.String(64))
#     colors = db.Column(db.String(64))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))