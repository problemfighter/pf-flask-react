import React from 'react';
import {PFProps} from "@pfo/pf-react/src/artifacts/interface/pf-mixed-interface";
import PFComponentState from "@pfo/pf-react/src/artifacts/component/pf-component-state";
import PFComponent from "@pfo/pf-react/src/artifacts/component/pf-component";
import LoginView from "@pfo/base-app/src/view/auth/login-view";
import loginLogo from './../../assets/img/logo/logo-login.png'
import PFHTTResponse from "@pfo/pf-react/src/artifacts/processor/http/pf-http-response";
import {ApiUtil} from "@pfo/base-app/src/system/api-util";
import {AppConstant} from "@pfo/base-app/src/system/app-constant";
import AuthenticationService from "../../service/authentication-service";
import {PFFRDefaultUrl} from "../../config/pffr-default-url";
import PFBrowserStorageManager from "@pfo/pf-react/src/artifacts/manager/pf-browser-storage-manager";
import {PFUtil} from "@pfo/pf-react/src/artifacts/utils/pf-util";


interface Props extends PFProps {
    logo?: any
    title?: String
    loginURL?: String
    successRedirect?: String
}

class State extends PFComponentState {

}


export default class PFRFLoginView extends PFComponent<Props, State> {

    state: State = new State();

    static defaultProps = {
        logo: loginLogo,
        title: "PFRF System",
    }

    constructor(props: Props) {
        super(props);
    }

    componentDidMount() {
        const _this = this;
        let successRedirect: any = PFFRDefaultUrl.UI_DEFAULT_LOGIN_SUCCESS
        if (_this.props.successRedirect) {
            successRedirect = _this.props.successRedirect
        }
        if (Boolean(PFBrowserStorageManager.getByKey("isAuthorized"))) {
            PFUtil.gotoUrl(this, successRedirect);
        }
    }

    componentDidUpdate(prevProps: Props) {
    }

    submitFormData(event: any, data: any, parentComponent: any) {
        event.preventDefault();
        const _this = this;
        let url: any = PFFRDefaultUrl.LOGIN_URL
        let successRedirect: any = PFFRDefaultUrl.UI_DEFAULT_LOGIN_SUCCESS
        if (_this.props.loginURL) {
            url = _this.props.loginURL
        }
        if (_this.props.successRedirect) {
            successRedirect = _this.props.successRedirect
        }
        try {
            _this.httpRequest.postJson(url, data,
                {
                    callback(response: PFHTTResponse): void {
                        let apiResponse = ApiUtil.getFormRequestValidResponseOrNone(response, parentComponent);
                        if (apiResponse && apiResponse.status === AppConstant.STATUS_SUCCESS) {
                            AuthenticationService.instance().processLoginToken(apiResponse.data);
                            _this.successRedirect(successRedirect, apiResponse.message);
                        }
                    }
                },
                {
                    callback(response: PFHTTResponse): void {
                        ApiUtil.inspectResponseAndShowValidationError(response, parentComponent);
                    }
                }
            );
        } catch (e: any) {
            _this.showErrorFlash(e.message)
        }
    }

    renderUI() {
        const {logo, title} = this.props
        const _this = this;
        return (
            <React.Fragment>
                <LoginView
                    route={this.props.route}
                    title={title}
                    logo={logo}
                    formSubmit={(event: any, data: any, parentComponent: any) =>{_this.submitFormData(event, data, parentComponent)}}
                />
            </React.Fragment>
        )
    }

}