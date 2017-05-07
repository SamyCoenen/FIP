import React from 'react';

import Clickable from './Clickable.jsx';


export default class ProgressBar extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            value: 0,
        }
    }

    render() {

        var procent = Math.ceil((this.props.value / this.props.max) * 100);

        if (this.props.inverse) {
            procent = 100 - procent;
        }

        var stBackground = {
            width: '100%',
            height: this.props.height,
            backgroundColor: this.props.backgroundColor,
        };

        var stBar = {
            width: procent + '%',
            height: '100%',
            backgroundColor: this.props.color,
            WebkitBoxShadow: '0 2px 5px rgba(0, 0, 0, 0.25) inset',
            boxShadow: '0 2px 5px rgba(0, 0, 0, 0.25) inset',
            border: 'none',
        };

        return (
            <div style={stBackground}>
                <div style={stBar}>
                </div>
            </div>
        );
    }
}

ProgressBar.propTypes = {
    height: React.PropTypes.string,
    backgroundColor: React.PropTypes.string,
    inverse: React.PropTypes.string,
    color: React.PropTypes.string,
    max: React.PropTypes.number,
    value: React.PropTypes.number,
}

ProgressBar.defaultProps = {
    height: '24px',
    backgroundColor: 'gray',
    color: '#4CAF50',
    max: 100,
    inverse: false,
}