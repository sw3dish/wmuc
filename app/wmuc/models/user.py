from wmuc import db
from flask import current_app
from passlib.hash import argon2
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy.ext.hybrid import hybrid_property


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    name = db.Column(db.String(128), index=True)
    _password = db.Column(db.String(128))
    # id of the user's role (user/admin, etc.)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    registered = db.Column(db.Boolean, default=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        # using Argon2 as crytographic function
        self._password = argon2.using(rounds=4).hash(plaintext)

    def is_correct_password(self, plaintext):
        return argon2.verify(plaintext, self.password)

    # All required by Flask-Login
    # An unregistered user cannot be authenticated
    @property
    def is_authenticated(self):
        return self.registered

    # An unregistered user cannot be active
    @property
    def is_active(self):
        return self.registered

    @property
    def is_anonymous(self):
        return False

    @property
    def is_administrator(self):
        return True

    def get_id(self):
        return str(self.id)

    # Confirmation token for email registration
    # default expiration time is 6 hours
    def generate_registration_token(self, expiration=21600):
        s = Serializer(current_app.config['TOKEN_SECRET_KEY'], expiration)
        return s.dumps({'account_id': self.id})

    # Validates that there is an account in the database with no username or password
    # that can have a new user associated to it
    @staticmethod
    def register(token):
        s = Serializer(current_app.config['TOKEN_SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        # make sure that the User with the id encoded in the token has no username/password yet
        return User.query.filter_by(id=data["account_id"], username=None, password=None).first()

    def __repr__(self):
        return '<User %r>' % (self.username)
