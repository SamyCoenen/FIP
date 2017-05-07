import React from 'react'
import { title } from '../../util.js'

import Clickable from './Clickable.jsx'
import NoSelect from './NoSelect.jsx'


export default class LanguagePicker extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        var stCont = {
            position: 'absolute',
            right: '0',
            padding: '4px',
            paddingRight: '0px',
            backgroundColor: '#fff',
            borderRadius: '8px 0px 0px 8px',
        };
        var stBtn = {
            padding: '2px',
            fontWeight: 'bold',
            color: '#999',
        };
        var stBtnHover = {
            color: '#666',
        };

        return (
            <div style={{position: 'relative'}}>
                <div style={stCont}>
                    <Clickable onClick={this.updateLanguage.bind(this, 'nl')} style={stBtn} hoverStyle={stBtnHover}><NoSelect>NL</NoSelect></Clickable>
                    <Clickable onClick={this.updateLanguage.bind(this, 'en')} style={stBtn} hoverStyle={stBtnHover}><NoSelect>EN</NoSelect></Clickable>
                </div>
            </div>
        )
    }

    updateLanguage(language) {
        this.props.onPick(language)
    }
}

LanguagePicker.propTypes = {
    lang: React.PropTypes.string,
    onPick: React.PropTypes.func,
};

LanguagePicker.defaultProps = {
    lang: '',
    onPick: null,
};