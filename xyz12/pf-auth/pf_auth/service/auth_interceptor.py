from fpf_common.common.pff_request_header_helper import pff_request_header_helper
from pf_flask.global_registry import get_global_app_config
from pfms.pfapi.rr.pfms_request_respons import PfRequestResponse

SYSTEM_DEFAULT_SKIP_URL = [
    "/api/v1/operator/login",
    "/api/v1/operator/init"
]


class AuthInterceptor(PfRequestResponse):

    def intercept(self):
        url_info = pff_request_header_helper.get_url_info()
        relative_url = url_info['relative_url']
        skip_urls = SYSTEM_DEFAULT_SKIP_URL
        if get_global_app_config() and get_global_app_config().SKIP_URL_ON_AUTH:
            skip_urls += get_global_app_config().SKIP_URL_ON_AUTH
        if relative_url not in skip_urls:
            return self.check_auth()

    def check_auth(self):
        bearer_token = pff_request_header_helper.get_bearer_token()
        if not bearer_token:
            return self.error("You are not Authorize for Access.", http_code=401)


auth_interceptor = AuthInterceptor()
