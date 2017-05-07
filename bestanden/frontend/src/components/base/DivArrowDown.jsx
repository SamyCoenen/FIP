import React from 'react';


export default class DivArrowDown extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        var arrowSize = this.props.arrowSize;

        var stArrowContainerOuter = {
            position: 'relative',
            width: '100%',
        }
        var stArrow = {
            position: 'absolute',
            top: this.props.offset,
            left: 'calc(50% - ' + this.props.arrowSize + ')',
            width: 0,
            height: 0,
            margin: '0 auto',
            borderLeft: arrowSize + ' solid transparent',
            borderRight: arrowSize + ' solid transparent',
            borderTop: arrowSize + ' solid ' + this.props.arrowColor,
        }

        return (
            <div style={this.props.style}>
                <div>
                    {this.props.children}
                </div>
                <div style={stArrowContainerOuter}>
                    <div style={stArrow}></div>
                </div>
            </div>
        );
    }

}