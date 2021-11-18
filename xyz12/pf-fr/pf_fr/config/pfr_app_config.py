from pf_flask.pff_app_config import PFFAppConfig


class PFRAppConfig(PFFAppConfig):
    LOGIN_DEFAULT_EMAIL: str = "admin@pfr.loc"
    LOGIN_DEFAULT_PASSWORD: str = "admin"
    LOGIN_IDENTIFIER: str = "email"
    ENABLE_AUTH_MODULE: bool = True
    MODULE_REGISTRY_PACKAGE: list = [
        "application.config.registry.Register",
        "pf_fr.config.registry.Register",
    ]
    APPLICATION_CONFIGURATION: str = "application.config.app_config.Config"
    AUTH_MIDDLEWARE: str = "application.config.middleware.AuthMiddleware"
    AUTH_PROCESSOR: str = "application.config.processor.AuthProcessor"
    JWT_SECRET: str = "I_am-secret_key12#"
    JWT_ACCESS_TOKEN_VALIDITY_MIN: int = 30
    JWT_REFRESH_TOKEN_VALIDITY_MIN: int = 60
    SKIP_URL_ON_AUTH: list = []
