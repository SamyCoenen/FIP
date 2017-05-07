import React from 'react';

import InputSelect from '../../base/InputSelect.jsx'
import { strings } from '../../../strings.js'

export default class BikeFilter extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        var lang = this.props.lang;
        return (
            <div style={this.props.style}>
                <div style={{ display: 'flex' }}>
                    <InputSelect label={strings[lang]['lblBikeFilterBrand']} tooltip={strings[lang]['ttBikeFilterBrand']} onChange={this.props.brandFilterCallback} style={{ width: '100%', margin: '10px' }} options={this.props.brands} value={this.props.selectedBrand}/>
                    <InputSelect label={strings[lang]['lblBikeFilterPrice']} tooltip={strings[lang]['ttBikeFilterPrice']} onChange={this.props.priceFilterCallback} style={{ width: '100%', margin: '10px' }} options={[{ val: 'All', desc: 'All' }, { val: '1', desc: '0-25' }, { val: '2', desc: '25-35' }, { val: '3', desc: '35-55' }, { val: '4', desc: '55-75' }, { val: '5', desc: '75-95' }, { val: '6', desc: '95+' }]} value={this.props.selectedPrice} />
                </div>
            </div>
        );
    }
}