from pf_flask.pff_app_config import PFFAppConfig


class PFRAppConfig(PFFAppConfig):
    LOGIN_IDENTIFIER: str = "email"
    ENABLE_AUTH_MODULE: bool = True
    MODULE_REGISTRY_PACKAGE: list = [
        "application.config.registry.Register",
        "pf_fr.config.registry.Register",
    ]
    APPLICATION_CONFIGURATION = "application.config.app_config.Config"
    AUTH_MIDDLEWARE = "application.config.middleware.AuthMiddleware"
    AUTH_PROCESSOR = "application.config.processor.AuthProcessor"


