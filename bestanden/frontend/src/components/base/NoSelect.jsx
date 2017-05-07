import React from 'react';


export default class NoSelect extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        var stSpan = Object.assign({}, {
            WebkitTouchCallout: 'none',
            WebkitUserSelect: 'none',
            MozUserSelect: 'none',
            msUserSelect: 'none',
            userSelect: 'none',
            cursor: 'default',
        }, this.props.style);

        return (
            <span style={stSpan}>
                {this.props.children}
            </span>
        )
    }
}