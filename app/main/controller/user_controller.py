from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..util.decorator import token_required
from ..services.user_service import save_new_user, get_all_users, get_a_user, delete_user, update_user

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @token_required
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<public_name>')
@api.param('public_name', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @token_required
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_name):
        """get a user given its identifier"""
        user = get_a_user(public_name)
        if not user:
            api.abort(404)
        else:
            return user

    @token_required
    @api.doc('delete a user')
    def delete(self, public_name):
        """delete a user given its identifier"""
        user = delete_user(public_name)
        if not user:
            api.abort()
        else:
            return user

    @token_required
    @api.doc('update a user')
    def put(self, public_name):
        """update user properties"""
        data = request.json
        user = update_user(public_name=public_name, data=data)
        if not user:
            api.abort(404)
        else:
            return user
