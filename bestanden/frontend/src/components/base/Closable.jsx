import React from 'react';
import isset from '../../util.js';

export default class Closable extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            opened: 0,
        }
    }

    render() {
        var stContainer = {}
        stContainer.default = {
            position: 'relative',
            height: '0',
            overflow: 'hidden',
            transition: 'height 0.4s ease-in-out',
        }
        stContainer.opened = Object.assign({}, stContainer.default, {
            height: 'auto',
        })

        var stSlide = {};
        stSlide.default = {
            position: 'relative',
            bottom: 0,
            /*transform: 'translate(0, -100%)', //100% here means 100% of the element itself, not the parent! very handy
            transition: 'transform 0.4s ease-in-out',*/
        }
        stSlide.opened = Object.assign({}, stSlide.default, {
            //transform: 'translate(0, 0)',
        })

        return (
            <div style={this.props.opened ? stContainer.opened : stContainer.default}>
                <div style={this.props.opened ? stSlide.opened : stSlide.default}>
                    {this.props.children}
                </div>
            </div>
        );
    }
}

Closable.propTypes = {
    style: React.PropTypes.object,
    opened: React.PropTypes.bool,
}

Closable.defaultProps = {
    opened: false,
}