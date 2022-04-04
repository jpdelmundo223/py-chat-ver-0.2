from .extensions import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    @staticmethod
    def verify_password_hash(password_hash: str, password: str) -> bool:
        return check_password_hash(password_hash, password)
            
    def check_if_username_already_exists(self):
        username = User.query.filter_by(username=self.username).first()
        if username:
            return 

    def check_if_email_already_exists(self):
        username = User.query.filter_by(username=self.email).first()
        if username:
            return 