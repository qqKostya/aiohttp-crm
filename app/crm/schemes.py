from marshmallow import Schema, fields

class UserSchem(Schema):
    email = fields.Str(required=True)
    