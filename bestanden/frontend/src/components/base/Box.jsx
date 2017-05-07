import React from 'react';
import Color from 'color';
import { title } from '../../util.js'

import Clickable from './Clickable.jsx';
import Closable from './Closable.jsx';
import NoSelect from './NoSelect.jsx';
import MediaQuery from 'react-responsive';


export default class Box extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            contentOpened: false,
        }

        this.toggleContent = this.toggleContent.bind(this);
    }

    componentDidMount() {
        this.setState({ contentOpened: this.props.startOpened })
    }

    render() {
        var bgColor = new Color(this.props.color);

        var stContainer = Object.assign({}, {
            border: 'solid 2px ' + bgColor.rgb().string(),
            boxShadow: '0px 2px 12px -2px rgba(0,0,0,0.5)',
            backgroundColor: '#fff',
        }, this.props.style);

        var stTitleContainer = {
            backgroundColor: bgColor.rgb().string(),
        };

        var stTitle = {
            color: '#fff',
            padding: '16px',
            fontWeight: 'bold',
            fontSize: '24px',
        };

        return (
            <div style={stContainer} onBlur={this.props.onBlur}>
                <Clickable style={stTitleContainer} onClick={this.toggleContent}>
                    <NoSelect><h1 style={stTitle}>{title(this.props.title)}</h1></NoSelect>
                </Clickable>
                <MediaQuery query='(max-width: 900px)'>
                    <Closable style={{ width: '100%' }} opened={this.state.contentOpened}>
                        {this.props.children}
                    </Closable>
                </MediaQuery>
                <MediaQuery query='(min-width: 900px)'>
                    <Closable style={{ width: '100%' }} opened={true}>
                        {this.props.children}
                    </Closable>
                </MediaQuery>
            </div>
        );
    }

    toggleContent() {
        this.setState({ contentOpened: !this.state.contentOpened });
    }
}

Box.propTypes = {
    style: React.PropTypes.object,
    color: React.PropTypes.string,
    startOpened: React.PropTypes.bool,
}

Box.defaultProps = {
    startOpened: false,
}