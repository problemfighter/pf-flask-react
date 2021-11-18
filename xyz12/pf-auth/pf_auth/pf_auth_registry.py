from pf_auth.controller.operator_controller import operator_controller
from pf_flask.pff_interfaces import PFFAppRegistry
from pf_auth.model.operator import database as operator_model
from pf_auth.model.operator_token import database as operator_token_model


class PFAuthRegistry(PFFAppRegistry):

    def run_on_start(self, flask_app):
        pass

    def register_model(self):
        operator_model.create_all()
        operator_token_model.create_all()

    def register_controller(self, flask_app):
        flask_app.register_blueprint(operator_controller)


pf_auth_registry = PFAuthRegistry()
