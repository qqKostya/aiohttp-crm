from marshmallow import Schema, fields

from app.web.schemes import OkResponseSchema


class UserSchema(Schema):
    email = fields.Str(required=True)


class ListUsersSchema(Schema):
    users = fields.Nested(UserSchema, many=True)


class ListUsersResponseSchema(OkResponseSchema):
    data = fields.Nested(ListUsersSchema)
