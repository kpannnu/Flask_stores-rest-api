
#this code was used previuos video and the code below is the current one  
#this code was used previuos video and the code below is the current one and also the line24 line 30 and line 34 code is added later in authentication and logging part 
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
#from db import db

from security import authenticate,identity
from resources.user import UserRegistar
from resources.item import Item,ItemList
from resources.store import Store,StoreList
app= Flask(__name__)
#we have to now tell SQLAlchemy where to find the data.db file
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db' # what we are saying is that the SQLAlchemy database is gonna live at the root folder of our project,SQLAlchemy with this  code is going to read the data.db that we have already created ,instead of sqlite it also could be POSTRESQL or MYSQL it will work the same
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False  #we specify a configuration property,in order to know when an object had changed but not been saved to the database,the extension flask SQLAlchemy was tracking every change that we made to the SQLAlchemy session and that took some resources,now we are turning it off because SQLAlchemy itself,the main library  has it's own modification tracker which is better so this turns off the flask SQLAchemy modification tracker.It doesn't turn off the SQLAlchemy modification tracker so this is only changing the extension behaviours and not the underlying SQLAlchemy behaviour
app.secret_key='jose'
api= Api(app)




jwt=JWT(app,authenticate,identity) #endpoint is /auth




api.add_resource(Item,'/item/<string:name>')  
api.add_resource(ItemList,'/items')
api.add_resource(UserRegistar,'/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')

#Python assigns a special name to the file we run and that name is always __main__
#also when we import a file or import something from that file then that file is alwyays run first 
#only the file that you run is __main__
'''if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000,debug=True)
'''