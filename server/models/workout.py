from models.__init__ import SerializerMixin,db

class WorkOut(db.Model, SerializerMixin):
    __tablename__ = "workouts"

    __table__args__ = (
        db.CheckConstraint("LENGTH(name) > 1")
    )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))


    # Relationship
    user = db.relationship("User", back_populates="work_outs")

    # Serialize 
    serialize_rules = ("-user",)

    def __repr__(self):
        return f"""
            Workout #{self.id}:
                Name: {self.name},
                Date: {self.date}
        """


