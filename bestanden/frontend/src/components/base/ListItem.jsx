import React from 'react';


export default class ListItem extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        var stDivBorder = {
            backgroundColor:'white',
            color:'black',
            border: 'solid 3px ',
            marginLeft: '-1px',
            marginTop: '-1px'
        };
        var st = Object.assign({}, stDivBorder, this.props.style);
        return (

            <div onClick={this.props.callback} style={st}>
                {this.props.children}
            </div>
        );
    }

};