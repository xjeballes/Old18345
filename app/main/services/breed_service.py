from app.main import db
from app.main.models.breed import Breed

def get_specie_breeds(specie_id):
    return Breed.query.filter_by(specie_id=specie_id).all()

def get_a_breed(public_id):
    return Breed.query.filter_by(public_id=public_id).first()