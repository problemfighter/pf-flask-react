from pf_auth.service.auth_interceptor import auth_interceptor
from pf_flask.bismillah import Bismillah
from pf_fr.processor.config_processor import config_processor


def init_authentication_checker():
    return auth_interceptor.intercept()


class PFRFSystem:
    name = None
    base_path = None
    application = None

    def __init__(self, name: str, base_path: str):
        self.base_path = base_path
        self.name = name

    def initialize(self):
        config = config_processor.get_config(self.base_path)
        self.application = Bismillah(self.name, config)
        self.init_auth_checker()
        return self.application

    def init_auth_checker(self):
        self.application.add_before_request_fun(init_authentication_checker)
