import React from 'react';
import Color from 'color';
import { isset } from '../../util.js';

import Box from './Box.jsx';
import Clickable from './Clickable.jsx'
import DivArrowDown from './DivArrowDown.jsx';
import NoSelect from './NoSelect.jsx';
import Tooltip from 'react-tooltip-component';

export default class DivWithTabs extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        var color = new Color(this.props.color)
        return (
            <div style={this.props.style}>
                <NoSelect style={{ display: 'flex', flexWrap: 'nowrap' }}>
                    {this.getTabs()}
                </NoSelect>
                {isset(this.props.children[this.props.index]) ? this.props.children[this.props.index] : undefined}
            </div>
        );
    }

    getTabs() {
        var color = new Color(this.props.color);
        var bgColorString = color.rgb().string();
        var tabColorString = color.darken(0.25).rgb().string();
        var arrowSize = '8px';
        var tabPadding = '12px';

        var stTab = {
            flexGrow: '1',
            flexBasis: '0',
            paddingBottom: tabPadding,
            paddingTop: tabPadding,
            textAlign: 'center',
            color: '#222',
            backgroundColor: bgColorString,
        };
        var stActive = Object.assign({}, stTab, {
            fontWeight: 'bold',
            color: 'white',
            backgroundColor: tabColorString,
        });
        var stHover = {
            backgroundColor: color.darken(0.1).rgb().string(),
        };
        var stClick = {
            backgroundColor: color.lighten(0.15).rgb().string(),
        };


        return this.props.tabs.map(function (tab, index) {
            var tabComponent = this.props.index === index
                ? (<DivArrowDown arrowSize={arrowSize} arrowColor={tabColorString} offset={tabPadding}>
                    <Tooltip title={tab.tooltip} position="bottom">
                        <div>
                            {tab.title}
                        </div>
                    </Tooltip>
                </DivArrowDown>)
                : (<Tooltip title={tab.tooltip} position="bottom">
                    <div>
                        {tab.title}
                    </div>
                </Tooltip>);

            var style;
            var active = index === this.props.index;
            active ? style = stActive : style = stTab;

            return (
                <Clickable style={style} hoverStyle={stHover} clickStyle={stClick} key={index} onClick={this.props.uIndex.bind(this, index)}>
                    {tabComponent}
                </Clickable>
            )
        }, this)
    }
}

DivWithTabs.propTypes = {
    style: React.PropTypes.object,
    tabs: React.PropTypes.array,
    index: React.PropTypes.number,
    uIndex: React.PropTypes.func,
}

DivWithTabs.defaultProps = {
    index: 0,
    uIndex: function () { }
}