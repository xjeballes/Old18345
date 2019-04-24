from flask import request
from flask_restplus import Resource
from ..util.dto import BusinessDto
from ..util.decorator import token_required
from ..services.business_service import save_new_business, get_all_businesses, get_a_business, delete_business, update_business

api = BusinessDto.api
_business = BusinessDto.business
parser = BusinessDto.parser

@api.route("/")
class BusinessList(Resource):
    @token_required
    @api.doc("show list of all registered businesss")
    @api.marshal_list_with(_business, envelope="data")
    def get(self):
        return get_all_businesses()

    @api.response(201, "Business successfully created.")
    @api.doc("register a business", parser=parser)
    def post(self):
        post_data = request.json

        return save_new_business(data=post_data)

@api.route("/<public_id>")
@api.param("public_id", "The business identifier")
@api.response(404, "Business not found.")
class Business(Resource):
    @token_required
    @api.doc("get a business")
    @api.marshal_with(_business)
    def get(self, public_id):
        business = get_a_business(public_id)

        if not business:
            api.abort(404)

        else:
            return business

    @token_required
    @api.doc("delete a business")
    def delete(self, public_id):
        business = delete_business(public_id)

        if not business:
            api.abort(404)
            
        else:
            return business

    @token_required
    @api.doc("update a business", parser=parser)
    def put(self, public_id):
        post_data = request.json

        business = update_business(public_id=public_id, data=post_data)
        
        if not business:
            api.abort(404)

        else:
            return business
