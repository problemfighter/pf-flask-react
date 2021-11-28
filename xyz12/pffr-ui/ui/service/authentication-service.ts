import PFHTTRequest from "@pfo/pf-react/src/artifacts/processor/http/pf-http-request";
import PFBrowserStorageManager from "@pfo/pf-react/src/artifacts/manager/pf-browser-storage-manager";
import {PFUtil} from "@pfo/pf-react/src/artifacts/utils/pf-util";
import {PFHTTPCall} from "@pfo/pf-react/src/artifacts/interface/pf-mixed-interface";
import PFHTTCallback from "@pfo/pf-react/src/artifacts/processor/http/pf-http-callback";
import PFHTTResponse from "@pfo/pf-react/src/artifacts/processor/http/pf-http-response";
import {ApiUtil} from "@pfo/base-app/src/system/api-util";
import {PFFRDefaultUrl} from "../config/pffr-default-url";

export default class AuthenticationService {


    public processAuth(request: PFHTTRequest): PFHTTRequest {
        let accessToken = PFBrowserStorageManager.getByKey("accessToken");
        if (accessToken) {
            request.headers = PFUtil.addDataToObject(request.headers, "Authorization", "Bearer " + accessToken);
        }
        return request;
    }


    public addAuthorizationMetaData(data: any): boolean {
        let responseData = data.loginToken;
        let accessToken = responseData.accessToken;
        let refreshToken = responseData.refreshToken;

        let access = data.access;
        let navList = data.navList;
        if (access) {
            PFBrowserStorageManager.addAsJSONString("access", access);
        }

        if (navList) {
            PFBrowserStorageManager.addAsJSONString("navList", navList);
        }

        if (accessToken && refreshToken) {
            PFBrowserStorageManager.add("accessToken", accessToken);
            PFBrowserStorageManager.add("refreshToken", refreshToken);
            return true;
        }
        return false;
    }

    public logout() {
        PFBrowserStorageManager.remove("isAuthorized")
        PFBrowserStorageManager.remove("accessToken")
        PFBrowserStorageManager.remove("refreshToken")
        PFBrowserStorageManager.remove("navData")
    }

    public setNavigationData(data: any) {
        PFBrowserStorageManager.addAsJSONString("navData", data);
    }

    public getNavigationData() {
        PFBrowserStorageManager.getAsJSON("navData");
    }

    public processLoginToken(responseData: any): boolean {
        if (this.addAuthorizationMetaData(responseData)) {
            PFBrowserStorageManager.add("isAuthorized", true);
            let user = responseData.operator;
            let name = "Anonymous";
            if (user.firstName) {
                name = user.firstName
            }
            if (user.lastName) {
                name += " " + user.lastName
            }
            PFBrowserStorageManager.add("operatorName", name);
            PFBrowserStorageManager.add("operatorId", user.id);
            PFBrowserStorageManager.addAsJSONString("apiData", responseData);
            return true;
        }
        return false;
    }

    public renewAuthorization(trHttpCall: PFHTTPCall): void {
        const _this = this
        const httpRequestHelper = trHttpCall.getHttpRequestHelper();
        const parentComponent = trHttpCall.getComponent();
        let request: PFHTTRequest = httpRequestHelper.httpRequestObject(PFFRDefaultUrl.RENEW_TOKEN_URL);
        request.requestData = {
            data: {
                refreshToken: PFBrowserStorageManager.getByKey("refreshToken")
            }
        };
        let callback: PFHTTCallback = {
            before: (response: PFHTTResponse) => {
                httpRequestHelper.showLoader();
            },
            success: (response: PFHTTResponse) => {
                const responseData = ApiUtil.getValidResponseOrNone(response, parentComponent);
                if (responseData && responseData.status !== "error" && this.addAuthorizationMetaData(responseData.data)) {
                    trHttpCall.resume();
                } else {
                    _this.logout();
                    parentComponent.failedRedirect("/", "Session has been expired.");
                }
            },
            failed: (response: PFHTTResponse) => {
                let message = "Unable to process request when trying to renew session";
                if (response.message) {
                    message = response.message
                }
                parentComponent.showErrorFlash(message);
            },
            finally: () => {
                httpRequestHelper.hideLoader();
            }
        };
        httpRequestHelper.httpManager().postJSON(request, callback);
    }


    public static instance() {
        return new AuthenticationService();
    }
}