"""
2022 Modified LAR Schema
https://ffiec.cfpb.gov/documentation/2022/modified-lar-schema/
"""

# Maps column names to data types for use in dd.read_csv
lar_dask_dtypes = {
    "activity_year":"float32",
    "lei":"object",
    "loan_type":"category",
    "loan_purpose":"category",
    "preapproval":"category",
    "construction_method":"category",
    "occupancy_type":"category",
    "loan_amount":"float32", 
    "action_taken":"category",
    "state_code":"category", 
    "county_code":"category", 
    "census_tract":"category",
    "applicant_ethnicity_1":"category",
    "applicant_ethnicity_2":"category", 
    "applicant_ethnicity_3":"category",
    "applicant_ethnicity_4":"category", 
    "applicant_ethnicity_5":"category",
    "co_applicant_ethnicity_1":"category", 
    "co_applicant_ethnicity_2":"category",
    "co_applicant_ethnicity_3":"category", 
    "co_applicant_ethnicity_4":"category",
    "co_applicant_ethnicity_5":"category", 
    "applicant_ethnicity_observed":"category",
    "co_applicant_ethnicity_observed":"category", 
    "applicant_race_1":"category",
    "applicant_race_2":"category", 
    "applicant_race_3":"category", 
    "applicant_race_4":"category",
    "applicant_race_5":"category", 
    "co_applicant_race_1":"category", 
    "co_applicant_race_2":"category",
    "co_applicant_race_3":"category", 
    "co_applicant_race_4":"category", 
    "co_applicant_race_5":"category",
    "applicant_race_observed":"category", 
    "co_applicant_race_observed":"category",
    "applicant_sex":"category", 
    "co_applicant_sex":"category", 
    "applicant_sex_observed":"category",
    "co_applicant_sex_observed":"category", 
    "applicant_age":"category", 
    "applicant_age_above_62":"category",
    "co_applicant_age":"category", 
    "co_applicant_age_above_62":"category", 
    "income":"float32",
    "purchaser_type":"category", 
    "rate_spread":"float32", 
    "hoepa_status":"category", 
    "lien_status":"category",
    "applicant_credit_scoring_model":"category", 
    "co_applicant_credit_scoring_model":"category",
    "denial_reason_1":"category", 
    "denial_reason_2":"category", 
    "denial_reason_3":"category",
    "denial_reason_4":"category", 
    "total_loan_costs":"float32", 
    "total_points_and_fees":"float32",
    "origination_charges":"float32", 
    "discount_points":"float32", 
    "lender_credits":"float32",
    "interest_rate":"float32", 
    "combined_loan_to_value_ratio":"float32", 
    "loan_term":"float32", 
    "intro_rate_period":"float32",
    "prepayment_penalty_term":"float32", 
    "debt_to_income_ratio":"category",
    "balloon_payment":"category", 
    "interest_only_payment":"category", 
    "negative_amortization":"category",
    "other_non_amortizing_features":"category",
    "property_value":"float32",
    "manufactured_home_secured_property_type":"category",
    "manufactured_home_land_property_interest":"category", 
    "total_units":"category",
    "multifamily_affordable_units":"float32",
    "submission_of_application":"category",
    "initially_payable_to_institution":"category", 
    "aus_1":"category", 
    "aus_2":"category", 
    "aus_3":"category", 
    "aus_4":"category",
    "aus_5":"category", 
    "reverse_mortgage":"category", 
    "open_end_line_of_credit":"category",
    "business_or_commercial_purpose":"category"
}

# Maps values to labels for qualitative columns
labels_to_values = {
    "loan_type":{
        "1": "Conventional",
        "2": "Federal Housing Administration",
        "3": "Veterans Affairs",
        "4": "USDA Rural Housing Service or Farm Service Agency"
    },
    "loan_purpose":{
        "1": "Home purchase",
        "2": "Home improvement",
        "31": "Refinancing",
        "32": "Cash-out refinancing",
        "4": "Other purpose",
        "5": "Not Applicable"
    },
    "preapproval":{
        "1": "Preapproval requested",
        "2": "Preapproval not requested"
    },
    "construction_method":{
        "1": "Site-built",
        "2": "Manufactured Home"
    },
    "occupancy_type":{
        "1": "Principal residence",
        "2": "Second residence",
        "3": "Investment property"
    },
    "action_taken":{
        "1": "Loan originated",
        "2": "Application approved but not accepted",
        "3": "Application denied",
        "4": "Application withdrawn by applicant",
        "5": "File closed for incompleteness",
        "6": "Purchased loan",
        "7": "Preapproval request denied",
        "8": "Preapproval request approved but not accepted"
    },
    "applicant_ethnicity_1":{
        "1": "Hispanic or Latino",
        "11": "Mexican",
        "12": "Puerto Rican",
        "13": "Cuban",
        "14": "Other Hispanic or Latino",
        "2": "Not Hispanic or Latino",
        "3": "Information not provided by applicant in mail internet or telephone application",
        "4": "Not applicable"
    },
    "applicant_ethnicity_2":{
        "1": "Hispanic or Latino",
        "11": "Mexican",
        "12": "Puerto Rican",
        "13": "Cuban",
        "14": "Other Hispanic or Latino",
        "2": "Not Hispanic or Latino"
    },
    "applicant_ethnicity_3":{
        "1": "Hispanic or Latino",
        "11": "Mexican",
        "12": "Puerto Rican",
        "13": "Cuban",
        "14": "Other Hispanic or Latino",
        "2": "Not Hispanic or Latino"
    },
    "applicant_ethnicity_4":{
        "1": "Hispanic or Latino",
        "11": "Mexican",
        "12": "Puerto Rican",
        "13": "Cuban",
        "14": "Other Hispanic or Latino",
        "2": "Not Hispanic or Latino"
    },
    "applicant_ethnicity_5":{
        "1": "Hispanic or Latino",
        "11": "Mexican",
        "12": "Puerto Rican",
        "13": "Cuban",
        "14": "Other Hispanic or Latino",
        "2": "Not Hispanic or Latino"
    },
    "co_applicant_ethnicity_1":{
        "1": "Hispanic or Latino",
        "11": "Mexican",
        "12": "Puerto Rican",
        "13": "Cuban",
        "14": "Other Hispanic or Latino",
        "2": "Not Hispanic or Latino",
        "3": "Information not provided by applicant in mail internet or telephone application",
        "4": "Not applicable",
        "5": "No co-applicant"
    },
    "co_applicant_ethnicity_1":{
        "1": "Hispanic or Latino",
        "11": "Mexican",
        "12": "Puerto Rican",
        "13": "Cuban",
        "14": "Other Hispanic or Latino",
        "2": "Not Hispanic or Latino"
    },
    "co_applicant_ethnicity_2":{
        "1": "Hispanic or Latino",
        "11": "Mexican",
        "12": "Puerto Rican",
        "13": "Cuban",
        "14": "Other Hispanic or Latino",
        "2": "Not Hispanic or Latino"
    },
    "co_applicant_ethnicity_3":{
        "1": "Hispanic or Latino",
        "11": "Mexican",
        "12": "Puerto Rican",
        "13": "Cuban",
        "14": "Other Hispanic or Latino",
        "2": "Not Hispanic or Latino"
    },
    "co_applicant_ethnicity_4":{
        "1": "Hispanic or Latino",
        "11": "Mexican",
        "12": "Puerto Rican",
        "13": "Cuban",
        "14": "Other Hispanic or Latino",
        "2": "Not Hispanic or Latino"
    },
    "co_applicant_ethnicity_5":{
        "1": "Hispanic or Latino",
        "11": "Mexican",
        "12": "Puerto Rican",
        "13": "Cuban",
        "14": "Other Hispanic or Latino",
        "2": "Not Hispanic or Latino"
    },
    "applicant_ethnicity_observed":{
        "1": "Collected on the basis of visual observation or surname",
        "2": "Not collected on the basis of visual observation or surname",
        "3": "Not applicable"
    },
    "co_applicant_ethnicity_observed":{
        "1": "Collected on the basis of visual observation or surname",
        "2": "Not collected on the basis of visual observation or surname",
        "3": "Not applicable",
        "4": "No co-applicant"
    },
    "applicant_race_1":{
        "1": "American Indian or Alaska Native",
        "2": "Asian",
        "21": "Asian Indian",
        "22": "Chinese",
        "23": "Filipino",
        "24": "Japanese",
        "25": "Korean",
        "26": "Vietnamese",
        "27": "Other Asian",
        "3": "Black or African American",
        "4": "Native Hawaiian or Other Pacific Islander",
        "41": "Native Hawaiian",
        "42": "Guamanian or Chamorro",
        "43": "Samoan",
        "44": "Other Pacific Islander",
        "5": "White",
        "6": "Information not provided by applicant in mail internet or telephone application",
        "7": "Not applicable."
    },
    "applicant_race_2":{
        "1": "American Indian or Alaska Native",
        "2": "Asian",
        "21": "Asian Indian",
        "22": "Chinese",
        "23": "Filipino",
        "24": "Japanese",
        "25": "Korean",
        "26": "Vietnamese",
        "27": "Other Asian",
        "3": "Black or African American",
        "4": "Native Hawaiian or Other Pacific Islander",
        "41": "Native Hawaiian",
        "42": "Guamanian or Chamorro",
        "43": "Samoan",
        "44": "Other Pacific Islander",
        "5": "White"
    },
    "applicant_race_3":{
        "1": "American Indian or Alaska Native",
        "2": "Asian",
        "21": "Asian Indian",
        "22": "Chinese",
        "23": "Filipino",
        "24": "Japanese",
        "25": "Korean",
        "26": "Vietnamese",
        "27": "Other Asian",
        "3": "Black or African American",
        "4": "Native Hawaiian or Other Pacific Islander",
        "41": "Native Hawaiian",
        "42": "Guamanian or Chamorro",
        "43": "Samoan",
        "44": "Other Pacific Islander",
        "5": "White"
    },
    "applicant_race_4":{
        "1": "American Indian or Alaska Native",
        "2": "Asian",
        "21": "Asian Indian",
        "22": "Chinese",
        "23": "Filipino",
        "24": "Japanese",
        "25": "Korean",
        "26": "Vietnamese",
        "27": "Other Asian",
        "3": "Black or African American",
        "4": "Native Hawaiian or Other Pacific Islander",
        "41": "Native Hawaiian",
        "42": "Guamanian or Chamorro",
        "43": "Samoan",
        "44": "Other Pacific Islander",
        "5": "White"
    },
    "applicant_race_5":{
        "1": "American Indian or Alaska Native",
        "2": "Asian",
        "21": "Asian Indian",
        "22": "Chinese",
        "23": "Filipino",
        "24": "Japanese",
        "25": "Korean",
        "26": "Vietnamese",
        "27": "Other Asian",
        "3": "Black or African American",
        "4": "Native Hawaiian or Other Pacific Islander",
        "41": "Native Hawaiian",
        "42": "Guamanian or Chamorro",
        "43": "Samoan",
        "44": "Other Pacific Islander",
        "5": "White"
    },
    "co_applicant_race_1":{
        "1": "American Indian or Alaska Native",
        "2": "Asian",
        "21": "Asian Indian",
        "22": "Chinese",
        "23": "Filipino",
        "24": "Japanese",
        "25": "Korean",
        "26": "Vietnamese",
        "27": "Other Asian",
        "3": "Black or African American",
        "4": "Native Hawaiian or Other Pacific Islander",
        "41": "Native Hawaiian",
        "42": "Guamanian or Chamorro",
        "43": "Samoan",
        "44": "Other Pacific Islander",
        "5": "White",
        "6": "Information not provided by applicant in mail internet or telephone application",
        "7": "Not applicable",
        "8": "No co-applicant"
    },
    "co_applicant_race_2":{
        "1": "American Indian or Alaska Native",
        "2": "Asian",
        "21": "Asian Indian",
        "22": "Chinese",
        "23": "Filipino",
        "24": "Japanese",
        "25": "Korean",
        "26": "Vietnamese",
        "27": "Other Asian",
        "3": "Black or African American",
        "4": "Native Hawaiian or Other Pacific Islander",
        "41": "Native Hawaiian",
        "42": "Guamanian or Chamorro",
        "43": "Samoan",
        "44": "Other Pacific Islander",
        "5": "White"
    },
    "co_applicant_race_3":{
        "1": "American Indian or Alaska Native",
        "2": "Asian",
        "21": "Asian Indian",
        "22": "Chinese",
        "23": "Filipino",
        "24": "Japanese",
        "25": "Korean",
        "26": "Vietnamese",
        "27": "Other Asian",
        "3": "Black or African American",
        "4": "Native Hawaiian or Other Pacific Islander",
        "41": "Native Hawaiian",
        "42": "Guamanian or Chamorro",
        "43": "Samoan",
        "44": "Other Pacific Islander",
        "5": "White"
    },
    "co_applicant_race_4":{
        "1": "American Indian or Alaska Native",
        "2": "Asian",
        "21": "Asian Indian",
        "22": "Chinese",
        "23": "Filipino",
        "24": "Japanese",
        "25": "Korean",
        "26": "Vietnamese",
        "27": "Other Asian",
        "3": "Black or African American",
        "4": "Native Hawaiian or Other Pacific Islander",
        "41": "Native Hawaiian",
        "42": "Guamanian or Chamorro",
        "43": "Samoan",
        "44": "Other Pacific Islander",
        "5": "White"
    },
    "co_applicant_race_5":{
        "1": "American Indian or Alaska Native",
        "2": "Asian",
        "21": "Asian Indian",
        "22": "Chinese",
        "23": "Filipino",
        "24": "Japanese",
        "25": "Korean",
        "26": "Vietnamese",
        "27": "Other Asian",
        "3": "Black or African American",
        "4": "Native Hawaiian or Other Pacific Islander",
        "41": "Native Hawaiian",
        "42": "Guamanian or Chamorro",
        "43": "Samoan",
        "44": "Other Pacific Islander",
        "5": "White"
    },
    "applicant_race_observed":{
        "1": "Collected on the basis of visual observation or surname",
        "2": "Not collected on the basis of visual observation or surname",
        "3": "Not applicable"
    },
    "co_applicant_race_observed":{
        "1": "Collected on the basis of visual observation or surname",
        "2": "Not collected on the basis of visual observation or surname",
        "3": "Not applicable",
        "4": "No co-applicant"
    },
    "applicant_sex":{
        "1": "Male",
        "2": "Female",
        "3": "Information not provided by applicant in mail internet or telephone application",
        "4": "Not applicable",
        "6": "Applicant selected both male and female"
    },
    "co_applicant_sex":{
        "1": "Male",
        "2": "Female",
        "3": "Information not provided by applicant in mail internet or telephone application",
        "4": "Not applicable",
        "5": "No co-applicant",
        "6": "Co-applicant selected both male and female"
    },
    "applicant_sex_observed":{
        "1": "Collected on the basis of visual observation or surname",
        "2": "Not collected on the basis of visual observation or surname",
        "3": "Not applicable"
    },
    "co_applicant_sex_observed":{
        "1": "Collected on the basis of visual observation or surname",
        "2": "Not collected on the basis of visual observation or surname",
        "3": "Not applicable",
        "4": "No co-applicant"
    },
    "purchaser_type":{
        "0": "Not applicable",
        "1": "Fannie Mae",
        "2": "Ginnie Mae",
        "3": "Freddie Mac",
        "4": "Farmer Mac",
        "5": "Private securitizer",
        "6": "Commercial bank savings bank or savings association",
        "71": "Credit union mortgage company or finance company",
        "72": "Life insurance Company",
        "8": "Affiliate institution",
        "9": "Other type of purchaser"
    },
    "hoepa_status":{
        "1": "High-cost mortgage",
        "2": "Not a high-cost mortgage",
        "3": "Not applicable"
    },
    "lien_status":{
        "1": "Secured by a first lien", 
        "2": "Secured by a subordinate lien"
    },
    "applicant_credit_scoring_model":{
        "1": "Equifax Beacon 5.0",
        "2": "Experian Fair Isaac",
        "3": "FICO Risk Score Classic 04",
        "4": "FICO Risk Score Classic 98",
        "5": "VantageScore 2.0",
        "6": "VantageScore 3.0",
        "7": "More than one credit scoring model",
        "8": "Other credit scoring model",
        "9": "Not applicable"
    },
    "co_applicant_credit_scoring_model":{
        "1": "Equifax Beacon 5.0",
        "2": "Experian Fair Isaac",
        "3": "FICO Risk Score Classic 04",
        "4": "FICO Risk Score Classic 98",
        "5": "VantageScore 2.0",
        "6": "VantageScore 3.0",
        "7": "More than one credit scoring model",
        "8": "Other credit scoring model",
        "9": "Not applicable",
        "10": "No co-applicant"
    },
    "denial_reason_1":{
        "1": "Debt-to-income ratio",
        "2": "Employment history",
        "3": "Credit history",
        "4": "Collateral",
        "5": "Insufficient cash (downpayment closing costs)",
        "6": "Unverifiable information",
        "7": "Credit application incomplete",
        "8": "Mortgage insurance denied",
        "9": "Other",
        "10": "Not applicable"
    },
    "denial_reason_2":{
        "1": "Debt-to-income ratio",
        "2": "Employment history",
        "3": "Credit history",
        "4": "Collateral",
        "5": "Insufficient cash (downpayment closing costs)",
        "6": "Unverifiable information",
        "7": "Credit application incomplete",
        "8": "Mortgage insurance denied",
        "9": "Other"
    },
    "denial_reason_3":{
        "1": "Debt-to-income ratio",
        "2": "Employment history",
        "3": "Credit history",
        "4": "Collateral",
        "5": "Insufficient cash (downpayment closing costs)",
        "6": "Unverifiable information",
        "7": "Credit application incomplete",
        "8": "Mortgage insurance denied",
        "9": "Other"
    },
    "denial_reason_4":{
        "1": "Debt-to-income ratio",
        "2": "Employment history",
        "3": "Credit history",
        "4": "Collateral",
        "5": "Insufficient cash (downpayment closing costs)",
        "6": "Unverifiable information",
        "7": "Credit application incomplete",
        "8": "Mortgage insurance denied",
        "9": "Other"
    },
    "balloon_payment":{
        "1": "Balloon payment",
        "2": "No balloon payment"
    },
    "interest_only_payment":{
        "1": "Interest-only payments",
        "2": "No interest-only payments"
    },
    "negative_amortization":{
        "1": "Negative amortization",
        "2": "No negative amortization"
    },
    "other_non_amortizing_features":{
        "1": "Other non-fully amortizing features",
        "2": "No other non-fully amortizing features"
    },
    "manufactured_home_secured_property_type":{
        "1": "Manufactured home and land",
        "2": "Manufactured home and not land",
        "3": "Not applicable"
    },
    "manufactured_home_land_property_interest":{
        "1": "Direct ownership",
        "2": "Indirect ownership",
        "3": "Paid leasehold",
        "4": "Unpaid leasehold",
        "5": "Not applicable"
    },
    "submission_of_application":{
        "1": "Submitted directly to your institution",
        "2": "Not submitted directly to your institution",
        "3": "Not applicable"
    },
    "initially_payable_to_institution":{
        "1": "Initially payable to your institution",
        "2": "Not initially payable to your institution",
        "3": "Not applicable"
    },
    "aus_1":{
        "1": "Desktop Underwriter (DU)",
        "2": "Loan Prospector (LP)",
        "3": "Technology Open to Approved Lenders (TOTAL) Scorecard",
        "4": "Guaranteed Underwriting System (GUS)",
        "5": "Other",
        "6": "Not applicable"
    },
    "aus_2":{
        "1": "Desktop Underwriter (DU)",
        "2": "Loan Prospector (LP)",
        "3": "Technology Open to Approved Lenders (TOTAL) Scorecard",
        "4": "Guaranteed Underwriting System (GUS)",
        "5": "Other"
    },
    "aus_3":{
        "1": "Desktop Underwriter (DU)",
        "2": "Loan Prospector (LP)",
        "3": "Technology Open to Approved Lenders (TOTAL) Scorecard",
        "4": "Guaranteed Underwriting System (GUS)",
        "5": "Other"
    },
    "aus_4":{
        "1": "Desktop Underwriter (DU)",
        "2": "Loan Prospector (LP)",
        "3": "Technology Open to Approved Lenders (TOTAL) Scorecard",
        "4": "Guaranteed Underwriting System (GUS)",
        "5": "Other"
    },
    "aus_5":{
        "1": "Desktop Underwriter (DU)",
        "2": "Loan Prospector (LP)",
        "3": "Technology Open to Approved Lenders (TOTAL) Scorecard",
        "4": "Guaranteed Underwriting System (GUS)",
        "5": "Other"
    },
    "reverse_mortgage":{
        "1": "Reverse mortgage", 
        "2": "Not a reverse mortgage"
    },
    "open_end_line_of_credit":{
        "1": "Open-end line of credit",
        "2": "Not an open-end line of credit"
    },
    "business_or_commercial_purpose":{
        "1": "Primarily for a business or commercial purpose",
        "2": "Not primarily for a business or commercial purpose"
    }
}