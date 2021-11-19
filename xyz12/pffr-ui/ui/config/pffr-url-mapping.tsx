import React from 'react';
import PFURLMapping from "@pfo/pf-react/src/artifacts/config/pf-url-mapping";
import PFLayoutInfoData from "@pfo/pf-react/src/artifacts/data/pf-layout-info-data";
import PublicLayout from "@pfo/base-app/src/view/layouts/public-layout";
import PrivateLayout from "@pfo/base-app/src/view/layouts/private-layout";

const PFRFLoginView = React.lazy(() => import('./../view/auth/pffr-login-view'));
const PFFRDashboardView = React.lazy(() => import('./../view/auth/pffr-dashboard-view'));


export default class PFFRURLMapping extends PFURLMapping {

    public getLayoutsAndPages(): Array<PFLayoutInfoData> {
        let pageWithLayout: Array<PFLayoutInfoData> = [];

        let privateLayoutInfo: PFLayoutInfoData = new PFLayoutInfoData();
        privateLayoutInfo.layout = PrivateLayout

        privateLayoutInfo.addPageInstance("/dashboard", PFFRDashboardView);
        pageWithLayout.push(privateLayoutInfo);

        let publicLayoutInfo: PFLayoutInfoData = new PFLayoutInfoData();
        publicLayoutInfo.layout = PublicLayout

        publicLayoutInfo.addPageInstance("/", PFRFLoginView);
        pageWithLayout.push(publicLayoutInfo);

        return pageWithLayout
    }

}