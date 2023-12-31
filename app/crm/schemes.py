from marshmallow import Schema, fields

from app.web.schemes import OkResponseSchema


class UserAddSchema(Schema):
    email = fields.Str(required=True)


class UserSchema(UserAddSchema):
    id = fields.UUID(required=True, attribute="id_")


class UserGetRequestSchema(Schema):
    id = fields.UUID(required=True)


class UsetGetSchema(Schema):
    user = fields.Nested(UserSchema)


class GetUserResponseSchema(OkResponseSchema):
    data = fields.Nested(UsetGetSchema)


class ListUsersSchema(Schema):
    users = fields.Nested(UserSchema, many=True)


class ListUsersResponseSchema(OkResponseSchema):
    data = fields.Nested(ListUsersSchema)
