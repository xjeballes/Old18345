import uuid, datetime
from app.main import db
from app.main.models.user import User, user_pet_rel
from app.main.models.pet import Pet, pet_kind_rel
from app.main.models.specie import Specie
from app.main.models.breed import Breed
from app.main.services.help import Helper

def save_new_pet(data, username):
    new_public_id = str(uuid.uuid4())

    owner = User.query.filter_by(username=username).first()
    
    new_pet = Pet(
        public_id = new_public_id,
        pet_name = data["petName"],
        bio = data["bio"],
        birthday = data["birthday"],
        sex = data["sex"],
        profPic_filename = data["profPicFilename"],
        registered_on = datetime.datetime.utcnow()
    )

    Helper.save_changes(new_pet)

    statement_one = user_pet_rel.insert().values(user_id=owner.public_id, pet_id=new_public_id)

    statement_two = pet_kind_rel.insert().values(pet_id=new_public_id, specie_id=data["specieId"], breed_id=data["breedId"])

    Helper.execute_changes(statement_one)

    Helper.execute_changes(statement_two)

    return Helper.generate_token("Pet", new_pet)

def get_all_pets():
    return Pet.query.all()

def get_a_pet(public_id):
    pet = db.session.query(Pet.public_id, Pet.pet_name, Pet.bio, Pet.birthday, Pet.sex, Pet.profPic_filename, Specie.specie_name, Breed.breed_name).filter(Pet.public_id==public_id).filter(pet_kind_rel.c.pet_id==Pet.public_id).filter(Specie.public_id==pet_kind_rel.c.specie_id).filter(Breed.public_id==pet_kind_rel.c.breed_id).first()
    print(pet)
    pet_obj = {}

    pet_obj["public_id"] = pet[0]
    pet_obj["pet_name"] = pet[1]
    pet_obj["bio"] = pet[2]
    pet_obj["birthday"] = pet[3]
    pet_obj["sex"] = pet[4]
    pet_obj["profPic_filename"] = pet[5]
    pet_obj["specie_name"] = pet[6]
    pet_obj["breed_name"] = pet[7]

    return pet_obj

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

def get_user_pets(username):
    user_id = User.query.filter_by(username=username).first().public_id

    pets = db.session.query(Pet.public_id, Pet.pet_name, Pet.bio, Pet.birthday, Pet.sex, Pet.profPic_filename, User.first_name, User.last_name, Specie.specie_name, Breed.breed_name).filter(User.public_id==user_id).filter(user_pet_rel.c.user_id==User.public_id).filter(user_pet_rel.c.pet_id==Pet.public_id).filter(pet_kind_rel.c.pet_id==user_pet_rel.c.pet_id).filter(pet_kind_rel.c.specie_id==Specie.public_id).filter(pet_kind_rel.c.breed_id==Breed.public_id).filter(Breed.specie_id==Specie.public_id).all()

    pet_list = []

    for x, pet in enumerate(pets):
        pet_obj = {}
        
        pet_obj["public_id"] = pet[0]
        pet_obj["pet_name"] = pet[1]
        pet_obj["bio"] = pet[2]
        pet_obj["birthday"] = pet[3]
        pet_obj["sex"] = pet[4]
        pet_obj["profPic_filename"] = pet[5]
        pet_obj["owner_firstName"] = pet[6]
        pet_obj["owner_lastName"] = pet[7]
        pet_obj["specie_name"] = pet[8]
        pet_obj["breed_name"] = pet[9]

        pet_list.append(pet_obj)

    return pet_list

def get_specie_pets(specie_id):
    pets = db.session.query(Pet.pet_name, Pet.public_id, Pet.sex, Specie.specie_name, Breed.breed_name, Pet.profPic_filename).filter(Pet.public_id==pet_kind_rel.c.pet_id).filter(pet_kind_rel.c.specie_id==Specie.public_id).filter(pet_kind_rel.c.breed_id==Breed.public_id).filter(pet_kind_rel.c.specie_id==specie_id).all()
    
    pet_list = []
    
    for x, pet in enumerate(pets):
        pet_obj = {}
        
        pet_obj["pet_name"] = pet[0]
        pet_obj["public_id"] = pet[1]
        pet_obj["sex"] = pet[2]
        pet_obj["specie_name"] = pet[3]
        pet_obj["breed_name"] = pet[4]
        pet_obj["profPic_filename"] = pet[5]

        pet_list.append(pet_obj)

    return pet_list

def get_breed_pets(breed_id):
    pets = db.session.query(Pet.pet_name, Pet.public_id, Pet.sex, Specie.specie_name, Breed.breed_name, Pet.profPic_filename).filter(Pet.public_id==pet_kind_rel.c.pet_id).filter(pet_kind_rel.c.specie_id==Specie.public_id).filter(pet_kind_rel.c.breed_id==Breed.public_id).filter(pet_kind_rel.c.breed_id==breed_id).all()
    
    pet_list = []
    
    for x, pet in enumerate(pets):
        pet_obj = {}
        
        pet_obj["pet_name"] = pet[0]
        pet_obj["public_id"] = pet[1]
        pet_obj["sex"] = pet[2]
        pet_obj["specie_name"] = pet[3]
        pet_obj["breed_name"] = pet[4]
        pet_obj["profPic_filename"] = pet[5]

        pet_list.append(pet_obj)

    return pet_list