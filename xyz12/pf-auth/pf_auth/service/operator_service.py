from fpf_common.util.common_util import get_uuid
from pf_auth.common.jwt_helper import JWTHelper
from pf_auth.dto.operator_dto import LoginDto, OperatorDto
from pf_auth.model.operator import Operator
from pf_auth.model.operator_token import OperatorToken
from pf_flask.global_registry import global_app_config
from pf_sqlalchemy.crud.pfs_crud_service import PfsCrudService
from pfms.pfapi.rr.pfms_request_respons import PfRequestResponse


class OperatorService(PfRequestResponse):
    crud_service = PfsCrudService()
    jwt_helper = JWTHelper()

    def get_operator_by_email(self, email):
        return Operator.query.filter(Operator.email == email).first()

    def get_operator_by_username(self, username):
        return Operator.query.filter(Operator.username == username).first()

    def get_operator_by_id(self, id):
        return Operator.query.filter(Operator.id == id).first()

    def init_default_operator(self):
        email = global_app_config.LOGIN_DEFAULT_EMAIL
        password = global_app_config.LOGIN_DEFAULT_PASSWORD
        operator = self.get_operator_by_email(email)
        if not operator:
            operator = Operator()
            operator.email = email
            operator.password = password
            self.crud_service.save(operator)
            if operator.id:
                return True
            return False

    def login_by(self, identifier, password):
        response: Operator
        if global_app_config.LOGIN_IDENTIFIER == "username":
            response = self.get_operator_by_username(identifier)
        else:
            response = self.get_operator_by_email(identifier)
        if response and response.verify_password(password):
            return response
        return None

    def login_operator(self):
        login_credential = self.json_request_process(LoginDto())
        response = self.login_by(login_credential['identifier'], login_credential['password'])
        if not response:
            return self.error("Invalid Credentials! Please enter valid Credential")
        if not response.isActive:
            return self.error("Sorry your account has been inactive.")
        if not response.isVerified:
            return self.error("Sorry your account has not been verified.")
        return self.process_login_response(response)

    def process_login_response(self, operator):
        operator_details = OperatorDto().dump(operator)
        response_map: dict = {
            "operator": operator_details
        }
        error_message = "Unable to process login request"
        access_token = self.get_access_token(operator.id)
        if not access_token:
            return self.error(error_message)
        response_map['accessToken'] = access_token
        refresh_token = self.get_refresh_token(operator.id)
        if not refresh_token:
            return self.error(error_message)
        response_map['refreshToken'] = refresh_token
        return self.json_list_dic_data_response(response_map)

    def get_access_token(self, operator_id):
        operator = self.get_operator_by_id(operator_id)
        if not operator:
            return None
        payload = {
            "operator": operator.id
        }
        return self.jwt_helper.get_access_token(payload, iss=operator.uuid)

    def get_refresh_token(self, operator_id):
        operator = self.get_operator_by_id(operator_id)
        if not operator:
            return None
        payload = {
            "operator": operator.id
        }
        db_token = self.create_or_update_db_refresh_token(operator_id)
        if not db_token:
            return None
        payload['token'] = db_token.token
        return self.jwt_helper.get_refresh_token(payload, iss=operator.uuid)

    def create_or_update_db_refresh_token(self, operator_id, uuid=None):
        existing_token: OperatorToken = self.get_operator_token_by_operator_id(operator_id)
        if uuid:
            if not existing_token or existing_token.token != uuid:
                return None
        else:
            if not existing_token:
                existing_token = OperatorToken(name="REFRESH_TOKEN", operatorId=operator_id)
        existing_token.token = get_uuid()
        self.crud_service.save(existing_token)
        return existing_token

    def get_operator_token_by_operator_id(self, operator_id):
        return OperatorToken.query.filter(OperatorToken.operatorId == operator_id).first()

    def renew_token(self):
        pass
