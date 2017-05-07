import React from 'react'
import { title } from '../../util.js'
import Tooltip from 'react-tooltip-component'

import NoSelect from './NoSelect.jsx'


export default class InputWrapper extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        var stCont = Object.assign({}, {
            padding: '12px',
        }, this.props.style);
        var stLabel = {
            display: 'inline-block',
            marginBottom: '4px',
            fontWeight: 'bold',
            marginLeft: '4px',
        };
        var stIcon = {
            height: '100%',
            marginRight: '2px',
        };
        if (this.props.tooltip != '') {
            return (
                <div style={stCont}>
                    <Tooltip title={this.props.tooltip} position='bottom' space='-6'>
                        <div>
                            <div style={stLabel}><NoSelect>{this.props.label==''?'‌‌ ':title(this.props.label)}</NoSelect></div> {/* don't delete space this is a hidden character*/}
                            {this.props.children}
                        </div>
                    </Tooltip>
                </div>
            );
        } else {
            return (
                <div style={stCont}>
                    <div style={stLabel}>{title(this.props.label)}</div>
                    {this.props.children}
                </div>
            );
        }
    }
}

InputWrapper.propTypes = {
    tooltip: React.PropTypes.string,
    label: React.PropTypes.string,
    icon: React.PropTypes.string,
};

InputWrapper.defaultProps = {
    tooltip: '',
    label: '',
    icon: '',
};