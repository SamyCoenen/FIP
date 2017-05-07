import React from 'react';

import InputWrapper from './InputWrapper.jsx'
import NoSelect from './NoSelect.jsx'
import Tooltip from 'react-tooltip-component'

export default class InputCheck extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        var stCheck = Object.assign({}, {
            width: '34px',
            height: '34px',
            boxShadow: '0px 1px 3px rgba(0, 0, 0, 0.1) inset',
            border: '1px solid #AAA',
            borderRadius: '4px',
            WebkitAppearance: 'none',
            MozAppearance: 'none',
        }, this.props.style);

        var stImg = {
            width: '36px',
            height: '36px',
        }

        return (
            <InputWrapper icon={this.props.icon} label={this.props.label}>
                <Tooltip title={this.props.tooltip} position='bottom' space='-6'>
                    <div
                        style={stCheck}
                        ref="complete"
                        onClick={this.props.onChange}
                    >
                        <NoSelect>{this.props.checked ? <img style={stImg} src="assets/images/vink.png" /> : null}</NoSelect>
                    </div>
                </Tooltip>
            </InputWrapper>
        );
    }

}

InputCheck.propTypes = {
    checked: React.PropTypes.bool,
    onChange: React.PropTypes.func,
    label: React.PropTypes.string,
}

InputCheck.defaultProps = {
    checked: '',
    onChange: null,
    label: '',
}