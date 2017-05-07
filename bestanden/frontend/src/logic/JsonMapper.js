import { log } from '../util.js'

export function buildRequestJson(state) {
    var jsonData = {
        income_info: {
            bruto : Number(state.wageBT),
            type_worker: state.workStatus,
            marital_status: state.maritalStatus,
            handicapped_partner: state.partnerHandicapped,
            partner_income: Number(state.partnerWage),
            partner_income_pension_or_interest: state.partnerRetirement,
            handicapped: state.handicapped,
            children_handicapped: Number(state.childrenHandicapped),
            children: Number(state.children),
            family_members: Number(state.adults),
            family_members_old: Number(state.old),
            family_members_handicapped: Number(state.adultsHandicapped),
            family_members_old_handicapped: Number(state.oldHandicapped),
        },
        social_benefits: {
            hospitalisation_partner: state.insurancePartner,
            children_hospitalisation: Number(state.insuranceChild),
            children_benefits: state.childBenefits ? Number(state.children + state.childrenHandicapped) : 0,
            retirement_saving: state.retirement
        },
        tech: {
            smartphone_value: Number(state.smartphonePrice),
            laptop_value: Number(state.laptopPrice),
            multimedia_value: Number(state.multimediaPrice),
            internet_value: Number(state.internetPrice),
        },
        charity: Number(state.charity),
    }

    if(state.mobilityOption === 'car') {
        Object.assign(jsonData,
            {car: {
                engine_type: state.carFuel,
                co2_car: Number(state.carCo2),
                catalog_value: Number(state.carPrice),
                registration_year: "2017-01-18",
                lease_price: Number(state.carLeasePrice)
            }}
        )
    }

    if(state.mobilityOption === 'bicycle') {
        Object.assign(jsonData,
            {bike: {
                lease_price: Number(state.bicycleLeasePrice)
            }}
        )
    }

    if(state.mobilityOption === 'allowance') {
        Object.assign(jsonData,
            {allowance: {
                days: Number(state.allowanceDays),
                kms: Number(state.allowanceKms),
            }}
        )
    }

    var jsonString = JSON.stringify(jsonData)
    console.log(jsonString);
    return jsonString;
}