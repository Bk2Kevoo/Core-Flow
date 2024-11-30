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


121212121