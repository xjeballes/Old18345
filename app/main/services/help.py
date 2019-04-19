import datetime, jwt
from app.main import db
from app.main.models.blacklist import BlacklistToken
from ..config import key

class Helper:
    @staticmethod
    def return_resp_obj(status, payload, token, code):
        response_obj = {
            "status" : status,
            "payload" : payload
            }

        if token:
            response_obj["Authorization"] = token.decode()

        return response_obj, code
        
    @staticmethod
    def save_changes(method, data):
        db.session.add(data)

        db.session.commit()

    @staticmethod
    def generate_token(user):
        try:
            auth_token = Helper.encode_auth_token(user.public_id)

            return Helper.return_resp_obj("success", "User is successfully registered.", auth_token, 201)

        except Exception as e:
            return Helper.return_resp_obj("fail", "Some error occured.", None, 401)

    @staticmethod
    def encode_auth_token(public_id):
        try:
            payload = {
                "exp" : datetime.datetime.utcnow() + datetime.timedelta(days=3650),
                "iat" : datetime.datetime.utcnow(),
                "sub" : public_id
            }
            return jwt.encode(
                payload,
                key,
                algorithm = "HS256"
            )

        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, key)

            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)

            if is_blacklisted_token:
                return "Token has been blacklisted. Please log in again."

            else:
                return payload["sub"]

        except jwt.ExpiredSignatureError:
            return "Signature has expired. Please log in again."

        except jwt.InvalidTokenError:
            return "Token is invalid. Please log in again."