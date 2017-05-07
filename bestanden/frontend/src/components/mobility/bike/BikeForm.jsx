import React from 'react';

import { strings } from '../../../strings.js';
import { title } from '../../../util.js'

import BikeItem from './BikeListItem.jsx';
import BikeFilter from './BikeFilter.jsx';
import Button from '../../base/Button.jsx';
import InputNumber from '../../base/InputNumber.jsx'
import List from '../../base/List.jsx';
import Popup from '../../base/Popup.jsx';
import Clickable from '../../base/Clickable.jsx';
import NoSelect from '../../base/NoSelect.jsx';
import InputWrapper from '../../base/InputWrapper.jsx'

export default class BikeForm extends React.Component {

    constructor(props) {
        super(props);
        var brands = this.props.data.bicycleList.map(function(bike) {return bike.brandname.name;});
        var price = this.props.data.bicycleList.map(function (bike) {return bike.bike_category});
        brands.sort();
        brands.unshift("All");
        price.unshift("All");
        this.state ={
            brands:brands.filter(this.onlyUnique),
            prices:price.filter(this.onlyUnique),
            brandFilter:'All',
            priceFilter:'All',
            showList: false,
            brand:'',
            model:'',
        }
        window.onkeydown = this.handleKeyDown.bind(this);
    }

    render() {
        var lang = this.props.lang;
        return (
            <div>
                <div>
                    <InputNumber
                        onChange={this.props.uFuncs['bicycleLeasePrice']}
                        value={this.props.data['bicycleLeasePrice']}
                        placeholder={strings[lang]['plhInEuro']}
                        label={strings[lang]['lblBikeLeasePrice']}
                        tooltip={strings[lang]['ttBikeLeasePrice']}
                    />
                    {this.state.model != '' ?
                        <InputWrapper label="Selected">
                            <div style={{display:"flex", width:'100%'}}>
                                <Clickable onClick={this.unselect.bind(this)}><NoSelect><div style={{width:'20px', color:'red'}}>X</div></NoSelect></Clickable><div style={{postion:'relative',}}>{this.state.brand} {this.state.model}</div>
                            </div>
                        </InputWrapper>
                            :''}
                </div>
                <Button name={title(strings[lang]['btnBike'])} onClick={this.showBikes.bind(this)}/>
                <Popup showPopup={this.state.showList}>
                    <div style={{padding: '12px', width:'100%', margin:'0 auto',}}>
                        <Clickable onClick={this.showBikes.bind(this)}><NoSelect><div style={{position:'absolute', right:'15px', top:'5px', fontSize:'2em'}} >x</div></NoSelect></Clickable>
                        <div style={{width:'90%'}}>
                            <BikeFilter lang={lang} brands={this.state.brands} prices={this.state.prices} priceFilterCallback={this.uPriceFilter.bind(this)} brandFilterCallback={this.uBrandFilter.bind(this)} selectedBrand={this.state.brandFilter} selectedPrice={this.state.priceFilter}/>
                        </div>
                        <List style={{margin:'0 auto'}}>
                            {this.props.data.bicycleList.filter(this.filter.bind(this)).map(function (bike, index) {
                                return (
                                    <div key={index} onClick={this.updateValue.bind(this,bike)}>
                                        <BikeItem index={index} key={index} data={bike} lang={lang}/>
                                    </div>
                                );
                            },this)}
                        </List>
                    </div>
                </Popup>
            </div>
        )

    }
    onlyUnique(value, index, self) {
        return self.indexOf(value) === index;
    }
    filter(value) {
        if(this.state.brandFilter !== 'All' && this.state.priceFilter !== 'All'){
            return value.bike_category === Number(this.state.priceFilter) && value.brandname.name === this.state.brandFilter;
        }else if(this.state.brandFilter === "All" && this.state.priceFilter !== "All"){
            return value.bike_category === Number(this.state.priceFilter);
        }else if(this.state.brandFilter !== "All" && this.state.priceFilter === "All"){
            return value.brandname.name === this.state.brandFilter;
        }else {
            return true;
        }
    }
    uBrandFilter(e){
        this.setState({brandFilter:e.target.value});
    }
    uPriceFilter(e){
        console.log(e.target.value);
        this.setState({priceFilter:e.target.value});
    }
    showBikes(e){
        this.setState({showList: !this.state.showList});
    }
    updateValue(bike, e){
        this.showBikes();
        this.props.uFuncs['bicycleLeasePrice'](String(bike.lease_price).split(" ")[0]);
        this.setState({brand:bike.brandname.name, model:bike.model});
    }
    unselect(e){
        this.props.uFuncs['bicycleLeasePrice']('');
        this.setState({brand:'', model:''});
    }

    handleKeyDown(e) {
        //if keycode matches enter key
        if(e.keyCode === 27) {
            this.setState({showList:false});
        }
    }
}