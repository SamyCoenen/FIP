import React from 'react'

import { title } from '../../util.js'
import { strings } from '../../strings.js';

import Box from '../base/Box.jsx'
import InputNumber from '../base/InputNumber.jsx'
import Checkbox from '../base/InputCheck.jsx'
import InputSelect from '../base/InputSelect.jsx'
import Closable from '../base/Closable.jsx'


export default class IncomeBox extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        var lang = this.props.lang;
        return (
            <Box onBlur={this.props.onBlur} style={this.props.style} title={strings[lang]['incomeBoxTitle']} color="#115e67" startOpened={true}>
                <InputNumber
                    value={this.props.data.wageBT}
                    onChange={this.props.uFuncs['wageBT']}
                    label={strings[lang]['lblWageBT']}
                    tooltip={strings[lang]['ttWageBT']}
                    placeholder={strings[lang]['plhInEuro']}
                />
                <InputSelect
                    value={this.props.data.workStatus}
                    options={[
                        { val: 'arbeider', desc: strings[lang]['descWorker'] },
                        { val: 'bediende', desc: strings[lang]['descClerk'] },
                    ]}
                    onChange={this.props.uFuncs['workStatus']}
                    label={strings[lang]['lblWorkStatus']}
                    tooltip={strings[lang]['ttWorkStatus']}
                    placeholder={strings[lang]['plhSelect']}
                />
                <InputSelect
                    value={this.props.data.maritalStatus}
                    options={[
                        { val: 'single', desc: strings[lang]['descSingle'] },
                        { val: 'couple', desc: strings[lang]['descCouple'] },
                        { val: 'married', desc: strings[lang]['descMarried'] },
                    ]}
                    onChange={this.props.uFuncs['maritalStatus']}
                    label={strings[lang]['lblMaritalStatus']}
                    tooltip={strings[lang]['ttMaritalStatus']}
                    placeholder={strings[lang]['plhSelect']}
                />
                <Closable opened={this.props.data.maritalStatus == 'couple' || this.props.data.maritalStatus == 'married'}>
                    <InputNumber
                        value={this.props.data.partnerWage}
                        onChange={this.props.uFuncs['partnerWage']}
                        label={strings[lang]['lblPartnerWage']}
                        tooltip={strings[lang]['ttPartnerWage']}
                        placeholder={strings[lang]['plhInEuro']}
                    />
                    <div style={{ display: 'flex' }}>
                        <Checkbox label={strings[lang]['lblPartnerRetirement']} tooltip={strings[lang]['ttPartnerRetirement']} checked={this.props.data['partnerRetirement']} onChange={this.toggleRetirementPartner.bind(this)} />
                        <Checkbox label={strings[lang]['lblPartnerHandicapped']} tooltip={strings[lang]['ttPartnerHandicapped']} checked={this.props.data['partnerHandicapped']} onChange={this.toggleHandicappedPartner.bind(this)} />
                    </div>
                </Closable>
                <div style={{ display: 'flex' }}>
                    <InputNumber
                        value={this.props.data.children}
                        onChange={this.props.uFuncs['children']}
                        label={strings[lang]['lblChildren']}
                        tooltip={strings[lang]['ttChildren']}
                        placeholder={strings[lang]['plhPeopleAmount']}
                        max="100"
                    />
                    <InputNumber
                        value={this.props.data.childrenHandicapped}
                        onChange={this.props.uFuncs['childrenHandicapped']}
                        label={strings[lang]['lblChildrenHandicapped']}
                        tooltip={strings[lang]['ttChildrenHandicapped']}
                        icon="/assets/images/disabled-viking.png"
                        placeholder={strings[lang]['plhPeopleAmount']}
                        max="100"
                    />
                </div>
                <div style={{ display: 'flex' }}>
                    <InputNumber
                        value={this.props.data.adults}
                        onChange={this.props.uFuncs['adults']}
                        label={strings[lang]['lblAdults']}
                        tooltip={strings[lang]['ttAdults']}
                        placeholder={strings[lang]['plhPeopleAmount']}
                        max="100"
                    />
                    <InputNumber
                        value={this.props.data.adultsHandicapped}
                        onChange={this.props.uFuncs['adultsHandicapped']}
                        label={strings[lang]['lblAdultsHandicapped']}
                        tooltip={strings[lang]['ttAdultsHandicapped']}
                        icon="/assets/images/disabled-viking.png"
                        placeholder={strings[lang]['plhPeopleAmount']}
                        max="100"
                    />
                </div>
                <div style={{ display: 'flex' }}>
                    <InputNumber
                        value={this.props.data.old}
                        onChange={this.props.uFuncs['old']}
                        label={strings[lang]['lblOld']}
                        tooltip={strings[lang]['ttOld']}
                        placeholder={strings[lang]['plhPeopleAmount']}
                        max="100"
                    />
                    <InputNumber
                        value={this.props.data.oldHandicapped}
                        onChange={this.props.uFuncs['oldHandicapped']}
                        label={strings[lang]['lblOldHandicapped']}
                        tooltip={strings[lang]['ttOldHanicapped']}
                        icon="/assets/images/disabled-viking.png"
                        placeholder={strings[lang]['plhPeopleAmount']}
                        max="100"
                    />
                </div>
            </Box>
        )
    }
    toggleRetirementPartner() {
        this.props.uFuncs['partnerRetirement'](!this.props.data['partnerRetirement'])
    }
    toggleHandicappedPartner() {
        this.props.uFuncs['partnerHandicapped'](!this.props.data['partnerHandicapped'])
    }
}
