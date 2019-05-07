from app.main import db
from app.main.models.breed import Breed

def save_new_breed(data):
    breed = Breed.query.filter_by(breed_name=data["breedName"]).first()
    breed_id = str(uuid.uuid4())

    if not breed:
        new_breed = Breed(
            public_id = breed_id,
            specie_id = data["specieId"],
            breed_name = data["breedName"]
        )

        Helper.save_changes(new_breed)

        return Helper.return_resp_obj("success", "Breed added successfully.", None, 200)

    else:
        return Helper.return_resp_obj("fail", "Breed already exists. Try again.", None, 409)

def get_all_breeds():
    return Breed.query.all()

def get_specie_breeds(specie_id):
    return Breed.query.filter_by(specie_id=specie_id).all()

def get_a_breed(public_id):
    return Breed.query.filter_by(public_id=public_id).first()