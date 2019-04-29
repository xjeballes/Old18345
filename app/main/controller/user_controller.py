from flask import request
from flask_restplus import Resource
from ..util.dto import UserDto
from ..util.decorator import token_required
from ..services.user_service import save_new_user, get_all_users, get_a_user, delete_user, update_user, get_logged_in_user

api = UserDto.api
_user = UserDto.user
parser = UserDto.parser

@api.route("/")
class UserList(Resource):
    @api.doc("show current user")
    def get(self):
        data, status = get_logged_in_user(request)

        payload = data.get("data")
        
        if not payload:
            return data, status

        return payload

    @api.response(201, "User successfully created.")
    @api.doc("register a user", parser=parser)
    def post(self):
        post_data = request.json

        return save_new_user(data=post_data)

@api.route("/<username>")
@api.param("username", "The User identifier")
@api.response(404, "User not found.")
class User(Resource):
    @token_required
    @api.doc("get a user")
    @api.marshal_with(_user)
    def get(self, username):
        user = get_a_user(username)

        if not user:
            api.abort(404)

        else:
            return user

    @token_required
    @api.doc("delete a user")
    def delete(self, username):
        user = delete_user(username)

        if not user:
            api.abort(404)
            
        else:
            return user

    @token_required
    @api.doc("update a user", parser=parser)
    def put(self, username):
        post_data = request.json

        user = update_user(username=username, data=post_data)
        if not user:
            api.abort(404)

        else:
            return user
