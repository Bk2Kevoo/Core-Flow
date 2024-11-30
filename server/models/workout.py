from models.__init__ import SerializerMixin, validates, re, db

class WorkOut(db.Model, SerializerMixin):
    __tablename__ = "work_outs"

    __table__args__ = (
        db.CheckConstraint()
    )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))


    # Relationship
    user = db.relationship("User", back_populates="work_outs")

    def __repr__(self):
        return f"""
            Workout #{self.id}:
                Name: {self.name},
                Date: {self.date}
        """



# api.add_resource(WorkOuts, "/workouts")

