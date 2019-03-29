from flask import request
from flask_restplus import Resource

from ..util.dto import CircleDto
from ..util.decorator import token_required
from ..services.circle_service import create_new_circle, delete_circle, get_all_circle, get_circle

api = CircleDto.api
_circle = CircleDto.circle


@api.route('/')
class CircleList(Resource):
    @token_required
    @api.doc('list_of_circles')
    @api.marshal_list_with(_circle, envelope='data')
    def get(self):
        return get_all_circle()

    @token_required
    @api.response(201, 'Circle successfully created.')
    @api.doc('create a new circle')
    @api.expect(_circle, validate=True)
    def post(self):
        data = request.json
        return create_new_circle(data=data)


@api.route('/<circle_name>')
@api.param('circle_name', 'The Circle identifier')
@api.response(404, 'User not found.')
class Circle(Resource):
    @token_required
    @api.doc('get a circle')
    @api.marshal_with(_circle)
    def get(self, circle_name):
        circle = get_circle(circle_name)
        if not circle:
            api.abort(404)
        else:
            return circle

    @token_required
    @api.doc('remove a circle')
    @api.marshal_with(_circle)
    def delete(self, circle_name):
        circle = delete_circle(circle_name)
        if not circle:
            api.abort(404)
        else:
            return circle
