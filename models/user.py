import sqlite3
from db import db

class UserModel(db.Model):
    #next we do is tell SQLAlchemy that the table name where these models are going to be stored
    __tablename__='users'
# the id below  is a primary key defined up here which means it is auto incrementing,whenever we insert a new row into the database,the SQL engine we use,SQLite in our case but it could be Postgres,or MySQL will automatically assign an id for us so we don't have to do it ourselves,and when we create object through SQLAlchemy,the id is given to us as well ,so sqlalchemy would give us self.id,but when we create the object we don't have to specify an id,because it is automatically created
    id=db.Column(db.Integer,primary_key=True) #telling SQlAlchemy that there is a column called id and that is of type integer and that's the primary key,primary key  means is that this is unique and it's going to create an index based on it so it makes it easy to search based on id
    username =db.Column(db.String(80))  #limit the size of username to 80 and tellsqlachemy what columsn are there and what are thier types
    password=db.Column(db.String(80))

    #above our 3 columns are model is going to have so we telling this to sqlalchemy
    #these above column names must match with these properties self.id self.username etc to be saved to the database if we have extra property of the class that is not written above then that won't be saved to the database
    def __init__(self,username,password):
        self.username=username
        self.password=password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first() #cls.query going to return us the query builder that essentially return SELECT * FROM users

    @classmethod
    def find_by_id(cls,_id):  #for searching by user id
         return cls.query.filter_by(id=_id).first()