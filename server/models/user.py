from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from config import db
from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column("password_hash", db.String(20), nullable=False)

    workouts = db.relationship("WorkOut", back_populates="user", cascade="all, delete-orphan")
    work_exercises = db.relationship("WorkExercise", back_populates="user", cascade="all, delete-orphan")
    categories = db.relationship("Category", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<User {self.id}: {self.name}>'

    @hybrid_property
    def password(self):
        raise AttributeError("")

    def validate_name(self, _, value):
        if not value:
            raise ValueError("name must be present")
        if len(value) < 3:
            raise ValueError("name must be at least 3 characters long")
        return value

    def validate_email(self, value):
        if not value:
            raise ValueError("email must be present")
        return value

    def validate_password(self, value):
        if not value:
            raise ValueError("password must be present")
        if len(value) < 8:
            raise ValueError("password must be at least 8 characters long")
        return value
