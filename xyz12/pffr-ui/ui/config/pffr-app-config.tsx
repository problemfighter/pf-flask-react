import React from 'react';
import PFAppConfig from "@pfo/pf-react/src/artifacts/config/pf-app-config";
import PFComponentState from "@pfo/pf-react/src/artifacts/component/pf-component-state";
import AppBeforeRenderView from "@pfo/base-app/src/view/system/app-before-render-view";
import PFHTTResponse from "@pfo/pf-react/src/artifacts/processor/http/pf-http-response";
import PFHTTAuthCallback from "@pfo/pf-react/src/artifacts/processor/http/pf-http-auth-callback";
import PFHTTRequest from "@pfo/pf-react/src/artifacts/processor/http/pf-http-request";
import AuthenticationService from "../service/authentication-service";
import {PFHTTPCall} from "@pfo/pf-react/src/artifacts/interface/pf-mixed-interface";


export default class PFFRAppConfig extends PFAppConfig {

    public getBeforeRenderUIView(componentState: PFComponentState, component: any) {
        return (<AppBeforeRenderView componentState={componentState} component={component}/>)
    }

    public getBaseURL(): string {
        return "http://127.0.0.1:1201/";
    }


    public getStaticBaseURL(): string {
        return "static/";
    }

    public isAuthorized(response?: PFHTTResponse): boolean {
        if (response && response.httpCode === 401) {
            return false
        }
        return true;
    }

    public authCallback(): PFHTTAuthCallback | undefined {
        let authCallback: PFHTTAuthCallback = {
            process(request: PFHTTRequest): PFHTTRequest {
                return AuthenticationService.instance().processAuth(request);
            }
        };
        return authCallback;
    }

    public renewAuthorization(trHttpCall: PFHTTPCall): void {
        let authService = new AuthenticationService();
        authService.renewAuthorization(trHttpCall);
    }

}