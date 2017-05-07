import React from 'react'

import { title } from '../../util.js';
import { strings } from '../../strings.js';

import Box from '../base/Box.jsx';
import InputText from '../base/InputNumber.jsx';
import InputSelect from '../base/InputSelect.jsx';
import InputCheck from '../base/InputCheck.jsx';
import InputWrapper from '../base/InputWrapper.jsx'
import Closable from '../base/Closable.jsx'


export default class TechnologieBox extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
        }
    }

    render() {
        var lang = this.props.lang;
        return (
            <Box style={this.props.style} startOpened={true} title={strings[lang]['charityBoxTitle']} color="#115e67">
                    <InputText
                        label={strings[lang]['lblCharity']}
                        tooltip={strings[lang]['ttCharity']}
                        placeholder={strings[lang]['plhInEuro']}
                        value={this.props.data['charity']}
                        onChange={this.props.uFuncs['charity']}
                        max="100"
                    />
            </Box>
        )
    }
    toggleInsurancePartner() {
        this.props.uFuncs['insurancePartner'](!this.props.data['insurancePartner'])
    }
    toggleInsuranceChild() {
        this.props.uFuncs['insuranceChild'](!this.props.data['insuranceChild'])
    }
    toggleBenefitsChild() {
        this.props.uFuncs['childBenefits'](!this.props.data['childBenefits'])
    }
}
