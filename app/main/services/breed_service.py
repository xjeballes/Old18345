import uuid, datetime
from app.main import db
from app.main.models.breed import Breed
from app.main.services.help import Helper

def save_new_breed(data):
    new_breed = Breed(
        public_id = str(uuid.uuid4()),
        breed_name = data["breedName"],
        specie_id = data["specieId"]
    )

    Helper.save_changes(new_breed)

    return Helper.generate_token(new_breed)

def get_all_breeds():
    return Breed.query.all()

def get_specie_breeds(specie_id):
    return Breed.query.filter_by(specie_id=specie_id).all()

def get_a_breed(public_id):
    return Breed.query.filter_by(public_id=public_id).first()

def delete_breed(public_id):
    breed = Breed.query.filter_by(public_id=public_id).first()

    if breed:
        db.session.delete(breed)

        db.session.commit()

        return Helper.return_resp_obj("success", "Breed deleted successfully.", None, 200)

    else:
        return Helper.return_resp_obj("fail", "No breed found.", None, 409)

def update_breed(public_id, data):
    breed = Breed.query.filter_by(public_id=public_id).first()
    
    breed.breed_name = data["breedName"]

    db.session.commit()

    return Helper.return_resp_obj("success", "Breed updated successfully.", None, 200)

def save_changes(data):
    db.session.add(data)

    db.session.commit()

def generate_token(breed):
    try:
        auth_token = Helper.encode_auth_token(breed.public_id)

        return Helper.return_resp_obj("success", "Breed registered successfully.", auth_token, 201)

    except Exception as e:
        return Helper.return_resp_obj("fail", "Some error occured.", None, 401)