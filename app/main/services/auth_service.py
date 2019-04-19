import datetime, jwt, json
from app.main.models.user import User
from ..services.blacklist_service import save_token_to_blacklist
from ..services.user_service import get_a_user
from app.main.services.help import Helper

def login_user(data):
    try:
        print(data.get("usernameOrEmail"))
        user = User.query.filter_by(email=data.get("usernameOrEmail")).first()

        if user and user.check_password(data.get("password")):
            auth_token = Helper.encode_auth_token(user.public_id)

            if auth_token:
                return Helper.return_resp_obj("success", {"message" : "Successfully logged in.", "username" : user.username}, auth_token, 200)

        elif user is None:
            user = User.query.filter_by(username=data.get("usernameOrEmail")).first()

            if user and user.check_password(data.get("password")):
                auth_token = Helper.encode_auth_token(user.public_id)

                if auth_token:
                    return Helper.return_resp_obj("success", {"message" : "Successfully logged in.", "username" : user.username}, auth_token, 200)

            else:
                return Helper.return_resp_obj("fail", "Log in unsuccessful. Try again.", None, 401)

        else:
            return Helper.return_resp_obj("fail", "Log in unsuccessful. Try again.", None, 401)

    except Exception as e:
        return Helper.return_resp_obj("fail", "Try again.", None, 500)

def logout_user(data):
    if data:
        auth_token = data.split(" ")[0]

    else:
        auth_token = ""
        
    if auth_token:
        resp = Helper.decode_auth_token(auth_token)

        if not isinstance(resp, str):
            return save_token_to_blacklist(token=auth_token)

        else:
            response_object = {
                "status" : "fail",
                "message" : resp
            }

            return response_object, 401
    else:
        response_object = {
            "status" : "fail",
            "message" : "Provide a valid authorized token."
        }

        return response_object, 403
