from pf_flask.pff_app_config import PFFAppConfig


class PFRAppConfig(PFFAppConfig):
    LOGIN_IDENTIFIER: str = "email"
    ENABLE_AUTH_MODULE: bool = True
    MODULE_REGISTRY_PACKAGE: list = [
        "application.registry.Register",
        "pf_fr.config.registry.Register",
    ]
