import ReactDOM from 'react-dom';
import React from 'react';
import PFPageManager from "@pfo/pf-react/src/artifacts/manager/pf-page-manager";
import PFFRAppConfig from "./config/pffr-app-config";
import PFFRURLMapping from "./config/pffr-url-mapping";


const appConfig = new PFFRAppConfig();
const urlMapping = new PFFRURLMapping();
ReactDOM.render(<PFPageManager appConfig={appConfig} urlMapping={urlMapping}/>, document.getElementById('root'));