from flask import Blueprint

from pf_auth.dto.operator_dto import LoginResponseDto, LoginDto, RefreshTokenDto, LoginTokenDto
from pf_auth.service.operator_service import OperatorService
from pfms.swagger.pfms_swagger_decorator import simple_get, pfms_post_request

operator_controller = Blueprint("operator_controller", __name__, url_prefix="/api/v1/operator")
operator_service = OperatorService()


@operator_controller.route("/init", methods=['GET'])
@simple_get(only_message=True)
def initialize():
    is_created = operator_service.init_default_operator()
    if is_created:
        return operator_service.success("Successfully Initialized")
    return operator_service.error("Unable to Initialize")


@operator_controller.route("/login", methods=["POST"])
@pfms_post_request(request_body=LoginDto, response_obj=LoginResponseDto)
def login():
    return operator_service.login_operator()


@operator_controller.route("/renew-token", methods=["POST"])
@pfms_post_request(request_body=RefreshTokenDto, response_obj=LoginTokenDto)
def renew_token():
    return operator_service.renew_token()


@operator_controller.route("/test", methods=['GET'])
@simple_get(only_message=True)
def test():
    return operator_service.error("Test Actions")
