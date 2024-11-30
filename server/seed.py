#!/usr/bin/env python3
from faker import Faker
from config import app
from models.__init__ import db
from models.workout import WorkOut
from models.category import Category
from models.workexercise import WorkExercise

fake = Faker()

with app.app_context():
    WorkOut.query.delete()
    Category.query.delete()
    WorkExercise.query.delete()

    
