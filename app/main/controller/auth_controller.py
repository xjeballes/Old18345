from flask import request
from flask_restplus import Resource

from app.main.services.auth_service import login_user, logout_user
from ..util.dto import AuthDto
from ..util.decorator import token_required

api = AuthDto.api
user_auth = AuthDto.user_auth
parser = AuthDto.parser

@api.route("/login")
class Login(Resource):
    @api.doc("user login", parser=parser)
    def post(self):

        return login_user(request.json)

@token_required
@api.route("/logout")
class Logout(Resource):
    @api.doc("logout a user")
    def post(self):

        return logout_user(request.headers.get("authorization"))
