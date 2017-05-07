import React from 'react';
import {title} from '../../util.js'

import InputNumber from './InputNumber.jsx';
import InputWrapper from './InputWrapper.jsx';


export default class InputRange extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div style={this.props.style}>
                <InputWrapper label={this.props.label} tooltip={this.props.tooltip}>
                    <div style={{ display: 'flex', alignContent: 'center'}}>
                        <input
                            value={this.props.value}
                            onChange={this.props.onChange}
                            style={{ flexGrow: '1', height: '36px', margin: '0px', marginRight: '12px' }}
                            type="range"
                            min={this.props.min}
                            max={this.props.max}
                            step={this.props.step}
                        />
                        <div style={{width: '88px'}}>
                            <InputNumber
                                wrapperStyle={{padding: '0px'}}
                                onChange={this.props.onChange}
                                placeholder={title(this.props.placeholder)}
                                value={this.props.value}
                                min={this.props.min}
                                max={this.props.max}
                            />
                        </div>
                    </div>
                </InputWrapper>
            </div>
        );
    }
}


InputRange.propTypes = {
    value: React.PropTypes.string,
    min: React.PropTypes.string,
    max: React.PropTypes.string,
    step: React.PropTypes.string,
    onChange: React.PropTypes.func,
    label: React.PropTypes.any,
    placeholder: React.PropTypes.string,
}

InputRange.defaultProps = {
    value: '',
    min: '0',
    max: '12',
    step: '1',
    onChange: null,
    label: '',
    placeholder: '',
}