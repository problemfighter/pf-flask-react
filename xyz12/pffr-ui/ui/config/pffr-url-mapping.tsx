import React from 'react';
import PFURLMapping from "@pfo/pf-react/src/artifacts/config/pf-url-mapping";
import PFLayoutInfoData from "@pfo/pf-react/src/artifacts/data/pf-layout-info-data";


export default class PFFRURLMapping extends PFURLMapping {

    public getLayoutsAndPages(): Array<PFLayoutInfoData> {
        let pageWithLayout: Array<PFLayoutInfoData> = [];

        let privateLayoutInfo: PFLayoutInfoData = new PFLayoutInfoData();

        return pageWithLayout
    }

}