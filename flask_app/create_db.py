'''

from app import db
from models.models import Profile

def create_database():
    db.create_all()


if __name__ == '__main__':
    create_database() 

'''


import os


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\\working\\tryouts\\flask_app\\test.db'
db = SQLAlchemy(app)


class Profile(db.Model):
    # Id : Field which stores unique id for every row in 
    # database table.
    # first_name: Used to store the first name if the user
    # last_name: Used to store last name of the user
    # Age: Used to store the age of the user
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)


with app.app_context():
    print('------------------------------')
    print("Current Working Directory:", os.getcwd())

    #db.init_app(app)  # Initialize database with app
    #with app.app_context():
    #    db.create_all()  # Ensure tables exist

    db.create_all()  # This will now work  
    print('------------------------------')
      
    #print("Current Working Directory:", os.getcwd())

    #p = Profile(first_name='Anu', last_name='Mohan', age=35)
    #db.session.add(p)
    #db.session.commit()