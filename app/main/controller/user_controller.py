from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..util.decorator import token_required
from ..service.user_service import save_new_user, get_all_users, get_a_user

api = UserDto.api
_user = UserDto.user_schema


@api.route('/')
class UserList(Resource):
    @api.doc('List of registered Users', security='apikey')
    @token_required
    @api.marshal_list_with(_user, envelope='result')
    def get(self):
        return get_all_users()

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created')
    @api.doc('Create a new User', security='apikey')
    def post(self):
        data = request.json
        return save_new_user(data=data)


@api.route('/<username>')
@api.param('username', 'User Name')
@api.response(404, 'User not found')
class User(Resource):
    @api.doc('Get a User')
    @api.marshal_with(_user)
    def get(self, username):
        user = get_a_user(username)
        return api.abort(404) if not user else user