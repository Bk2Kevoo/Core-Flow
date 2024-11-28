from models.__init__ import SerializerMixin, validates, db

class Category(db.Model, SerializerMixin):
    __tablename__ = "categories"


    # add relationship
    
    # add serialization rules
    serialize_rules = ('-',)
    
    #add validations
    

    def __repr__(self):
        return f"<Category {self.name}>"