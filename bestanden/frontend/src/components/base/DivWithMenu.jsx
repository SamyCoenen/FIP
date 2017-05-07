import React from 'react';
import { isset } from '../../util.js';

import Clickable from './Clickable.jsx'


export default class DivWithMenu extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            opened: false,
        }

        this.toggleOpen = this.toggleOpen.bind(this);
    }

    render() {
        var values = {};
        if (this.props.location === 'right') {
            values = {
                left: '100%',
                transformClose: 'translate(0, 0)',
                transformOpen: 'translate(-100%, 0)',
                pullyTransform: 'translate(-100%, 0%)',
                pullyLeft: 0,
            }
        }
        if (this.props.location === 'left') {
            values = {
                left: 0,
                transformClose: 'translate(-100%, 0)',
                transformOpen: 'translate(0, 0)',
                pullyTransform: 'translate(0%, 0%)',
                pullyLeft: '100%',
            }
        }

        var stDiv = Object.assign({}, this.props.style, {
            position: 'relative',
        })

        var stSlideContainer = {}
        stSlideContainer.regular = {
            position: 'absolute',
            height: '100%',
            minWidth: 0,
            left: values.left,
            transform: values.transformClose,
            transition: 'transform ' + this.props.duration + ' ease-in-out',
        }
        stSlideContainer.opened = Object.assign({}, stSlideContainer.regular, {
            transform: values.transformOpen,
        })

        var stContainerNoOverflow = {
            position: 'absolute',
            height: '100%',
            width: '100%',
            top: '0%',
            overflow: 'hidden',
            pointerEvents: 'none',
        }

        var stContainer = {
            position: 'relative',
            width: '100%',
            height: '100%',
            pointerEvents: 'auto',
            zIndex: '3',
        }

        var stPully = {
            position: 'absolute',
            left: values.pullyLeft,
            transform: values.pullyTransform,
            zIndex: '-2',
        }

        var opened = isset(this.props.opened) ? this.props.opened : this.state.opened;

        return (
            <div id="container" style={stDiv}>
                <div style={stContainerNoOverflow}>
                    <div style={opened ? stSlideContainer.opened : stSlideContainer.regular}>
                        <div style={stContainer}>
                            {isset(this.props.pully)
                                ? <div style={stPully}>
                                    <Clickable onClick={this.toggleOpen}>
                                        {this.props.pully}
                                    </Clickable>
                                </div>
                                : null
                            }
                            {this.props.menu}
                        </div>
                    </div>
                </div>
                {this.props.children}
            </div>

        );
    }

    toggleOpen() {
        this.props.openCallback(!this.props.opened);
        this.setState({ opened: !this.state.opened });
    }
}

DivWithMenu.propTypes = {
    style: React.PropTypes.object,
    opened: React.PropTypes.bool,
    openCallback: React.PropTypes.func,
    location: React.PropTypes.string,
    duration: React.PropTypes.string,
    pully: React.PropTypes.element,

    menu: React.PropTypes.element.isRequired,
}

DivWithMenu.defaultProps = {
    openCallback: function () { },
    location: 'right',
    duration: '0.3s',
}