import uuid, datetime
from app.main import db
from app.main.models.user import User
from app.main.models.pet import Pet, pet_kind_rel
from app.main.services.help import Helper

def save_new_pet(data):
    new_public_id = str(uuid.uuid4())
    ownerId = User.query.filter_by(username=data["ownerUsername"]).first()
    new_pet = Pet(
        public_id = new_public_id,
        pet_name = data["petName"],
        sex = data["sex"],
        owner_id = ownerId.id,
        registered_on = datetime.datetime.utcnow()
    )

    Helper.save_changes(new_pet)

    statement = pet_kind_rel.insert().values(pet_id=new_public_id, specie_id=data["specieId"], breed_id=data["breedId"])
            
    Helper.execute_changes(statement)

    return Helper.generate_token("Pet", new_pet)

def get_all_pets():
    return Pet.query.all()

def get_a_pet(public_id):
    return Pet.query.filter_by(public_id=public_id).first()

def delete_pet(public_id):
    pet = Pet.query.filter_by(public_id=public_id).first()

    if pet:
        db.session.delete(pet)

        db.session.commit()

        return Helper.return_resp_obj("success", "Pet deleted successfully.", None, 200)

    else:
        return Helper.return_resp_obj("fail", "No pet found.", None, 409)

def update_pet(public_id, data):
    pet = Pet.query.filter_by(public_id=public_id).first()
    
    pet.pet_name = data["petName"]
    pet.sex = data["sex"]

    db.session.commit()

    return Helper.return_resp_obj("success", "Pet updated successfully.", None, 200)