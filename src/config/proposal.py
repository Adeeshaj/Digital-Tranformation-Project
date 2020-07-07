PROPOSAL = {
    "type": None,
    "office_use": {
        "date": {
		    "year": None, "month": None, "day": None
        },
        "pb": None,
        "cp": None,
        "division_I": None,
        "j": None,
        "initial_payment": None,
        "monthly_payment": None,
        "number_of_months": None,
        "total_amount": None,
        "comments": None
    },
    "personal_inf":{
        "last_name": None,
        "all_given_names": None,
        "other_names": None,
        "occupation": None,
        "address": None,
        "apt_no": None,
        "city": None,
        "province": None,
        "postal_code": None,
        "address_since": {
            "date": {
                    "year": None, "month": None, "day": None
            }
        },
        "telephone_numbers": {
            "residence": None,
            "work": None,
            "ext": None,
            "cell": None,
            "email": None
        },
        "sin": None,
        "birthdate": {
            "date": {
                "year": None, "month": None, "day": None
            }
        },
        "gender": None,
        "marital_status": None,
        "as_of": {
            "date": {
                    "year": None, "month": None, "day": None
            }
        },
        "number_of_persons_household": None,
        "number_of_persons_under_17": None,
        "spouse_last_name": None,
        "spouse_given_name": None,
        "spouse_date_of_birth": {
        "date": {
                "year": None, "month": None, "day": None
        }
        },
        "spouse_occupation": {
            "date": {
                    "year": None, "month": None, "day": None
            }
        },
        "household_dependents": []
    },
    "employement_inf": {
            "employer": None,
            "position": None,
            "employed_since": {
            "date": {
                    "year": None, 
                    "month": None, 
                    "day": None
                }
        }
    },
    "business_inf": {
        "owned": None,
        "percentage_ownership": None,
        "self_employed": None,
        "name": None,
        "address": None,
        "city": None,
        "province": None,
        "postal_code": None,
        "details": {
            "commenced": {
                "date": {
                    "year": None, 
                    "month": None, 
                    "day": None
                }
            },
            "ceased": {
                "date": {
                    "year": None, 
                    "month": None,
                    "day": None
                }
            },
            "nature": None,
            "ownership_type": None
        },
        "percentage_debts": None,
        "partners": []
    },
    "causes_of_insolvency": {
        "opinion": None,
	    "previously_bankrupted": None,
	    "previously_proposaled": None
    },
    "transfer_assets": {
        "disposed_pleged_property": {
			"Selection": None,
			"description": None
        },
        "exess_payment_to_creditors": {
            "Selection": None,
            "description": None
        },
        "property_seized": {
            "Selection": None,
            "description": None
        },
        "sold_property": {
            "Selection": None,
            "description": None
        },
        "gifts": {
            "Selection": None,
            "description": None
        },
        "expect_money": {
            "Selection": None,
            "description": None
        },
		"comments": None
    },
    "assets": {
        "real_state": {
			"value": None,
			"description": None
        },
        "furniture": {
            "value": None,
            "description": None
        },
        "personal_effects": {
            "value": None,
            "description": None
        },
        "cash_surrender": {
            "value": None,
            "description": None
        },
        "stocks_bonds": {
            "value": None,
            "description": None
        },
        "RRSP_RRIF_GIC_RESP": {
            "value": None,
            "description": None
        },
        "automobile": {
            "value": None,
            "description": None
        },
        "recreational_vehicles": {
            "value": None,
            "description": None
        },
        "tools_of_trade": {
            "value": None,
            "description": None
        },
        "other_assets": {
            "value": None,
            "description": None
        },
        "coporation_ownerships": {
            "value": None,
            "description": None
        },
    },
    "money_owed": {
        "co_signed_to_you": None,
        "co_signed_to_anyone": None,
        "owe_for_ei_overpayement": None,
        "fines": None,
        "student_loans": None,
        "creditors": [
            {
                "name": None,
                "type_of_debt": None,
                "amount_owned": None,
                "acc_no": None,
                "secured_against": None
            }
        ],
        "total_debt_amount_debtor": None,
        "total_debt_amount_spouse": None,
        "total_debt_amount_joint": None,
        "total_debts": None,
        "creditors_more": {
            "name": None,
            "Acc_no": None
        }
    },
    "income_details": {
        "new_employment_income": {
		    "debtor": None,
		    "spouse": None
        },
        "net_employment_income": {
            "debtor": None,
            "spouse": None
        },
        "child_support": {
            "debtor": None,
            "spouse": None
        },
        "child_tax_benifit": {
            "debtor": None,
            "spouse": None
        },
        "alimony": {
            "debtor": None,
            "spouse": None
        },
        "ei": {
            "debtor": None,
            "spouse": None
        },
        "social_assistance": {
            "debtor": None,
            "spouse": None
        },
        "net_self_employment": {
            "debtor": None,
            "spouse": None
        },
        "disability": {
            "debtor": None,
            "spouse": None
        },
        "pension_oas": {
            "debtor": None,
            "spouse": None
        },
        "pension_cpp": {
            "debtor": None,
            "spouse": None
        },
        "rental_income": {
                "debtor": None,
                "spouse": None
        },
        "rental_expenses": {
            "debtor": None,
            "spouse": None
        },
        "net_rental_income": {
            "debtor": None,
            "spouse": None
        },
        "wsib_benifits": {
            "debtor": None,
            "spouse": None
        },
        "total": {
            "debtor": None,
            "spouse": None
        }        
    },
    "monthly_non_discreationary_expenses":{
        "child_support": {
		    "bankrupt": None,
		    "spouse": None
        },
        "spouse_support": {
            "bankrupt": None,
            "spouse": None
        },
        "child_care": {
            "bankrupt": None,
            "spouse": None
        },
        "medical_condition": {
            "bankrupt": None,
            "spouse": None
        }
    },
    "monthly_discreationary_expenses": {
        "housing": {
			"rent": None,
			"property_fees": None,
			"heating": None,
			"telephone": None,
			"internet": None,
			"water": None
        },
        "living": {
			"food": None,
			"laundry": None,
			"grooming": None,
			"pet_supplies": None,
			"clothing": None
        },
        "personal": {
			"alcohol": None,
			"education": None,
			"entertainment": None,
			"gifts": None,
			"dental": None
        },
        "transport_insurance": {
			"car_lease": None,
			"maintenance": None,
			"parking": None,
			"public_transport": None,
			"vehicle_insurance": None,
			"house_insurance": None,
			"life_insurance": None
        },
        "payments": {
			"to_estate": None,
			"payment_proposal": None,
			"to_estate_spousal": None,
			"payment_proposal_spousal": None,
			"to_secured_creditor": None,
			"other": None
        },
        "sub_total": None,
        "total": None
    },
    "income_history":{
        "year": None,
	    "history": [
            {
                "date": None,
                "income_source": None,
                "salary": None
            }
        ]
    }
}