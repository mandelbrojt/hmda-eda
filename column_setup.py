# Selected columns for Exploratory Data Analysis
selected_cols = [
    "lei", "derived_msa-md", "state_code", "county_code", "census_tract",
    "conforming_loan_limit", "derived_ethnicity", "derived_race",
    "derived_sex", "action_taken", "purchaser_type", "preapproval",
    "loan_type", "loan_purpose", "lien_status", "reverse_mortgage",
    "open-end_line_of_credit", "business_or_commercial_purpose",
    "loan_amount", "interest_rate", "rate_spread", "hoepa_status",
    "total_loan_costs", "total_points_and_fees", "origination_charges",
    "discount_points", "lender_credits", "loan_term", "negative_amortization",
    "interest_only_payment", "balloon_payment", "property_value",
    "construction_method", "occupancy_type", "total_units", "applicant_age",
    "income", "debt_to_income_ratio", "applicant_credit_score_type",
    "applicant_race_observed", "applicant_sex_observed",
    "applicant_age_above_62", "submission_of_application",
    "initially_payable_to_institution", "aus-1", "denial_reason-1",
    "tract_population", "ffiec_msa_md_median_family_income",
    "tract_to_msa_income_percentage", "tract_owner_occupied_units",
    "tract_median_age_of_housing_units"
]

# Maps every column to their corresponding data type
col_dtypes = {
    "lei":"str",
    "derived_msa-md":"str",
    "state_code":"str",
    "county_code":"str",
    "census_tract":"float32",
    "conforming_loan_limit":"category",
    "derived_ethnicity":"category",
    "derived_race":"category",
    "derived_sex":"category",
    "action_taken":"category",
    "purchaser_type":"category",
    "preapproval":"category",
    "loan_type":"category",
    "loan_purpose":"category",
    "loan_purpose":"category",
    "lien_status":"category",
    "reverse_mortgage":"category",
    "open-end_line_of_credit":"category",
    "business_or_commercial_purpose":"category",
    "loan_amount":"float32",
    "interest_rate":"float32",
    "rate_spread":"float32",
    "hoepa_status":"category",
    "total_loan_costs":"float32",
    "total_points_and_fees":"float32",
    "origination_charges":"float32",
    "discount_points":"float32",
    "lender_credits":"float32",
    "loan_term":"int32",
    "negative_amortization":"category",
    "interest_only_payment":"category",
    "balloon_payment":"category",
    "property_value":"float32",
    "construction_method":"category",
    "occupancy_type":"category",
    "total_units":"category",
    "applicant_age":"category",
    "income":"float32",
    "debt_to_income_ratio":"category",
    "applicant_credit_score_type":"category",
    "applicant_race_observed":"category",
    "applicant_sex_observed":"category",
    "applicant_age_above_62":"category",
    "submission_of_application":"category",
    "initially_payable_to_institution":"category",
    "aus-1":"category",
    "denial_reason-1":"category",
    "tract_population":"float32",
    "ffiec_msa_md_median_family_income":"float32",
    "tract_to_msa_income_percentage":"float32",
    "tract_owner_occupied_units":"int32",
    "tract_median_age_of_housing_units":"int32"
}

# Maps every categorical column to their corresponding labels
cols_to_labels = {
    "conforming_loan_limit":{
        "C":"Conforming",
        "NC":"Nonconforming",
        "U":"Undetermined",
        "NA":"Not Applicable"
    },
    "action_taken":{
        1: "Loan originated",
        2: "Application approved but not accepted",
        3: "Application denied",
        4: "Application withdrawn by applicant",
        5: "File closed for incompleteness",
        6: "Purchased loan",
        7: "Preapproval request denied",
        8: "Preapproval request approved but not accepted"
    },
    "purchaser_type":{
        0:"Not applicable",
        1:"Fannie Mae",
        2:"Ginnie Mae",
        3:"Freddie Mac",
        4:"Farmer Mac",
        5:"Private securitizer",
        6:"Commercial bank, savings bank, or savings association",
        71:"Credit union, mortgage company, or finance company",
        72:"Life insurance company",
        8:"Affiliate institution",
        9:"Other type of purchaser"
    },
    "preapproval":{
        1:"Preapproval requested",
        2:"Preapproval not requested"
    },
    "loan_type":{
        1:"Conventional",
        2:"Federal Housing Administration insured",
        3:"Veterans Affairs guaranteed",
        4:"USDA Rural Housing Service or Farm Service Agency guaranteed"
    },
    "loan_purpose":{
        1:"Home purchase",
        2:"Home improvement",
        31:"Refinancing",
        32:"Cash-out refinancing",
        4:"Other purpose",
        5:"Not applicable"
    },
    "lien_status":{
        1:"Secured by a first lien",
        2:"Secured by a subordinate lien"
    },
    "reverse_mortgage":{
    1:"Reverse mortgage",
    2:"Not a reverse mortgage",
    1111:"Exempt"
    },
    "open-end_line_of_credit":{
    1:"Open-end line of credit",
    2:"Not an open-end line of credit",
    1111:"Exempt"
    },
    "business_or_commercial_purpose":{
    1:"Primarily for a business or commercial purpose",
    2:"Not primarily for a business or commercial purpose",
    1111:"Exempt"
    },
    "hoepa_status":{
    1:"High-cost mortgage",
    2:"Not a high-cost mortgage",
    3:"Not applicable"
    },
    "negative_amortization":{
    1:"Negative amortization",
    2:"No negative amortization",
    1111:"Exempt"
    },
    "interest_only_payment":{
    1:"Interest-only payments",
    2:"No interest-only payments",
    1111:"Exempt"
    },
    "balloon_payment":{
    1:"Balloon payment",
    2:"No balloon payment",
    1111:"Exempt"
    },
    "construction_method":{
    1:"Site-built",
    2:"Manufactured home"
    },
    "occupancy_type":{
    1:"Principal residence",
    2:"Second residence",
    3:"Investment property"
    },
    "applicant_credit_score_type":{
    1:"Equifax Beacon 5.0",
    2:"Experian Fair Isaac",
    3:"FICO Risk Score Classic 04",
    4:"FICO Risk Score Classic 98",
    5:"VantageScore 2.0",
    6:"VantageScore 3.0",
    7:"More than one credit scoring model",
    8:"Other credit scoring model",
    9:"Not applicable",
    1111:"Exempt"
    },
    "applicant_race_observed":{
    1:"Collected on the basis of visual observation or surname",
    2:"Not collected on the basis of visual observation or surname",
    3:"Not applicable"
    },
    "applicant_sex_observed":{
    1:"Collected on the basis of visual observation or surname",
    2:"Not collected on the basis of visual observation or surname",
    3:"Not applicable"
    },
    "submission_of_application":{
    1:"Submitted directly to your institution",
    2:"Not submitted directly to your institution",
    3:"Not applicable",
    1111:"Exempt"
    },
    "aus-1":{
    1:"Desktop Underwriter (DU)",
    2:"Loan Prospector (LP) or Loan Product Advisor",
    3:"Technology Open to Approved Lenders (TOTAL) Scorecard",
    4:"Guaranteed Underwriting System (GUS)",
    5:"Other",
    6:"Not applicable",
    7:"Internal Proprietary System",
    1111:"Exempt"
    },
    "denial_reason-1":{
    1:"Debt-to-income ratio",
    2:"Employment history",
    3:"Credit history",
    4:"Collateral",
    5:"Insufficient cash (downpayment, closing costs)",
    6:"Unverifiable information",
    7:"Credit application incomplete",
    8:"Mortgage insurance denied",
    9:"Other",
    10:"Not applicable"
    }
}
