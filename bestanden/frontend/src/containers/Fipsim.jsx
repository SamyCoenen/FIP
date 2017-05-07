import React from 'react'
import { title } from '../util.js'
import { config } from '../config.js'
import { log } from '../util.js'
import { buildRequestJson } from '../logic/JsonMapper.js'
import { fetch } from 'whatwg-fetch'
import rest from 'rest'

import MainPage from '../pages/MainPage.jsx'


export default class Fipsim extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            //logic
            showResult: false,
            savedMobilityOption: '',
            savedSmartphonePrice: '',
            savedMultimediaPrice: '',
            savedLaptopPrice: '',
            savedInternetPrice: '',
            savedCharity: '',

            //income
            wageBT: '3000', //before taxes
            workStatus: 'bediende',
            maritalStatus: 'single',
            handicapped: false,
            partnerWage: '',
            partnerRetirement: false,
            partnerHandicapped: false,
            children: '',
            childrenHandicapped: '',
            adults: '',
            adultsHandicapped: '',
            old: '',
            oldHandicapped: '',

            //mobility
            mobilityOption: '',
            carCategory: '',
            carLeasePrice: '',
            carPrice: '',
            carCo2: '',
            carFuel: '',
            bicycleLeasePrice: '',
            allowanceDays: '',
            allowanceKms: '',

            //technologie
            smartphonePrice: '',
            multimediaPrice: '',
            laptopPrice: '',
            internetPrice: '',

            //social security
            insurancePartner: false,
            insuranceChild: '',
            retirement: false,
            childBenefits: false,

            //charity
            charity: '',

            //lists
            carList: [],
            bicycleList: [],

            //results
            result: null,
        }

        this.uFuncs = this.createUpdaters();
        this.getCarList();
        this.getBicycleList();
    }

    render() {
        return <MainPage data={this.state} uFuncs={this.uFuncs} getBikesList={this.getbicycleList} updateResult={this.updateResult.bind(this)}/>
    }

    createUpdaters() {
        var uFuncs = [];
        for (var val in this.state) {
            uFuncs[val] = this.createUpdater(val);
        }
        return uFuncs;
    }

    //creates a function to set a state property (handles both events and regular vars)
    createUpdater(key) {
        return (function (value) {
            if (typeof value === 'object' && value.target != null && value.target.value != null) {
                value = value.target.value;
            }
            try {
                this.setState({ [key]: value });
                log('updated state: ' + key + ', ' + value + ' (' + typeof value + ')');
            } catch (e) {
                log('failed to update state: ' + key);
            }
        }.bind(this))
    }

    getCarList() {
        log('attempting to fetch car list');
        var ctx = this;
        rest({
            path: config.carListUrl,
            method: 'GET',
        }).then(function (response) {
            ctx.setState({ carList: JSON.parse(response.entity) });
            log('fetched car list');
        });
    }

    getBicycleList() {
        log('attempting to fetch bicycle list');
        var ctx = this;
        rest({
            path: config.bicycleListUrl,
            method: 'GET',
        }).then(function (response) {
            ctx.setState({ bicycleList: JSON.parse(response.entity) });
            log('fetched bicycle list');
        });
    }

    updateResult() {
        log('attempting to fetch results');
        var ctx = this;
        rest({
            path: config.resultUrl,
            method: 'POST',
            headers: { 'Content-Type': "application/json" },
            entity: buildRequestJson(this.state),
        }).then(function (response) {
            try {
                ctx.setResultData(JSON.parse(response.entity));
                log('fetched results: ' + response.entity);
            } catch (e) {
                log(e);
                ctx.setState({ result: null });
                log('Failed to parse received JSON')
            }
        });
    }

    setResultData(result) {
        this.setState({
            result: result,
            showResult: true,
            savedMobilityOption: this.state.mobilityOption,
            savedSmartphonePrice: this.state.smartphonePrice,
            savedMultimediaPrice: this.state.multimediaPrice,
            savedLaptopPrice: this.state.laptopPrice,
            savedInternetPrice: this.state.internetPrice,
            savedCharity: this.state.charity,
        });
    }
}