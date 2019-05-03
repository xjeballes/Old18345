from flask_restplus import Resource
from ..util.dto import BreedDto
from ..util.decorator import token_required
from ..services.breed_service import *

api = BreedDto.api
_breed = BreedDto.breed
parser = BreedDto.parser

@api.route("/<public_id>")
@api.param("public_id", "The Breed identifier")
@api.response(404, "Breed not found.")
class Breed(Resource):
    @token_required
    @api.doc("get a breed")
    @api.marshal_with(_breed)
    def get(self, public_id):
        breed = get_a_breed(public_id)

        if not breed:
            api.abort(404)

        else:
            return breed

@api.route("/specie/<specie_id>")
@api.param("specie_id", "Breeds with specific specie")
@api.response(404, "Breeds not found.")
class SpecieBreeds(Resource):
    @token_required
    @api.doc("get breeds with specific specie")
    @api.marshal_list_with(_breed, envelope="data")
    def get(self, specie_id):
        breeds = get_specie_breeds(specie_id=specie_id)

        if not breeds:
            api.abort(404)

        else:
            return breeds