import React from 'react'

import { title } from '../../util.js';
import { strings } from '../../strings.js';

import Box from '../base/Box.jsx';
import InputNumber from '../base/InputNumber.jsx';
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
            <Box style={this.props.style} startOpened={true} title={strings[lang]['socialBoxTitle']} color="#115e67">
                <div>
                    <InputWrapper label={strings[lang]['lblInsurance']}>
                            <div style={{ display: 'flex' }}>
                                {this.props.data.maritalStatus == 'couple' || this.props.data.maritalStatus == 'married' ?
                                    <InputCheck
                                        label={strings[lang]['lblInsurancePartner']}
                                        tooltip={strings[lang]['ttInscurancePartner']}
                                        checked={this.props.data['insurancePartner']}
                                        onChange={this.toggleInsurancePartner.bind(this)}
                                    /> : ""
                                }
                                    <InputNumber
                                        label={strings[lang]['lblInsuranceChild']}
                                        tooltip={strings[lang]['ttInsuranceChild']}
                                        onChange={this.props.uFuncs['insuranceChild']}
                                        value={this.props.data['insuranceChild']}
                                        placeholder={strings[lang]['plhPeopleAmount']}
                                        max="100"
                                    />
                            </div>
                        </InputWrapper>
                    <InputCheck
                        label={strings[lang]['lblRetirement']}
                        tooltip={strings[lang]['ttRetirement']}
                        checked={this.props.data['retirement']}
                        onChange={this.toggleRetirementChild.bind(this)}
                    />
                    <Closable opened={Number(this.props.data['children']) > 0 || Number(this.props.data['childrenHandicapped']) > 0}>
                        <InputCheck
                            label={strings[lang]['lblChildBenefits']}
                            tooltip={strings[lang]['ttChildBenefits']}
                            checked={this.props.data['childBenefits']}
                            onChange={this.toggleBenefitsChild.bind(this)}
                        />
                    </Closable>
                </div>
            </Box>
        )
    }
    toggleInsurancePartner() {
        this.props.uFuncs['insurancePartner'](!this.props.data['insurancePartner'])
    }
    toggleBenefitsChild() {
        this.props.uFuncs['childBenefits'](!this.props.data['childBenefits'])
    }
    toggleRetirementChild() {
        this.props.uFuncs['retirement'](!this.props.data['retirement'])
    }
}
