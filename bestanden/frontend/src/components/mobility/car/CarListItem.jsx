/**
 * Created by cyril on 9/12/16.
 */
import React from 'react';

import Listitem from '../../base/ListItem.jsx';


export default class CarListItem extends React.Component {

    constructor(props) {
        super(props);
        this.state={
            active: false
        }
    }

    render() {
        var stTd = {
            fontSize: '12px',
        };

        var stBox = {
            width:'380px',
            height:'240px',
        };

        return (
                <Listitem style={stBox} callback={this.props.carCallback}>
                    <div style={{height:'200px', width:'380px'}}>
                            <img style={{maxWidth:'100%', maxHeight:'100%'}} src={'/assets/images/cars/'+this.props.data.image_url}/>
                    </div>
                    <div>{this.props.data.brandname.name} {this.props.data.model}</div>
                    <div style={stTd}>Engine: {this.props.data.engine_type} </div>
                    <div style={stTd}>Emissions: {this.props.data.co2}</div>
                </Listitem>
        );
    }
    test(){
    }
}