from flask_restful import Resource
from HW_models import *
from flask import request
from HW_schemas import *
import json
from marshmallow import ValidationError


class CategoryResource(Resource):

    def get(self, category_id=None):
        if category_id:
            res = json.loads(CategorySchema().dumps(Category.read(category_id=category_id)))
        else:
            res = json.loads(CategorySchema(many=True).dumps(Category.read(category_id=category_id)))
        return res

    def post(self):
        data = json.dumps(request.json)
        try:
            data = CategorySchema().loads(data)
            category = Category.create(**data)
            res = json.loads(CategorySchema().dumps(category))
        except ValidationError as err:
            res = err.messages
        return res

    def put(self, category_id):
        if category_id:
            category = Category.objects.filter(id=category_id)[0]
            category.update(**request.json)
            return 'Category_updated'

    def delete(self, category_id):
        Category.delete(category_id)
        return 'Category_deleted'


class ItemResource(Resource):

    def get(self, category_id, item_id):
        return json.loads(ItemSchema().dumps(Item.read(item_id)))

    def post(self, category_id, item_id=None):
        category = Category.objects.get(id=category_id)
        data = json.dumps(request.json)
        try:
            data = ItemSchema().loads(data)
            res = json.loads(ItemSchema().dumps(Item.create(category, **data)))
        except ValidationError as err:
            res = err.messages
        return res

    def put(self, category_id, item_id):

        if item_id:
            item = Item.objects.filter(id=item_id)[0]
            category = Category.objects.filter(id=category_id)[0]
            Item.update(item, category, **request.json)
            return 'Item_updated'

    def delete(self, item_id):
        Item.delete(item_id)
        return 'Item_deleted'


class TotalResource(Resource):

    def get(self):
        return Total.read(self)
