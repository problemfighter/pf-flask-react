from flask import Blueprint
from pf_auth.service.operator_service import OperatorService
from pfms.swagger.pfms_swagger_decorator import simple_get


operator_controller = Blueprint("operator_controller", __name__, url_prefix="/api/v1/operator")
operator_service = OperatorService()


@operator_controller.route("/init", methods=['GET'])
@simple_get(only_message=True)
def initialize():
    is_created = operator_service.init_default_operator()
    if is_created:
        return operator_service.success("Successfully Initialized")
    return operator_service.error("Unable to Initialize")
