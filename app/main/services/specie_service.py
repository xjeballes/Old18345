import uuid, datetime
from app.main import db
from app.main.models.specie import Specie
from app.main.services.help import Helper

def save_new_specie(data):
    new_specie = Specie(
        public_id = str(uuid.uuid4()),
        specie_name = data["specieName"]
    )

    Helper.save_changes(new_specie)

    return Helper.generate_token(new_specie)

def get_all_species():
    return Specie.query.all()

def get_a_specie(public_id):
    return Specie.query.filter_by(public_id=public_id).first()

def delete_specie(public_id):
    specie = Specie.query.filter_by(public_id=public_id).first()

    if specie:
        db.session.delete(specie)

        db.session.commit()

        return Helper.return_resp_obj("success", "Specie deleted successfully.", None, 200)

    else:
        return Helper.return_resp_obj("fail", "No specie found.", None, 409)

def update_specie(public_id, data):
    specie = Specie.query.filter_by(public_id=public_id).first()
    
    specie.specie_name = data["specieName"]

    db.session.commit()

    return Helper.return_resp_obj("success", "Specie updated successfully.", None, 200)

def save_changes(data):
    db.session.add(data)

    db.session.commit()

def generate_token(specie):
    try:
        auth_token = Helper.encode_auth_token(specie.public_id)

        return Helper.return_resp_obj("success", "Specie registered successfully.", auth_token, 201)

    except Exception as e:
        return Helper.return_resp_obj("fail", "Some error occured.", None, 401)