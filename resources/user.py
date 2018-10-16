from flask_restful import Resource, reqparse
from models.user import UserModel

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email',
        type=str,
        required=True,
        help='This field cannot be left blank'
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help='This field cannot be left blank'
    )

    def get(self, name):
        user = UserModel.find_by_name(name)
        if user:
            return user.json()
        else:
            return {'message': 'The user does not exist'}, 404


    def post(self, name):
        user = UserModel.find_by_name(name)
        if user:
            return {'message': 'A user with that name already exits.'}, 400
        else:
            data = User.parser.parse_args()
            user = UserModel(name, **data)

            try:
                user.save_to_db()
            except:
                return {'message': 'An error accurred while creating the user'}, 500

        return user.json(), 201

    def delete(self, name):
        user = UserModel.find_by_name(name)
        if user:
            user.delete_from_db()
            return {'message': 'User Deleted'}
        else:
            return{'message': 'User not found'}, 404



class UserList(Resource):
    def get(self):
        return {'users': [user.json() for user in UserModel.query.all()]}
