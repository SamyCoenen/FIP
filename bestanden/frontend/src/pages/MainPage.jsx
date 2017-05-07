import React from 'react'
import MediaQuery from 'react-responsive'
import { log } from '../util.js'

import IncomeBox from '../components/income/IncomeBox.jsx'
import LanguagePicker from '../components/base/LanguagePicker.jsx'
import MobilityBox from '../components/mobility/MobilityBox.jsx'
import ResultBox from '../components/result/ResultBox.jsx'
import TechnologieBox from '../components/technologie/TechnologieBox.jsx'
import SocialBox from '../components/social/SocialBox.jsx'
import CharityBox from '../components/charity/CharityBox.jsx'


export default class MainPage extends React.Component {

    constructor(props) {
        super(props);

        window.onkeydown = this.handleKeyDown.bind(this);

        this.state = {
            lang: 'nl',
        }
    }

    render() {
        var stContBig = {
            display: 'flex',
            width: '900px',
            margin: '0 auto',
        };
        var stContColumnL = {
            width: '438px',
        };
        var stContColumnR = {
            width: '438px',
            marginLeft: '24px',
        };
        var stContSmall = {
            maxWidth: 600,
            minWidth: 300,
            margin: '0 auto',
            padding: '0px 4px',
        };
        var stBox = {
            marginBottom: '24px',
        };
        var incomeBox = <IncomeBox
            style={stBox}
            lang={this.state.lang}
            data={this.props.data}
            uFuncs={this.props.uFuncs}
            //onBlur={this.props.updateResult}
        />;
        var mobilityBox = <MobilityBox
            style={stBox}
            lang={this.state.lang}
            data={this.props.data}
            uFuncs={this.props.uFuncs}
            //onBlur={this.props.updateResult}
        />;
        var resultBox = <ResultBox
            style={stBox}
            lang={this.state.lang}
            data={this.props.data}
            result={this.props.data.result}
            updateResult={this.props.updateResult}
            //onBlur={this.props.onBlur}
            show={this.props.data.showResult}
        />;
        var technologieBox = <TechnologieBox
            style={stBox}
            lang={this.state.lang}
            data={this.props.data}
            uFuncs={this.props.uFuncs}
            //onBlur={this.props.updateResult}
        />
        var socialBox = <SocialBox
            style={stBox}
            lang={this.state.lang}
            data={this.props.data}
            uFuncs={this.props.uFuncs}
            //onBlur={this.props.updateResult}
        />
        var charityBox = <CharityBox
            style={stBox}
            lang={this.state.lang}
            data={this.props.data}
            uFuncs={this.props.uFuncs}
            //onBlur={this.props.updateResult}
        />
        return (
            <div>
                <LanguagePicker lang={this.state.lang} onPick={this.setLanguage.bind(this)}/>
                <MediaQuery query='(min-width: 900px)'>
                    <div style={stContBig}>
                        <div style={stContColumnL}>
                            {incomeBox}
                            {socialBox}
                        </div>
                        <div style={stContColumnR}>
                            {resultBox}
                            {mobilityBox}
                            {technologieBox}
                            {charityBox}
                        </div>
                    </div>
                </MediaQuery>
                <MediaQuery query='(max-width: 899px)'>
                    <div style={stContSmall}>
                        {incomeBox}
                        {socialBox}
                        {mobilityBox}
                        {technologieBox}
                        {charityBox}
                        {resultBox}
                    </div>
                </MediaQuery>
                <div style={{height: '48px'}}></div>
            </div>
        );
    }

    handleKeyDown(e) {
        //if keycode matches enter key
        if (e.keyCode === 13) {
            this.props.updateResult();
        }
    }

    setLanguage(lang) {
        log('changed language to: ' + lang);
        this.setState({ lang: lang });
    }
}

