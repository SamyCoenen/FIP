import React from 'react';
import Color from 'color';
import { isset } from '../../util.js';

import Clickable from './Clickable.jsx'
import NoSelect from './NoSelect.jsx';


export default class YesNo extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        var stContainer = {
            backgroundColor: '#eee',
        }
        var stBtn = {
            width: '50%',
        }
        var stSelected = {
            backgroundColor: '#f0f',
        }

        return (
            <Clickable style={stContainer} onClick={this.props.onClick}>
                <NoSelect style={Object.assign({}, stBtn, this.props.yes ? stSelected : {})}>
                    yes
                </NoSelect>
                <NoSelect style={Object.assign({}, stBtn, !this.props.yes ? stSelected : {})}>
                    no
                </NoSelect>
            </Clickable>
        )
    }
}

YesNo.propTypes = {
    style: React.PropTypes.object,
    yes: React.PropTypes.bool,
    onClick: React.PropTypes.func,
}

YesNo.defaultProps = {
    yes: true,
}