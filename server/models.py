from sqlalchemy_serializer import SerializerMixin, validates
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

class Category(db.Model, SerializerMixin):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    @validates("name")
    def validate_name(self, value):
        if not value:
            raise ValueError("name must be present")
        if len(value) < 3:
            raise ValueError("name must be at least 3 characters long")
        return value

    def __repr__(self):
        return f'<Category {self.id}: {self.name}>'


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    workouts = db.relationship("WorkOut", back_populates="user", cascade="all, delete-orphan")
    work_exercises = db.relationship("WorkExercise", back_populates="user", cascade="all, delete-orphan")
    categories = db.relationship("Category", back_populates="user", cascade="all, delete-orphan")

    def validate_name(self, value):
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

    def __repr__(self):
        return f'<User {self.id}: {self.name}>'

