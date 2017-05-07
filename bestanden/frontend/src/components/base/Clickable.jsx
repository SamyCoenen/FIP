import React from 'react';


export default class Clickable extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            mouseOver: false,
            mouseClicking: false,
        }
    }

    render() {
        var stDiv = Object.assign({}, {
            cursor: 'pointer',
        }, this.props.style, this.state.mouseOver ? this.props.hoverStyle : null, this.state.mouseClicking ? this.props.clickStyle : null);      

        return (
            <div
                style={stDiv}
                onMouseEnter={this.onMouseEnter.bind(this)}
                onMouseLeave={this.onMouseLeave.bind(this)}
                onMouseDown={this.onMouseDown.bind(this)}
                onMouseUp={this.onMouseUp.bind(this)}
                onClick={this.props.onClick.bind(this)}
            >
                {this.props.children}
            </div>
        )
    }

    onMouseEnter() {
        this.setState({mouseOver: true});
    }

    onMouseLeave() {
        this.setState({mouseOver: false});
    }

    onMouseDown() {
        this.setState({mouseClicking: true});
    }

    onMouseUp() {
        this.setState({mouseOver: false});
        this.setState({mouseClicking: false});
    }
}

Clickable.propTypes = {
    style: React.PropTypes.object,
    hoverStyle: React.PropTypes.object,
    clickStyle: React.PropTypes.object,
    onClick: React.PropTypes.func,
}