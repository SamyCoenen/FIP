import React from 'react';

import Listitem from '../../base/ListItem.jsx';
import { strings } from '../../../strings.js';

export default class BikeListItem extends React.Component {

    constructor(props) {
        super(props);
        this.state={
            active: false
        }
    }

    render() {
        var stTd = {
            fontSize: '20px'
        };
        var stBox = {
            width:'380px',
            height:'240px',
        };
        var trimmed = this.props.data.model.substring(0, 30);
        return (
            <Listitem style={stBox} callback={this.props.bikeCallback}>
                <div style={{height:'200px', width:'380px'}}>
                    <img style={{display:'block', maxWidth:'100%', maxHeight:'100%'}} src={"/assets/images/"+this.props.data.image_location}/>
                </div>
                {this.props.data.brandname.name} {trimmed.substring(0, Math.min(trimmed.length, trimmed.lastIndexOf(" ")))}
                <div style={stTd}>{strings[this.props.lang]['plhPrice']} {this.props.data.lease_price}</div>
            </Listitem>
        );
    }
}