import React from 'react'
import { title, log } from '../../util.js'
import { strings } from '../../strings.js';

import PieChart from 'react-simple-pie-chart';

import Button from '../base/Button.jsx'
import Box from '../base/Box.jsx'
import ProgressBar from '../base/ProgressBar.jsx'


export default class ResultBox extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        var lang = this.props.lang;
        var stCont = {
            padding: '12px',
        };
        var stTitle = {
            fontSize: '16px',
            marginBottom: '8px',
            fontWeight: 'bold',
        }
        var stSpaced = {
            marginTop: '24px',
        }
        var stLeft = {
            flexBasis: 0,
            flexGrow: 3,
        };
        var stRight = {
            flexBasis: 0,
            flexGrow: 2,
            marginLeft: '12px',
        };

        var showResult = this.props.result != null && this.props.show;
        if (showResult ) {
            var allocation = {
                budget: Number(this.props.result.budget),
                totalBudget: Number(this.props.result.total_budget),
                socialBudget: Number(this.props.result.social_budget),
                mobilityBudget: Number(this.props.result.mobility_budget),
                techBudget: Number(this.props.result.tech_budget),
                charity: Number(this.props.data.savedCharity),
            }
            var result = {
                yearWageNoFip: Number(this.props.result.netto_without_options * 12 + this.props.result.total_end_budget_payment),
                yearWageWithFip: Number(this.props.result.netto * 12 + this.props.result.end_budget_payment),
                allowanceValue: Number(this.props.result.allowance),
                smartphoneValue: Number(this.props.data.savedSmartphonePrice),
                multimediaValue: Number(this.props.data.savedMultimediaPrice),
                laptopValue: Number(this.props.data.savedLaptopPrice),
                internetValue: Number(this.props.data.savedInternetPrice * 12),
                charityValue: Number(this.props.data.savedCharity),
                mobilityOption: this.props.data.savedMobilityOption,
                social: Number(this.props.result.social_budget) > 0,
            };
        };

        return (
            <Box style={this.props.style} title={strings[lang]['resultBoxTitle']} color="#236192" startOpened={true}>
                { showResult && allocation.budget >= 0 ?
                    <div style={stCont}>
                        <h3 style={stTitle}>{title(strings[lang]['ttlBudgetSplit'])}</h3>
                        <div style={{display: 'flex'}}>
                            <div style={stLeft}>
                                <ValueSum
                                    items={[
                                        {desc: strings[lang]['lblBudgetTotal'], value: allocation.totalBudget},
                                        {desc: strings[lang]['lblSpentOnSocial'], value: allocation.socialBudget, color: '#00e021'},
                                        {desc: strings[lang]['lblSpentOnMobility'], value: allocation.mobilityBudget, color: '#236192'},
                                        {desc: strings[lang]['lblSpentOnTechnology'], value: allocation.techBudget, color: '#CD0400'},
                                        {desc: strings[lang]['lblSpentOnCharity'], value: allocation.charity, color: '#FF7700'},
                                        {desc: strings[lang]['lblBudgetLeft'], value: allocation.budget, color: '#777'},
                                    ]}
                                />
                            </div>
                            <div style={stRight}>
                                <PieChart
                                    slices={[
                                        { color: '#ddd', value: allocation.budget },
                                        { color: '#00e021', value: allocation.socialBudget },
                                        { color: '#236192', value: allocation.mobilityBudget },
                                        { color: '#CD0400', value: allocation.techBudget },
                                        { color: '#FF7700', value: allocation.charity },
                                    ]}
                                />
                            </div>
                        </div>
                        <div style={stSpaced}>
                            <ValueSum
                                items={[{
                                    desc: <h3 style={stTitle}>{title(strings[lang]['ttlValueNoFip'])}</h3>,
                                    value: <span style={{fontSize: '18px'}}>{'€' + Number(result.yearWageNoFip).formatMoney(2)}</span>
                                    },
                                ]}
                            />
                        </div>
                        <div style={stSpaced}>
                            <h3 style={stTitle}>{title(strings[lang]['ttlValueWithFip'])}</h3>
                            {this.renderFipValue(result)}
                        </div>
                    </div>
                : null }
                { showResult && allocation.budget < 0 ?
                    <div style={stCont}>
                        <h3 style={stTitle}>{title(strings[lang]['ttlBudgetSplit'])}</h3>
                        <ValueSum
                            items={[
                                {
                                    desc: strings[lang]['lblBudgetTotal'],
                                    value: allocation.totalBudget
                                },
                                {
                                    desc: <span style={{color: '#f00'}}>{strings[lang]['lblBudgetLeft']}</span>,
                                    value: <span style={{color: '#f00'}}>{'-€' + (-1 * Number(allocation.budget)).formatMoney(2)}</span>
                                },
                            ]}
                        />
                        <div style={stSpaced}><div style={{padding: '8px', paddingTop: '0px', fontWeight: 'bold', color: '#f00'}}>{strings[lang]['warningOverspending']}</div></div>
                    </div>
                : null }
                <Button onClick={this.props.updateResult} name={title(strings[lang]['btnResult'])} />
            </Box>
        )
    }

    renderFipValue(result) {
        var items = [];
        var lang = this.props.lang;
        var data = this.props.data;
        var total = 0;
        var totalExtra = '';

        items.push({desc: strings[lang]['strNetWageYear'], value: result.yearWageWithFip});
        total += Number(result.yearWageWithFip);
        if (result.mobilityOption === 'car') {
            items.push({desc: strings[lang]['strCar'], value: strings[lang]['strCarValue']});
            totalExtra += strings[lang]['strCar'] + ', ';
        }
        if (result.mobilityOption === 'bicycle') {
            items.push({desc: strings[lang]['strBicycle'], value: strings[lang]['strBicycleValue']});
            totalExtra += strings[lang]['strBicycle'] + ', ';
        }
        if (result.mobilityOption === 'allowance') {
            items.push({desc: strings[lang]['strAllowance'], value: result.allowanceValue});
            total += result.allowanceValue;
        }
        if (result.social) {
            items.push({desc: strings[lang]['strSocialSecurity'], value: strings[lang]['strSocialValue']});
            totalExtra += strings[lang]['strSocialSecurity'] + ', ';
        }
        if (result.smartphoneValue) {
            items.push({desc: strings[lang]['strSmartphone'], value: result.smartphoneValue});
            total += result.smartphoneValue;
        }
        if (result.multimediaValue) {
            items.push({desc: strings[lang]['strMultimedia'], value: result.multimediaValue});
            total += result.multimediaValue;
        }
        if (result.laptopValue) {
            items.push({desc: strings[lang]['strLaptop'], value: result.laptopValue});
            total += result.laptopValue;
        }
        if (result.internetValue) {
            items.push({desc: strings[lang]['strInternet'], value: result.internetValue});
            total += result.internetValue;
        }
        if (result.charityValue) {
            items.push({desc: strings[lang]['strCharity'], value: (strings[lang]['strCharityValue'] + ', -€' + Number(result.charityValue).formatMoney(2))});
            total -= result.charityValue;
        }

        if(totalExtra !== '')
            total = totalExtra.substring(0, totalExtra.length - 2) + ' ' + strings[lang]['strAnd'] + ' ' + '€' + Number(total).formatMoney(2);
        else
            total = '€' + Number(total).formatMoney(2);

        log(totalExtra);

        items.push({desc: <span style={{fontSize: '18px', fontWeight: 'bold'}}>{title(strings[lang]['strTotal'])}</span>, value: <span style={{fontSize: '18px'}}>{total}</span>});

        return <ValueSum
            items={items}
        />;
    }
}

class ValueSum extends React.Component {
    render() {
        var height = '28px';
        var stCont = {
            display: 'flex',
            height: height,
            borderTop: '1px solid #ddd',
        };
        var stLeft = {
            flexGrow: 1,
            lineHeight: height,
            fontSize: '12px',
        };
        var stRight = {
            flexGrow: 0,
            lineHeight: height,
            fontSize: '14px',
        };


        var aids =  (
            <div>
                {this.props.items.map(function(item, index) {
                    var st = index === 0 ? Object.assign({}, stCont, {borderTop: 'none'}) : stCont;
                    return <div style={st} key={index}>
                        <div style={stLeft}>{typeof item.desc === 'string' ? title(item.desc) : item.desc}</div>
                        <div style={Object.assign({}, stRight, {color: item.color})}>{
                                typeof item.value === 'number'
                                ? '€' + Number(item.value).formatMoney(2)
                                : item.value
                            }
                        </div>
                    </div>
                }, this)}
            </div>
        )
        return aids;
    }
}

//http://stackoverflow.com/questions/149055/how-can-i-format-numbers-as-money-in-javascript#149099
Number.prototype.formatMoney = function(c, d, t){
var n = this, 
    c = isNaN(c = Math.abs(c)) ? 2 : c, 
    d = d == undefined ? "," : d, 
    t = t == undefined ? "." : t, 
    s = n < 0 ? "-" : "", 
    i = String(parseInt(n = Math.abs(Number(n) || 0).toFixed(c))), 
    j = (j = i.length) > 3 ? j % 3 : 0;
   return s + (j ? i.substr(0, j) + t : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + t) + (c ? d + Math.abs(n - i).toFixed(c).slice(2) : "");
 };
