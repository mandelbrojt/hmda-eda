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
    }
}

