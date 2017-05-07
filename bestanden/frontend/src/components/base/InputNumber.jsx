import React from 'react';
import { title, log } from '../../util.js'

import InputText from './InputText.jsx'


export default class InputNumber extends React.Component {

    constructor(props) {
        super(props);
        this.validateInput = this.validateInput.bind(this);
    }

    render() {
        return (
            <InputText
                style={this.props.style}
                wrapperStyle={this.props.wrapperStyle}
                icon={this.props.icon}
                label={this.props.label}
                tooltip={this.props.tooltip}
                onChange={this.validateInput}
                placeholder={title(this.props.placeholder)}
                value={this.props.value}
            />
        );
    }

    validateInput(e) {
        var value = e.target.value.replace(',', '.');
        if (!isNaN(value)) {
            if(this.props.max == '' || Number(value) <= Number(this.props.max)) {
                this.props.onChange(value);
            } // css transition red
        }
    }
}

InputNumber.propTypes = {
    style: React.PropTypes.object,
    wrapperStyle: React.PropTypes.object,
    value: React.PropTypes.string,
    min: React.PropTypes.string,
    max: React.PropTypes.string,
    onChange: React.PropTypes.func,
    label: React.PropTypes.any,
    placeholder: React.PropTypes.string,
    icon: React.PropTypes.string,
}

InputNumber.defaultProps = {
    style: null,
    wrapperStyle: null,
    value: '',
    min: '0',
    max: '',
    onChange: null,
    label: '',
    placeholder: '',
    icon: '',
}