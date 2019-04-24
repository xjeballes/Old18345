from flask import request
from flask_restplus import Resource
from ..util.dto import CircleDto
from ..util.decorator import token_required
from ..services.circle_service import save_new_circle, get_all_circles, get_a_circle, delete_circle, update_circle

api = CircleDto.api
_circle = CircleDto.circle
parser = CircleDto.parser

@api.route("/")
class CircleList(Resource):
    @token_required
    @api.doc("show list of all registered circles")
    @api.marshal_list_with(_circle, envelope="data")
    def get(self):
        return get_all_circles()

    @api.response(201, "Circle successfully created.")
    @api.doc("register a circle", parser=parser)
    def post(self):
        post_data = request.json

        return save_new_circle(data=post_data)

@api.route("/<public_id>")
@api.param("public_id", "The circle identifier")
@api.response(404, "Circle not found.")
class Circle(Resource):
    @token_required
    @api.doc("get a circle")
    @api.marshal_with(_circle)
    def get(self, public_id):
        circle = get_a_circle(public_id)

        if not circle:
            api.abort(404)

        else:
            return circle

    @token_required
    @api.doc("delete a circle")
    def delete(self, public_id):
        circle = delete_circle(public_id)

        if not circle:
            api.abort(404)
            
        else:
            return circle

    @token_required
    @api.doc("update a circle", parser=parser)
    def put(self, public_id):
        post_data = request.json

        circle = update_circle(public_id=public_id, data=post_data)
        
        if not circle:
            api.abort(404)

        else:
            return circle
