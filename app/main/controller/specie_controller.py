from flask_restplus import Resource
from ..util.dto import SpecieDto
from ..util.decorator import *
from ..services.specie_service import *

api = SpecieDto.api
_specie = SpecieDto.specie
parser = SpecieDto.parser

@api.route("/")
class SpecieList(Resource):
    @token_required
    @api.doc("show list of all registered species")
    @api.marshal_list_with(_specie, envelope="data")
    def get(self):
        return get_all_species()

    @admin_token_required
    @api.response(201, "Specie successfully created.")
    @api.doc("register a specie", parser=parser)
    def post(self):
        post_data = request.json

        return save_new_specie(data=post_data)

@api.route("/<public_id>")
@api.param("public_id", "The Specie identifier")
@api.response(404, "Specie not found.")
class Specie(Resource):
    @token_required
    @api.doc("get a specie")
    @api.marshal_with(_specie)
    def get(self, public_id):
        specie = get_a_specie(public_id)

        if not specie:
            api.abort(404)

        else:
            return specie