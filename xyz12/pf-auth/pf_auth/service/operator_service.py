from pf_auth.model.operator import Operator
from pf_flask.global_registry import global_app_config
from pf_sqlalchemy.crud.pfs_crud_service import PfsCrudService
from pfms.pfapi.rr.pfms_request_respons import PfRequestResponse


class OperatorService(PfRequestResponse):

    crud_service = PfsCrudService()

    def get_operator_by_email(self, email):
        return Operator.query.filter(Operator.email == email).first()

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
