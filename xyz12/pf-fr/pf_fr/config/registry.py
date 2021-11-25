from pf_auth.pf_auth_registry import pf_auth_registry
from pf_flask.global_registry import get_global_app_config
from pf_flask.pff_interfaces import PFFRegisterModule


class Register(PFFRegisterModule):

    def register_model_controller(self, flask_app):
        if get_global_app_config() and get_global_app_config().ENABLE_AUTH_MODULE:
            pf_auth_registry.register_model()
            pf_auth_registry.register_controller(flask_app)

    def run_on_start(self, flask_app):
        if get_global_app_config() and get_global_app_config().ENABLE_AUTH_MODULE:
            pf_auth_registry.run_on_start(flask_app)
