import React from 'react';
import PFAppConfig from "@pfo/pf-react/src/artifacts/config/pf-app-config";
import PFComponentState from "@pfo/pf-react/src/artifacts/component/pf-component-state";
import AppBeforeRenderView from "@pfo/base-app/src/view/system/app-before-render-view";


export default class PFFRAppConfig extends PFAppConfig {

    public getBeforeRenderUIView(componentState: PFComponentState, component: any) {
        return (<AppBeforeRenderView componentState={componentState} component={component}/>)
    }

    public getBaseURL(): string {
        return "https://flask-hmtmcse.herokuapp.com/";
    }

}