from flask import request
from flask_restplus import Resource
from ..util.dto import PetDto
from ..util.decorator import token_required
from ..services.pet_service import save_new_pet, get_all_pets, get_a_pet, delete_pet, update_pet

api = PetDto.api
_pet = PetDto.pet
parser = PetDto.parser

@api.route("/")
class PetList(Resource):
    @token_required
    @api.doc("show list of all registered pets")
    @api.marshal_list_with(_pet, envelope="data")
    def get(self):
        return get_all_pets()

    @api.response(201, "Pet successfully created.")
    @api.doc("register a pet", parser=parser)
    def post(self):
        post_data = request.json

        return save_new_pet(data=post_data)

@api.route("/<public_id>")
@api.param("public_id", "The Pet identifier")
@api.response(404, "Pet not found.")
class User(Resource):
    @token_required
    @api.doc("get a pet")
    @api.marshal_with(_pet)
    def get(self, public_id):
        if public_id:
            pet = get_a_pet(public_id)

            if not pet:
                api.abort(404)

            else:
                return pet

    @token_required
    @api.doc("delete a pet")
    def delete(self, public_id):
        pet = delete_pet(public_id)

        if not pet:
            api.abort(404)
            
        else:
            return pet

    @token_required
    @api.doc("update a pet", parser=parser)
    def put(self, public_id):
        data = request.form

        pet = update_pet(public_id=public_id, data=data)
        if not pet:
            api.abort(404)

        else:
            return pet