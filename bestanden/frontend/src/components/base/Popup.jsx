import React from 'react';

export default class Popup extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        if (this.props.showPopup) {
            return (
                <div style={{ position: 'fixed', top: '0', left: '0', width: '100%', height: '100%', backgroundColor: 'rgba(0,0,0,0.8)', color: 'white', zIndex: '1000' }}>
                    {this.props.children}
                </div>
            );
        } else {
            return (<div></div>);
        }
    }



}