from marshmallow import Schema, fields, validate, ValidationError


def validate_name(value):
    if all([value.is_alpha(), len(value) >= 3]):
        return value
    else:
        raise ValidationError(message={'name error': 'Invalid data'})


class AuthorSchema(Schema):
    id = fields.String(load_only=True)
    name = fields.String(required=True, validate=validate_name)
    surname = fields.String(required=True, validate=validate_name)
    posts = fields.Integer(dump_only=True)


class TagSchema(Schema):
    id = fields.String(load_only=True)
    tag = fields.String(required=True, validate=validate.Length(min=2))


class PostSchema(Schema):
    id = fields.String(load_only=True)
    title = fields.String(required=True, validate=validate.Length(min=5, max=128))
    text = fields.String(required=True, validate=validate.Length(min=5, max=4096))
    date = fields.Date(dump_only=True)
    author = fields.Nested(AuthorSchema, dump_only=True)
    views = fields.Integer(dump_only=True)
    tag = fields.Nested(TagSchema, dump_only=True)
