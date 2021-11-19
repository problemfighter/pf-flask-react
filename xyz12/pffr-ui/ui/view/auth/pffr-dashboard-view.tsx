import React from 'react';
import {PFProps} from "@pfo/pf-react/src/artifacts/interface/pf-mixed-interface";
import PFComponentState from "@pfo/pf-react/src/artifacts/component/pf-component-state";
import PFComponent from "@pfo/pf-react/src/artifacts/component/pf-component";


interface Props extends PFProps {
}

class State extends PFComponentState {

}

export default class PFFRDashboardView extends PFComponent<Props, State> {

    state: State = new State();

    static defaultProps = {}

    constructor(props: Props) {
        super(props);
    }

    componentDidMount() {
    }

    componentDidUpdate(prevProps: Props) {
    }

    renderUI() {
        return (
            <React.Fragment>
                <h1>Dashboard</h1>
            </React.Fragment>
        )
    }

}