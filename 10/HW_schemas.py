from marshmallow import Schema, fields, validate


class CategorySchema(Schema):
    id = fields.String(load_only=True)
    title = fields.String(required=True)
    description = fields.String()


class ItemSchema(Schema):
    id = fields.String(load_only=True)
    name = fields.String(required=True)
    price = fields.Float(required=True)
    availability = fields.Integer(required=True, load_only=True)
    quantity = fields.Integer(validate=validate.Range(min=0))
    category = fields.Nested(CategorySchema, load_only=True)
    views = fields.Integer(dump_only=True)
