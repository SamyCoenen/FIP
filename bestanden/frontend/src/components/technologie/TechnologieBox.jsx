import React from 'react'

import Box from '../base/Box.jsx';
import Textbox from '../base/InputNumber.jsx';
import Combobox from '../base/InputSelect.jsx';
import { title } from '../../util.js';
import { strings } from '../../strings.js';


export default class TechnologieBox extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
        }
    }

    render() {
        var lang = this.props.lang;
        return (
            <Box onBlur={this.props.onBlur} style={this.props.style} startOpened={true} title={title(strings[lang]['technologieBoxTitle'])} color="#115e67">
                <Textbox label={title(strings[lang]['lblSmartphone'])} tooltip={strings[lang]['ttSmartphone']} placeholder={strings[lang]['plhInEuro']} value={this.props.data['smartphonePrice']} onChange={this.props.uFuncs['smartphonePrice']} />
                <Textbox label={title(strings[lang]['lblMultimedia'])} tooltip={strings[lang]['ttMultimedia']} placeholder={strings[lang]['plhInEuro']} value={this.props.data['multimediaPrice']} onChange={this.props.uFuncs['multimediaPrice']} />
                <Textbox label={title(strings[lang]['lblLaptop'])} tooltip={strings[lang]['ttLaptop']} placeholder={strings[lang]['plhInEuro']} value={this.props.data['laptopPrice']} onChange={this.props.uFuncs['laptopPrice']} />
                <Combobox label={title(strings[lang]['lblInternet'])} tooltip={strings[lang]['ttInternet']} value={this.props.data['internetPrice']} placeholder={strings[lang]['plhSelect']}
                    options={[{ val: '0', desc: strings[lang]['descNone'] }, { val: '25', desc: strings[lang]['descInternet25'] }, { val: '35', desc: strings[lang]['descInternet35'] }, { val: '45', desc: strings[lang]['descInternet45'] }]} onChange={this.props.uFuncs['internetPrice']} />
            </Box>
        )
    }
}
