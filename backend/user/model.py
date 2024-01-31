from backend.database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    nickname = db.Column(db.String(64))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255))
    avatar_url = db.Column(db.String(255))

    def __init__(self, id=None, username=None, password=None):
        # pylint: disable=redefined-builtin
        self.id = id

        self.username = username
        self.password = self.set_password(password)

    def set_password(self, password):
        return generate_password_hash(password, method="pbkdf2:sha1:100", salt_length=2)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "nickname": self.nickname,
            "email": self.email,
            "avatar_url": self.avatar_url,
        }
