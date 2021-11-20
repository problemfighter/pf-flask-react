from marshmallow import fields, Schema

from pfms.pfapi.base.pfms_base_schema import PfBaseSchema


class LoginDto(PfBaseSchema):
    identifier = fields.String(required=True, error_messages={"required": "Please enter identifier."})
    password = fields.String(required=True, error_messages={"required": "Please enter password."})


class LoginTokenDto(PfBaseSchema):
    accessToken = fields.String()
    refreshToken = fields.String()


class OperatorDto(PfBaseSchema):
    firstName = fields.String()
    lastName = fields.String()
    name = fields.String()
    email = fields.String()
    username = fields.String()
    id = fields.Integer()


class LoginResponseDto(PfBaseSchema):
    loginToken = fields.Nested(LoginTokenDto)
    operator = fields.Nested(OperatorDto)


class RefreshTokenDto(PfBaseSchema):
    refreshToken = fields.String()


class RefreshTokenResponseDto(PfBaseSchema):
    loginToken = fields.Nested(LoginTokenDto)
