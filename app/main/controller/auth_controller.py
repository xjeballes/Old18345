from flask import request
from flask_restplus import Resource

from app.main.services.auth_helper import Auth
from ..util.dto import AuthDto
from ..util.decorator import token_required

api = AuthDto.api
user_auth = AuthDto.user_auth
parser = AuthDto.parser


@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login', parser=parser)
    def post(self):
        # get the post data
        post_data = request.form
        return Auth.login_user(data=post_data)


@token_required
@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    def post(self):
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)
