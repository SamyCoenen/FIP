import React from 'react';
import Color from 'color';

import Clickable from './Clickable.jsx';
import NoSelect from './NoSelect.jsx';

export default class Button extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        var color = new Color(this.props.color);
        var stButton = {
            width: '100%',
            backgroundColor: color.rgb().string(),
            border: 'none',
            color: 'white',
            padding: '15px 0',
            textAlign: 'center',
            textDecoration: 'none',
            display: 'inline-block',
            fontSize: '16px',
        };
        var stHover = {
            backgroundColor: color.darken(0.16).rgb().string(),
        };
        var stClick = {
            backgroundColor: color.darken(0.32).rgb().string(),
        };

        return (
            <Clickable onClick={this.props.onClick} style={stButton} hoverStyle={stHover} id="basicInput" clickStyle={stClick}>
                <NoSelect>{this.props.name}</NoSelect>
            </Clickable>
        );
    }

}
Button.propTypes = {
    color: React.PropTypes.string,
    name: React.PropTypes.string.isRequired,

}

Button.defaultProps = {
    color: '#4CAF50',
}