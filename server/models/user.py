from models.__init__ import SerializerMixin, validates, db

class User(db.Model, SerializerMixin):
    __tablename__ = "users"


    # add relationship
    
    # add serialization rules
    serialize_rules = ('-',)

    #add validations
    

    def __repr__(self):
        return f"<Users {self.name}>"