import uuid
from app.main import db
from app.main.models.specie import Specie
from app.main.services.help import Helper

def save_new_specie(data):
    specie = Specie.query.filter_by(specie_name=data["specieName"]).first()
    specie_id = str(uuid.uuid4())

    if not specie:
        new_specie = Specie(
            public_id = specie_id,
            specie_name = data["specieName"]
        )

        Helper.save_changes(new_specie)

        return Helper.return_resp_obj("success", "Specie added succesfully. Specie ID: {}".format(specie_id), None, 200)

    else:
        return Helper.return_resp_obj("fail", "Specie already exists. Try again.", None, 409)

def get_all_species():
    return Specie.query.all()

def get_a_specie(public_id):
    return Specie.query.filter_by(public_id=public_id).first()