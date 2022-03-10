from flask_restful import Resource,reqparse
from flask_jwt import jwt_required

from models.item import ItemModel




class Item(Resource):#CRUD API's only
    parser=reqparse.RequestParser()
    parser.add_argument('price',type=float,required=True,help='this field cannot be left blank!')
    parser.add_argument('store_id',type=int,required=True,help='Every item needs a store id. ')
    
    @jwt_required()
    def get(self,name):
        
        item=ItemModel.find_by_name(name)
        if item:
            return item.json()  #the item returns itself to a json or a dictionary basically
        return {'message':'Item not found'},400


    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message':'An item with name {} already exists'.format(name)},400  #400->something got wrong with the request 
        data=self.parser.parse_args()
        #item=ItemModel(name,data['price'],data['store_id'])
        #OR
        item=ItemModel(name,**data)  #** for dictionary unpacking and is equivalent to 'price'=data['price'],'store_id'=data['store_id']
        try:
            item.save_to_db()
        except:
            return {'message':'An error occured inserting the item.'},500       #500->internal server error
        
        
        return item.json(),201
    
    
    def delete(self,name):
        item=ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message':'Item deleted'}

       

    def put(self,name):
        data=Item.parser.parse_args()
        
        item=ItemModel.find_by_name(name)
        
        if item is None:
            item=ItemModel(name,data['price'],data['store_id'])

        else:
            item.price= data['price'] 
        item.save_to_db() #we are doing this as this item is uniquely identified by it's id  so SQLAchemy will update if the price has changed  or it will insert a new one if there wasn't one there already 
        return item.json()
            
    
class ItemList(Resource):
    def get(self):
       #return {'items':[item.json() for item in ItemModel.query.all()]}  #using list comprehension
       #or
       return {'items': list(map(lambda x:x.json(),ItemModel.query.all()))}  #it would apply this function to each element in this list,so that mapping is maopping of function to elements and then it would make them into a list

       #list comprehension is more pythonic if we are programming in python only and is better use map if we are also programming in other languages there map is more familiar