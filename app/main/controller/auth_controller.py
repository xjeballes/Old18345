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
<<<<<<< HEAD
        post_data = request.json
=======
        # get the post data
        post_data = request.form
        # post_data = request.json
        return Auth.login_user(data=post_data)
>>>>>>> cffd89c85a4e198c7c845a0c82d399f16a11e6e6

        return login_user(data=post_data)

@token_required
@api.route("/logout")
class LogoutAPI(Resource):
    @api.doc("logout a user")
    def post(self):
        auth_header = request.headers.get("Authorization")
        
        return logout_user(data=auth_header)
