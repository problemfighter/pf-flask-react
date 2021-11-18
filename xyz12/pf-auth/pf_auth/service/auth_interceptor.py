from fpf_common.common.pff_request_header_helper import pff_request_header_helper
from pf_auth.common.jwt_helper import JWTHelper
from pf_flask.global_registry import get_global_app_config
from pfms.pfapi.rr.pfms_request_respons import PfRequestResponse

SYSTEM_DEFAULT_SKIP_URL = [
    "/pf-swagger-ui",
    "/api/v1/operator/login",
    "/api/v1/operator/init",
    "/pf-swagger-json"
]

SYSTEM_DEFAULT_SKIP_START_WITH_URL = [
    "/pf-marshmallow-swagger/",
]


class AuthInterceptor(PfRequestResponse):

    jwt_helper = JWTHelper()

    def intercept(self):
        url_info = pff_request_header_helper.get_url_info()
        relative_url = url_info['relative_url']
        skip_urls = SYSTEM_DEFAULT_SKIP_URL
        if get_global_app_config() and get_global_app_config().SKIP_URL_ON_AUTH:
            skip_urls += get_global_app_config().SKIP_URL_ON_AUTH
        if relative_url not in skip_urls and not self.check_url_start_with(relative_url):
            return self.check_auth()

    def check_url_start_with(self, request_url):
        for url in SYSTEM_DEFAULT_SKIP_START_WITH_URL:
            if request_url.startswith(url):
                return True
        return False

    def check_auth(self):
        bearer_token = pff_request_header_helper.get_bearer_token()
        if not bearer_token:
            return self.get_error_response()
        if not self.jwt_helper.validate_token(bearer_token):
            return self.get_error_response()

    def get_error_response(self, message="You are not Authorize for Access."):
        return self.error(message, code=4100, http_code=401)


auth_interceptor = AuthInterceptor()
