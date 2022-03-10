
from db import db  #imported the db variable from db file
#and then we made the classes extend db model in both UserModel and ItemModel
class StoreModel(db.Model):  #both the user and the item model are going to extend db.Model and this is going to tell the SQLAlchemy entity that these classes here,this ItemModel and the User model that we are about to make and extend as well are things that we are going to be saving to a database and retrieving from a database so it is going to create that mapping between the database and these objects
    __tablename__='stores'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    
    #backrefernce does the opposite it allows the store to see which items are in the item database or in the items table with the store_id equals to it's own id 
    #items=db.relationship('ItemModel')  #this variable items is a list of ItemModels as it is a many to one relationship => there could be many items with the same store_id
# the above relationship is created as soon as we create a store model,so if we have mant stores and many items,whenever we create a StoreModel we are going to go and create an object for each item in a database that matches that store_id,if we have few items then that is fine but if we have a lot of items then that can be a really expensive operation so we can tell SQLAlchemy to not do that ,to not go into items table and create an object for each item yet
    items=db.relationship('ItemModel',lazy='dynamic')  #after adding this lazy=dynamic whenevr we acces the JSON method we are going to get an error unless we do .all in json method below
    def __init__(self,name):
        self.name=name
        
    def json(self):
        #return {'name':self.name,'items':[item.json() for item in self.items]} #this line was used when lazy=dynamic was not used
        return {'name':self.name,'items':[item.json() for item in self.items.all()]} #A dictionary representing our items, after adding rthis .all we can avoid error due to that lazy=dynmaic done above as when we use lazy=dynamic,self.items is no longer is a list of items now it is a query builder that has the ability to look into the items table and then we can use .all() to retrieve all of the items in that table it means unntil we call the json method we are not looking into the table which means that creating stores is very simple but is also means that whenever we cal the json method we have to go into the table,there is tradeoff between speed of creating the store and speed of calling the json method as without using lazy it wil take a lot of time to create store and with using it we have to llok into the table everytime we call json method that makes it a bit slower,in our case the store model gets created when we wanna acces the data,it's gonna be like that in resource                  

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first() #this is equivalent to the query SELECT * FROM items WHERE name=name LIMIT 1 ,means returns the first row mathing the condition ,this line directly translates it to the given SQL code in comments,also then this data also gets converted to an ItemModel object,so it is basically returning an ItemModel Object
    
    def save_to_db(self): #not only for inserting that but now for updating also,or it is also called upserting 
       
        db.session.add(self)  #self is the object that we need to save in database
        db.session.commit() #to save in the database
        
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()         