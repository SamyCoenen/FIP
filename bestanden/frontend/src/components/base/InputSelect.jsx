import React from 'react';

import InputWrapper from './InputWrapper.jsx'
import {title} from '../../util.js'


export default class InputSelect extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        var stSelect = Object.assign({}, {
            width: '100%',
            display: 'block',
            boxShadow: '0px 1px 3px rgba(0, 0, 0, 0.1) inset',
            backgroundImage: 'url(/assets/images/15xvbd5.png)',
            backgroundPosition: 'calc(100% - 10px) center',
            backgroundRepeat: 'no-repeat',
            border: '1px solid #AAA',
            color: '#555',
            fontSize: 'inherit',
            overflow: 'hidden',
            padding: '8px',
            paddingRight: '32px',
            textOverflow: 'ellipsis',
            whiteSpace: 'nowrap',
            backgroundColor: '#ffffff',
            borderRadius: '4px',
            WebkitAppearance: 'none',
            MozAppearance: 'none',
        }, this.props.style);

        return (
            <InputWrapper label={this.props.label} style={this.props.style} tooltip={this.props.tooltip}>
                <select style={stSelect} value={this.props.value} onChange={this.props.onChange}>
                    {this.props.placeholder ?
                        <option style={{ color: 'gray' }} value="" hidden disabled>{title(this.props.placeholder)}</option>
                        : null}
                    {
                        this.props.options.map(function (option, index) {
                            if (typeof option === 'string') {
                                return (
                                    <option value={option} key={index}>{title(option)}</option>
                                );
                            } else {
                                return (
                                    <option value={option.val} key={index}>{title(option.desc)}</option>
                                );
                            }
                        })
                    }
                </select>
            </InputWrapper>
        );
    }
}

InputSelect.propTypes = {
    value: React.PropTypes.string,
    onChange: React.PropTypes.func,
    label: React.PropTypes.any,
    placeholder: React.PropTypes.string,
}

InputSelect.defaultProps = {
    value: '',
    onChange: null,
    label: '',
    placeholder: '',
}