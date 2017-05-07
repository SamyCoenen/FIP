import React from 'react';

import { strings } from '../../../strings.js';
import { title } from '../../../util.js'

import InputRange from '../../base/InputRange.jsx';
import InputSelect from '../../base/InputSelect.jsx';


export default class AllowanceForm extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        var lang = this.props.lang;
        return (
            <div style={{ position: 'relative', overflow: 'hidden' }}>
                <InputSelect
                    label={title(strings[lang]['lblAllowanceDays'])}
                    tooltip={strings[lang]['ttAllowanceDays']}
                    value={this.props.data['allowanceDays']}
                    options={['1', '2', '3', '4', '5', '6', '7']}
                    onChange={this.props.uFuncs['allowanceDays']}
                    placeholder={strings[lang]['plhSelect']}
                />
                <InputRange
                    value={this.props.data.allowanceKms}
                    max="300"
                    step="5"
                    onChange={this.props.uFuncs['allowanceKms']}
                    label={strings[lang]['lblAllowanceDistance']}
                    tooltip={strings[lang]['ttAllowanceDistance']}
                    placeholder={strings[lang]['plhAllowanceDistance']}
                />
            </div>
        );
    }
}