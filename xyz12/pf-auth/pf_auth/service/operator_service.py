from pf_auth.dto.operator_dto import LoginDto, OperatorDto
from pf_auth.model.operator import Operator
from pf_flask.global_registry import global_app_config
from pf_sqlalchemy.crud.pfs_crud_service import PfsCrudService
from pfms.pfapi.rr.pfms_request_respons import PfRequestResponse


class OperatorService(PfRequestResponse):

    crud_service = PfsCrudService()

    def get_operator_by_email(self, email):
        return Operator.query.filter(Operator.email == email).first()

    def get_operator_by_username(self, username):
        return Operator.query.filter(Operator.username == username).first()

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
        return self.json_list_dic_data_response(response_map)

    def renew_token(self):
        pass
