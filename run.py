from app import app
from db import db #to avoid circular imports

db.init_app(app)

#flask decorator
@app.before_first_request  #this decorator of flask is going to affect the method below it and it's going to run that method before the first request into this app
def create_tables():  #it only creates the tables it sees so the import of those things or Models containing tables is important
    db.create_all()   #before the first request runs it's going to run this method and that is going to create this file there data.db and it's gonna create all the tables in the file unless they exist already
