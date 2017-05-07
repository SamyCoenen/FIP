import React from 'react'

import { title } from '../../util.js'
import { strings } from '../../strings.js'

import AllowanceForm from './allowance/AllowanceForm.jsx'
import BikeForm from './bike/BikeForm.jsx'
import Box from '../base/Box.jsx'
import CarForm from './car/CarForm.jsx'
import DivWithTabs from '../base/DivWithTabs.jsx'


export default class MobilityBox extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            tabIndex: 0,
        }
        this.updateTabIndex = this.updateTabIndex.bind(this);
    }

    render() {
        var lang = this.props.lang;
        var tabs = [
            {title:title(strings[lang]['lblTabNothing']),tooltip:title(strings[lang]['ttTabNothing'])},
            {title:title(strings[lang]['lblTabCar']),tooltip:title(strings[lang]['ttTabCar'])},
            {title:title(strings[lang]['lblTabBicycle']),tooltip:title(strings[lang]['ttTabBicycle'])},
            {title:title(strings[lang]['lblTabAllowance']),tooltip:title(strings[lang]['ttTabAllowance'])},
        ]

        return (
            <Box style={this.props.style} startOpened={true} title={strings[lang]['mobilityBoxTitle']} color="#115e67">
                <DivWithTabs tabs={tabs} color="#115e67" index={this.state.tabIndex} uIndex={this.updateTabIndex}>
                    <div></div>
                    <CarForm
                        lang={this.props.lang}
                        data={this.props.data}
                        uFuncs={this.props.uFuncs}
                    />
                    <BikeForm
                        lang={this.props.lang}
                        data={this.props.data}
                        uFuncs={this.props.uFuncs}
                    />
                    <AllowanceForm
                        lang={this.props.lang}
                        data={this.props.data}
                        uFuncs={this.props.uFuncs}
                    />
                </DivWithTabs>
            </Box>
        );
    }

    updateTabIndex(index) {
        this.setState({ tabIndex: index });
        var indexMap = ['', 'car', 'bicycle', 'allowance'];
        this.props.uFuncs['mobilityOption'](indexMap[index]);
    }
}