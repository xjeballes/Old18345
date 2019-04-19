import uuid, datetime

from app.main import db
from app.main.models.pet import Pet
from app.main.services.help import Helper

def save_new_pet(data):
    new_pet = Pet(
        public_id = str(uuid.uuid4()),
        pet_name = data["petName"],
        sex = data["sex"],
        registered_on = datetime.datetime.utcnow()
    )

    Helper.save_changes(new_user)

    return Helper.generate_token(new_user)

def get_all_pets():
    return Pet.query.all()

def get_a_pet(public_id):
    return Pet.query.filter_by(public_id=public_id).first()

def delete_pet(public_id):
    pet = Pet.query.filter_by(public_id=public_id).first()

    if pet:
        db.session.delete(pet)

        db.session.commit()

        return Helper.return_resp_obj("success", "Pet has been deleted.", None, 200)

    else:
        return Helper.return_resp_obj("fail", "No pet found.", None, 409)

def update_pet(public_id, data):
    pet = Pet.query.filter_by(public_id=public_id).first()
    
    user.first_name = data["firstName"]
    user.last_name = data["lastName"]
    user.email = data["email"]
    user.username = data["username"]
    user.contact_no = data["contactNo"]

    db.session.commit()

    return Helper.return_resp_obj("success", "User has been updated.", None, 200)

def save_changes(data):
    db.session.add(data)

    db.session.commit()

def generate_token(pet):
    try:
        auth_token = Helper.encode_auth_token(pet.public_id)

        return Helper.return_resp_obj("success", "Pet is successfully registered.", auth_token, 201)

    except Exception as e:
        return Helper.return_resp_obj("fail", "Some error occured.", None, 401)