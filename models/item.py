
from db import db  #imported the db variable from db file
#and then we made the classes extend db model in both UserModel and ItemModel
class ItemModel(db.Model):  #both the user and the item model are going to extend db.Model and this is going to tell the SQLAlchemy entity that these classes here,this ItemModel and the User model that we are about to make and extend as well are things that we are going to be saving to a database and retrieving from a database so it is going to create that mapping between the database and these objects
    __tablename__='items'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    price=db.Column(db.Float(precision=2))#precison means upto how many decimal we want our float
    
    store_id=db.Column(db.Integer,db.ForeignKey('stores.id'))  #this column was added later when the store model was created
    store=db.relationship('StoreModel')  #now every item model has a property store that is the store which matches the store_id in it's id,we can also do am back reference in the Store Model

    def __init__(self,name,price,store_id):
        self.name=name
        self.price=price
        self.store_id=store_id

    def json(self):
        return {'name':self.name,'price':self.price} #A dictionary representing our items

    @classmethod
    def find_by_name(cls,name):
        #return ItemModel.query.filter_by(name=name).filter_by(id=1) # it is doing SELECT * FROM items WHERE name=name  without making connections at all
        #return ItemModel.query.filter_by(name=name,id=1)#can filter by multiple arguments simulataneously
        return cls.query.filter_by(name=name).first() #this is equivalent to the query SELECT * FROM items WHERE name=name LIMIT 1 ,means returns the first row mathing the condition ,this line directly translates it to the given SQL code in comments,also then this data also gets converted to an ItemModel object,so it is basically returning an ItemModel Object
    
    def save_to_db(self): #not only for inserting that but now for updating also,or it is also called upserting 
        # SQLAlchemy can directly translate from object to row in a database,so we don't need to tell what row data to insert ,we just need to tell to insert this object into the database and the object we are currently dealing is self
        # the seesion in this instance is collection of objects that we are going to write to the database,we can add multiple objects to this session and then write them all at once 
        db.session.add(self)  #self is the object that we need to save in database
        db.session.commit() #to save in the database
        #this above session method is useful for both the update and the insert
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()         