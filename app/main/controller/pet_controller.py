from flask import request
from flask_restplus import Resource
from ..util.dto import PetDto
from ..util.decorator import token_required
from ..services.user_service import get_logged_in_user
from ..services.pet_service import *
from ..services.help import Helper

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

    @token_required
    @api.response(201, "Pet successfully created.")
    @api.doc("register a pet", parser=parser)
    def post(self):
        post_data = request.json

        user = get_logged_in_user(request)
        
        user_username = user[0]["data"]["username"]
        
        return save_new_pet(data=post_data, username=user_username)

@api.route("/user/<username>")
@api.param("username", "Pets of a specific owner")
@api.response(404, "Pets not found.")
class UserPets(Resource):
    @token_required
    @api.doc("get pets with specific owner")
    @api.marshal_list_with(_pet, envelope="data")
    def get(self, username):
        pets = get_user_pets(username=username)

        return pets

@api.route("/specie/<specie_id>")
@api.param("specie_id", "Pets with specific specie")
@api.response(404, "Pets not found.")
class SpeciePets(Resource):
    @token_required
    @api.doc("get pets with specific specie")
    @api.marshal_list_with(_pet, envelope="data")
    def get(self, specie_id):
        pets = get_specie_pets(specie_id=specie_id)

        return pets

@api.route("/breed/<breed_id>")
@api.param("breed_id", "Pets with specific breed")
@api.response(404, "Pets not found.")
class SpeciePets(Resource):
    @token_required
    @api.doc("get pets with specific breed")
    @api.marshal_list_with(_pet, envelope="data")
    def get(self, breed_id):
        pets = get_breed_pets(breed_id=breed_id)

        return pets

@api.route("/<public_id>")
@api.param("public_id", "The Pet identifier")
@api.response(404, "Pet not found.")
class Pet(Resource):
    @token_required
    @api.doc("get a pet")
    @api.marshal_with(_pet)
    def get(self, public_id):
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
        post_data = request.json

        pet = update_pet(public_id=public_id, data=post_data)
        
        if not pet:
            api.abort(404)

        else:
            return pet