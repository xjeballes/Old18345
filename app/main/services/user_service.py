import datetime, uuid
from app.main import db
from app.main.models.user import User, user_pet_rel
from app.main.services.help import Helper

def save_new_user(data):
    user = User.query.filter_by(email=data["email"]).first()

    check_first_user = User.query.filter_by(id=1).first()
    
    if not check_first_user:
        is_admin = True
    else:
        is_admin = False
        
    if not user:
        new_user = User(
            public_id = str(uuid.uuid4()),
            first_name = data["firstName"],
            last_name = data["lastName"],
            email = data["email"],
            username = data["username"],
            password = data["password"],
            contact_no = data["contactNo"],
            registered_on = datetime.datetime.utcnow(),
            admin = is_admin
        )

        Helper.save_changes(new_user)

        return Helper.generate_token("User", new_user)

    else:
        return Helper.return_resp_obj("fail", "User already exists. Please log in instead.", None, 409)

def get_all_users():
    return User.query.all()

def get_a_user(username):
    return User.query.filter_by(username=username).first()

def delete_user(username):
    user = User.query.filter_by(username=username).first()

    if user:
        db.session.delete(user)

        db.session.commit()

        return Helper.return_resp_obj("success", "User deleted successfully.", None, 200)

    else:
        return Helper.return_resp_obj("fail", "No user found.", None, 409)

def update_user(username, data):
    user = User.query.filter_by(username=username).first()
    
    if user:
        if User.query.filter_by(email=data["email"]).count() == 0 or User.query.filter_by(email=data["email"]).count() == 1 and user.email == data["email"]:
            user.first_name = data["firstName"]
            user.last_name = data["lastName"]
            user.email = data["email"]
            user.username = data["username"]
            user.contact_no = data["contactNo"]

            db.session.commit()

            return Helper.return_resp_obj("success", "User updated successfully.", None, 200)

        else:
            return Helper.return_resp_obj("fail", "Email or username is already used.", None, 409)
    else:
        return Helper.return_resp_obj("fail", "No user found.", None, 409)

def get_logged_in_user(new_request):
    auth_token = new_request.headers.get("authorization")

    if auth_token:
        public_id_resp = Helper.decode_auth_token(auth_token)
        
        user = User.query.filter_by(public_id=public_id_resp).first()

        if user:
            response_object = {
                "status" : "success",
                "data" : {
                    "firstName" : user.first_name,
                    "lastName" : user.last_name,
                    "email" : user.email,
                    "username" : user.username,
                    "contactNo" : user.contact_no,
                    "admin" : user.admin,
                    "registeredOn" : str(user.registered_on)
                }
            }

            return response_object, 200

        else:
            response_object = {
                "status" : "fail",
                "message": "Provide a valid authorized token."
            }

            return response_object, 401

    else:
        response_object = {
            "status": "fail",
            "message": "Provide a valid authorized token."
        }

        return response_object, 401

def get_pet_owners(public_id):
    users = db.session.query(User.first_name, User.last_name, User.bio, User.email, User.username, User.contact_no).filter(user_pet_rel.c.user_id==User.public_id).filter(user_pet_rel.c.pet_id==public_id).all()

    user_list = []
    
    for x, user in enumerate(users):
        user_obj = {}
        
        user_obj["first_name"] = user[0]
        user_obj["last_name"] = user[1]
        user_obj["bio"] = user[2]
        user_obj["email"] = user[3]
        user_obj["username"] = user[4]
        user_obj["contact_no"] = user[5]

        user_list.append(user_obj)

    return user_list
