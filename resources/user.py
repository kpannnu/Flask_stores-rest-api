import sqlite3
from flask_restful import Resource,reqparse  #import the parser from flask_restful
from models.user import UserModel

# this user class must not be same as the resource that we are going to use to sign up
class UserRegistar(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',
                    type=str,
                    required=True,
                    help="This field cannot be blank"
                    )
    parser.add_argument('password',
                    type=str,
                    required=True,
                    help="This field cannot be blank"
                    )
    # the above parser will parse through the JSON of the request and make sure userame and password are there

    def post(self):
        data=UserRegistar.parser.parse_args() #parse the arguments using UserRegustar parser which is going to expect username and a password
        if UserModel.find_by_username(data['username']):# to find if username already exists
            return {'message':"A user with that username already exists "},400
        
        user=UserModel(**data)
        user.save_to_db()
        return {'message':'User created successfuly.'},201