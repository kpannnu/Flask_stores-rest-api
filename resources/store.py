from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message':'Store not found'},404  # this is a tuple we have returned

    def post(self,name):
        if StoreModel.find_by_name(name):
            return {"message':'Store with name '{}' already exists".format(name)},400
        store=StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message':'An error occured while creating the store'},500 #500 is internal server error

        return store.json(),201

    def delete(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            StoreModel.delete_from_db(store)
        
        return {'message':'Store deleted'} 


class StoreList(Resource):
    def get(self):
        return {'stores':[store.json() for store in StoreModel.query.all()]}