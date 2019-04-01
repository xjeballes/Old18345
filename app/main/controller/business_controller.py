from flask import request
from flask_restplus import Resource

from ..util.dto import BusinessDto
from ..util.decorator import token_required
from ..services.business_service import create_new_business, delete_business, get_all_business, get_business

api = BusinessDto.api
_business = BusinessDto.business


@api.route('/')
class BusinessList(Resource):
    @token_required
    @api.doc('list_of_businesses')
    @api.marshal_list_with(_business, envelope='data')
    def get(self):
        return get_all_business()

    @token_required
    @api.response(201, 'Your business has been created successfully.')
    @api.doc('create a new business')
    @api.expect(_business, validate=True)
    def post(self):
        data = request.json
        return create_new_business(data=data)


@api.route('/<business_name>')
@api.param('business_name', 'business identifier')
@api.response(404, 'User not found.')
class business(Resource):
    @token_required
    @api.doc('get a business')
    @api.marshal_with(_business)
    def get(self, business_name):
        business = get_business(business_name)
        if not business:
            api.abort(404)
        else:
            return business

    @token_required
    @api.doc('remove a business')
    @api.marshal_with(_business)
    def delete(self, business_name):
        business = delete_business(business_name)
        if not business:
            api.abort(404)
        else:
            return business
