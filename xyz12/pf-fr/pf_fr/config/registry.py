from pf_flask.global_registry import global_app_config
from pf_flask.pff_interfaces import PFFRegisterModule


class Register(PFFRegisterModule):

    def register_model_controller(self, flask_app):
        if global_app_config and global_app_config.ENABLE_AUTH_MODULE:
            print("Register Auth")
        print("PF FR Register Model Controller")

    def run_on_start(self, flask_app):
        print("PF FR Run On Start")
