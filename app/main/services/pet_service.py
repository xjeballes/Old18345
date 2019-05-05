import uuid, datetime
from app.main import db
from app.main.models.user import User
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
        sex = data["sex"],
        profPic_filename = data["profPicFilename"], 
        profPic_sm_filename = data["profPicSmallFilename"],
        owner_id = owner.id,
        registered_on = datetime.datetime.utcnow()
    )

    Helper.save_changes(new_pet)

    statement = pet_kind_rel.insert().values(pet_id=new_public_id, specie_id=data["specieId"], breed_id=data["breedId"])
            
    Helper.execute_changes(statement)

    return Helper.generate_token("Pet", new_pet)

def get_all_pets():
    return Pet.query.all()

def get_a_pet(public_id):
    pet = db.session.query(Pet.pet_name, Pet.public_id, Pet.sex, Specie.specie_name, Breed.breed_name, Pet.profPic_filename, Pet.profPic_sm_filename).filter(Pet.public_id==pet_kind_rel.c.pet_id).filter(pet_kind_rel.c.specie_id==Specie.public_id).filter(pet_kind_rel.c.breed_id==Breed.public_id).filter(Pet.public_id==public_id).first()
    
    pet_obj = {}
    
    pet_obj["pet_name"] = pet[0]
    pet_obj["public_id"] = pet[1]
    pet_obj["sex"] = pet[2]
    pet_obj["specie_name"] = pet[3]
    pet_obj["breed_name"] = pet[4]
    pet_obj["profPic_filename"] = pet[5]
    pet_obj["profPic_sm_filename"] = pet[6]

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

def get_user_pet(pet_name, username):
    user_id = User.query.filter_by(username=username).first().id
    pet = db.session.query(Pet.pet_name, Pet.public_id, Pet.sex, Specie.specie_name, Breed.breed_name, Pet.profPic_filename, Pet.profPic_sm_filename).filter(Pet.public_id==pet_kind_rel.c.pet_id).filter(pet_kind_rel.c.specie_id==Specie.public_id).filter(pet_kind_rel.c.breed_id==Breed.public_id).filter(Pet.owner_id==user_id).filter(Pet.pet_name==pet_name).first()
    
    pet_obj = {}
    
    pet_obj["pet_name"] = pet[0]
    pet_obj["public_id"] = pet[1]
    pet_obj["sex"] = pet[2]
    pet_obj["specie_name"] = pet[3]
    pet_obj["breed_name"] = pet[4]
    pet_obj["profPic_filename"] = pet[5]
    pet_obj["profPic_sm_filename"] = pet[6]
    
    return pet_obj

def get_user_pets(username):
    user_id = User.query.filter_by(username=username).first().id
    pets = db.session.query(Pet.pet_name, Pet.public_id, Pet.sex, Specie.specie_name, Breed.breed_name, Pet.profPic_filename, Pet.profPic_sm_filename).filter(Pet.public_id==pet_kind_rel.c.pet_id).filter(pet_kind_rel.c.specie_id==Specie.public_id).filter(pet_kind_rel.c.breed_id==Breed.public_id).filter(Pet.owner_id==user_id).all()
    
    pet_list = []
    
    for x, pet in enumerate(pets):
        pet_obj = {}
        
        pet_obj["pet_name"] = pet[0]
        pet_obj["public_id"] = pet[1]
        pet_obj["sex"] = pet[2]
        pet_obj["specie_name"] = pet[3]
        pet_obj["breed_name"] = pet[4]
        pet_obj["profPic_filename"] = pet[5]
        pet_obj["profPic_sm_filename"] = pet[6]

        pet_list.append(pet_obj)

    return pet_list

def get_specie_pets(specie_id):
    pets = db.session.query(Pet.pet_name, Pet.public_id, Pet.sex, Specie.specie_name, Breed.breed_name, Pet.profPic_filename, Pet.profPic_sm_filename).filter(Pet.public_id==pet_kind_rel.c.pet_id).filter(pet_kind_rel.c.specie_id==Specie.public_id).filter(pet_kind_rel.c.breed_id==Breed.public_id).filter(pet_kind_rel.c.specie_id==specie_id).all()
    
    pet_list = []
    
    for x, pet in enumerate(pets):
        pet_obj = {}
        
        pet_obj["pet_name"] = pet[0]
        pet_obj["public_id"] = pet[1]
        pet_obj["sex"] = pet[2]
        pet_obj["specie_name"] = pet[3]
        pet_obj["breed_name"] = pet[4]
        pet_obj["profPic_filename"] = pet[5]
        pet_obj["profPic_sm_filename"] = pet[6]

        pet_list.append(pet_obj)

    return pet_list

def get_breed_pets(breed_id):
    pets = db.session.query(Pet.pet_name, Pet.public_id, Pet.sex, Specie.specie_name, Breed.breed_name, Pet.profPic_filename, Pet.profPic_sm_filename).filter(Pet.public_id==pet_kind_rel.c.pet_id).filter(pet_kind_rel.c.specie_id==Specie.public_id).filter(pet_kind_rel.c.breed_id==Breed.public_id).filter(pet_kind_rel.c.breed_id==breed_id).all()
    
    pet_list = []
    
    for x, pet in enumerate(pets):
        pet_obj = {}
        
        pet_obj["pet_name"] = pet[0]
        pet_obj["public_id"] = pet[1]
        pet_obj["sex"] = pet[2]
        pet_obj["specie_name"] = pet[3]
        pet_obj["breed_name"] = pet[4]
        pet_obj["profPic_filename"] = pet[5]
        pet_obj["profPic_sm_filename"] = pet[6]

        pet_list.append(pet_obj)

    return pet_list