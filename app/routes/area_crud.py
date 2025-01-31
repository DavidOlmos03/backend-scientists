"""
    Area CRUD
"""
from flask_restx import Namespace, Resource, fields
# from flask import request
from app.services.area_service import (
    get_all_areas
)

category_api = Namespace('categories', description='Operations related to categories')

category_model = category_api.model('Category', {
    'id': fields.Integer(readonly=True),
    'name': fields.String(required=True, description='The name of the category')
})

@category_api.route('/')
class CategoryList(Resource):
    """
        List all categories
    """
    @category_api.marshal_list_with(category_model)
    def get(self):
        """
            Returns all categories
        """
        return get_all_areas()

    # @category_api.expect(category_model)
    # def post(self):
    #     data = request.get_json()
    #     return {'id': data['id'], 'name': data['name']}, 201
