import React from 'react';
import { title, log } from '../../util.js'

import InputWrapper from './InputWrapper.jsx'


export default class InputText extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        var stText = Object.assign({}, {
            width: '100%',
            display: 'block',
            boxShadow: '0px 1px 3px rgba(0, 0, 0, 0.1) inset',
            backgroundImage: 'url(' + this.props.icon + ')',
            backgroundSize: '26px 26px',
            backgroundRepeat: 'no-repeat',
            backgroundPosition: '4px 4px',
            border: '1px solid #AAA',
            color: '#555',
            fontSize: 'inherit',
            overflow: 'hidden',
            padding: '8px',
            paddingLeft: this.props.icon != '' ? '32px' : '8px',
            textOverflow: 'ellipsis',
            whiteSpace: 'nowrap',
            backgroundColor: '#ffffff',
            borderRadius: '4px',
        }, this.props.style);

        return (
            <InputWrapper label={this.props.label} tooltip={this.props.tooltip} style={this.props.wrapperStyle}>
                <input style={stText} value={this.props.value} onChange={this.props.onChange} type="text" placeholder={title(this.props.placeholder)} />
            </InputWrapper>
        );
    }
}