import React from 'react';

import { strings } from '../../../strings.js'

import InputSelect from '../../base/InputSelect.jsx';


export default class CarFilter extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        var lang = this.props.lang;
        var stCombo = {
            flexBasis: '0px',
            flexGrow: 1,
        }
        return (
            <div style={{ display: 'flex' }}>
                <InputSelect
                    style={stCombo}
                    defaultValue={this.props.carCategory}
                    options={[{ val: '1', desc: '1 (€435)' }, { val: '2', desc: '2 (€485)' }, { val: '3', desc: '3 (€585)' }]}
                    onChange={this.props.categorieFilterCallback}
                    label={strings[lang]['lblCarFilterCategory']}
                    tooltip={strings[lang]['ttCarFilterCategory']}
                    value={this.props.selectedCategorie}
                />
                <InputSelect
                    style={stCombo}
                    onChange={this.props.brandFilterCallback}
                    options={this.props.brands}
                    label={strings[lang]['lblCarFilterBrand']}
                    tooltip={strings[lang]['ttCarFilterBrand']}
                    value={this.props.selectedBrand}
                />
                <InputSelect
                    style={stCombo}
                    onChange={this.props.fuelFilterCallback}
                    options={this.props.fuels}
                    label={strings[lang]['lblCarFilterFuel']}
                    tooltip={strings[lang]['ttCarFilterFuel']}
                    value={this.props.selectedFuel}
                />
            </div>
        );
    }
}