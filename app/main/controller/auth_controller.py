from flask import request
from flask_restplus import Resource

from app.main.services.auth_service import login_user, logout_user
from ..util.dto import AuthDto
from ..util.decorator import token_required

api = AuthDto.api
user_auth = AuthDto.user_auth
parser = AuthDto.parser

@api.route("/login")
class UserLogin(Resource):
    @api.doc("user login", parser=parser)
    def post(self):
        post_data = request.json
        
        return login_user(data=post_data)

@token_required
@api.route("/logout")
class LogoutAPI(Resource):
    @api.doc("logout a user")
    def post(self):
        post_data = request.headers.get("authorization")
        
        return logout_user(data=post_data)
