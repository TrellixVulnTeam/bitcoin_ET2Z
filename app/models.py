from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)

    def __repr__(self):
        return '<Role %r' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    mobile = db.Column(db.Integer, nullable = False, index = True)
    identity = db.Column(db.String(20), nullable = False, index=True)
    name = db.Column(db.String(12), nullable = False, index = True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForgignKey ('roles.id'))

    @property
    def password(self):
        return AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verif_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r' % self.name




