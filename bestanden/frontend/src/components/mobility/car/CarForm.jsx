import React from 'react'

import { strings } from '../../../strings.js';
import { title } from '../../../util.js'

import CarItem from './CarListItem.jsx'
import InputSelect from '../../base/InputSelect.jsx'
import InputText from '../../base/InputNumber.jsx'
import List from '../../base/List.jsx'
import CarFilter from './CarFilter.jsx'
import Button from '../../base/Button.jsx'
import Popup from '../../base/Popup.jsx'
import Clickable from '../../base/Clickable.jsx';
import NoSelect from '../../base/NoSelect.jsx';
import InputWrapper from '../../base/InputWrapper.jsx'


export default class CarForm extends React.Component {

    constructor(props) {
        super(props);
        this.cars = this.props.data.carList;
        var brands = this.cars.map(function(car) {return car.brandname.name;});
        var fuels = this.cars.map(function (car) {return car.engine_type;});
        brands.sort();
        brands.unshift("All");
        fuels.sort();
        fuels.unshift("All");

        this.state ={
            fuels:fuels.filter(this.onlyUnique),
            brands:brands.filter(this.onlyUnique),
            brandFilter:'All',
            fuelFilter:'All',
            leaseFilter:1,
            showList:false,
            brand:'',
            model:'',
        }

        window.onkeydown = this.handleKeyDown.bind(this);
    }

    render() {
        var lang = this.props.lang;
        var data = this.props.data;
        return (
            <div>
                <InputText
                    onChange={this.props.uFuncs['carLeasePrice']}
                    value={data.carLeasePrice}
                    placeholder={strings[lang]['plhInEuro']}
                    label={strings[lang]['lblCarLeasePrice']}
                    tooltip={strings[lang]['ttCarLeasePrice']}
                />
                <InputText
                    onChange={this.props.uFuncs['carPrice']}
                    value={data.carPrice}
                    placeholder={strings[lang]['plhInEuro']}
                    label={strings[lang]['lblCarPrice']}
                    tooltip={strings[lang]['ttCarPrice']}
                />
                <InputText
                    onChange={this.props.uFuncs['carCo2']}
                    value={data.carCo2}
                    placeholder={strings[lang]['plhInGpK']}
                    label={strings[lang]['lblCarCo2']}
                    tooltip={strings[lang]['ttCarCo2']}
                />
                <InputSelect
                    onChange={this.props.uFuncs['carFuel']}
                    value={data.carFuel}
                    options={[
                        {val: 'diesel', desc: strings[lang]['descDiesel']},
                        {val: 'benzine', desc: strings[lang]['descPetrol']},
                        {val: 'electric', desc: strings[lang]['descElectric']},
                    ]}
                    label={strings[lang]['lblCarFuel']}
                    tooltip={strings[lang]['ttCarFuel']}
                    placeholder={strings[lang]['plhSelect']}
                />
                {this.state.model != '' ?
                <InputWrapper label="Selected">
                    <div style={{display:"flex", width:'100%'}}>
                        <Clickable onClick={this.unselect.bind(this)}><NoSelect><div style={{width:'20px', color:'red'}}>X</div></NoSelect></Clickable><div style={{postion:'relative',}}>{this.state.brand} {this.state.model}</div>
                    </div>
                </InputWrapper>:''}
                <Button name={title(strings[lang]['btnCar'])} onClick={this.showCars.bind(this)}/>
                <Popup showPopup={this.state.showList}>
                    <div style={{padding: '12px', width:'100%', margin:'0 auto'}}>
                        <Clickable onClick={this.showCars.bind(this)}><NoSelect><div style={{position:'absolute', right:'15px', top:'5px', fontSize:'2em'}} >x</div></NoSelect></Clickable>
                        <div style={{width:'90%'}}>
                            <CarFilter lang={this.props.lang}
                                       brands={this.state.brands}
                                       fuels={this.state.fuels}
                                       categorieFilterCallback={this.uLeaseFilter.bind(this)}
                                       fuelFilterCallback={this.uFuelFilter.bind(this)}
                                       brandFilterCallback={this.uBrandFilter.bind(this)}
                                       selectedCategorie={this.state.leaseFilter}
                                       selectedFuel={this.state.fuelFilter}
                                       selectedBrand={this.state.brandFilter}
                            />
                        </div>
                        <List style={{margin: '0 auto'}}>
                            {this.cars.filter(this.filter.bind(this)).map(function (car, index) {
                                return (
                                    <div key={index} onClick={this.updateValue.bind(this, car)}>
                                        <CarItem index={index} key={index} data={car}/>
                                    </div>
                                );
                            },this)}
                        </List>
                    </div>
                </Popup>
            </div>
        );

    }
    onlyUnique(value, index, self) {
        return self.indexOf(value) === index;
    }
    filter(value) {
        if(this.state.brandFilter === 'All' && this.state.fuelFilter !== 'All'){
            return value.engine_type === this.state.fuelFilter && parseFloat(value.category) == this.state.leaseFilter;
        }else if(this.state.fuelFilter === 'All' && this.state.brandFilter !== 'All') {
            return value.brandname.name === this.state.brandFilter && parseFloat(value.category) == this.state.leaseFilter;
        }else if(this.state.fuelFilter === 'All' && this.state.brandFilter === 'All'){
            return parseFloat(value.category) == this.state.leaseFilter;
        }
        else {
            return value.brandname.name === this.state.brandFilter && value.engine_type === this.state.fuelFilter && parseFloat(value.category) == this.state.leaseFilter;
        }
    }
    uBrandFilter(e){
        this.setState({brandFilter:e.target.value});
    }
    uFuelFilter(e){
        this.setState({fuelFilter:e.target.value});
    }
    uLeaseFilter(e){
        this.setState({leaseFilter:e.target.value});
    }
    showCars(e){
        this.setState({showList: !this.state.showList});
    }
    updateValue(car, e){
        this.showCars();
        this.props.uFuncs['carLeasePrice'](car.lease_price+'');
        this.props.uFuncs['carPrice'](car.catalog_value+'');
        this.props.uFuncs['carCo2'](car.co2+'');
        this.props.uFuncs['carFuel'](car.engine_type);
        this.setState({brand:car.brandname.name ,model:car.model});
    }
    unselect(e){
        this.props.uFuncs['carLeasePrice']('');
        this.props.uFuncs['carPrice']('');
        this.props.uFuncs['carCo2']('');
        this.props.uFuncs['carFuel']('');
        this.setState({brand:'', model:''});
    }

    handleKeyDown(e) {
        //if keycode matches enter key
        if(e.keyCode === 27) {
            this.setState({showList:false});
        }
    }
}