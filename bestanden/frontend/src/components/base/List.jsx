import React from 'react';
import ListItems from './List.jsx';


export default class List extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            activeItem: -1,
        }
    }

    render() {
        return (
            <div style={{ height: '100%', overflowY: 'scroll' }}>
                <div style={{ display: 'flex', flexWrap: 'wrap', padding: '10px', height: 'auto', marginBottom: '100px' }}>
                    {this.props.children}
                </div>
            </div>
        );
    }

};