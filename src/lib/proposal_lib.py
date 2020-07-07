from lib.ml_lib import is_selected
from config.proposal import PROPOSAL
BOX_TYPES = {"type": "TYPE", "office_use": "OFFICE_USE", "personal_inf": "PERSONAL_INF", "employment_inf": "EMPLOYMENT_INF", "business_inf": "BUSINESS_INF", "causes_of_insolvency": "CAUSES_OF_INSOLVENCY", "transfer_assests": "TRANSFER_ASSETS", "assets": "ASSETS", "money_owed": "MONEY_OWED", "income_details": "INCOME_DETAILS", "monthly_non_discreationary_expenses": "MONTHLY_NON_DISCREATIONARY_EXPENCES", "monthly_discreationary_expenses": "MONTHLY_DISCREATIONAY_EXPENSES", "income_history": "INCOME_HISTORY", "none": "NONE"}


def make_proposal_obj(doc):
    components = identify_box_types(doc)
    if BOX_TYPES["type"] in components:
        PROPOSAL["type"] = get_type(components[BOX_TYPES["type"]][0])
    
    if BOX_TYPES["office_use"] in components:
        PROPOSAL["office_use"] = get_office_use(components[BOX_TYPES["office_use"]], PROPOSAL["office_use"])
        
    if BOX_TYPES["personal_inf"] in components:
        PROPOSAL["personal_inf"] = get_personal_inf(components[BOX_TYPES["personal_inf"]], PROPOSAL["personal_inf"])
    

    return PROPOSAL

    

def identify_box_types(doc):
    box_type = None
    components = {}
    for page in doc:
        for box in page:
            if box_checker(box) is not BOX_TYPES["none"]:
                box_type = box_checker(box)
                components[box_type] = []
            box["type"] = box_type
            if box_type is not None:
                components[box_type].append(box)
    
    return components


def box_checker(box):
    keywords = [x.strip() for x in box["text"].split()]
    keywords = [x.lower() for x in keywords]

    if("bankruptcy" in keywords and "consumer" in keywords and "proposal" in keywords):
        return BOX_TYPES["type"]
    elif("office" in keywords and "use" in keywords and "only" in keywords):
        return BOX_TYPES["office_use"]
    elif("please" in keywords and "complete" in keywords and "sign" in keywords):
        return BOX_TYPES["personal_inf"]
    elif("employment" in keywords and "information" in keywords):
        return BOX_TYPES["employment_inf"]
    elif("business" in keywords and "information" in keywords):
        return BOX_TYPES["business_inf"]
    elif("cuases" in keywords and "of" in keywords):
        return BOX_TYPES["causes_of_insolvency"]
    elif("transfer" in keywords and "of" in keywords and "assets" in keywords):
        return BOX_TYPES["transfer_assests"]
    elif("assets" in keywords):
        return BOX_TYPES["assets"]
    elif("everyone" in keywords and "owe" in keywords and "money" in keywords):
        return BOX_TYPES["money_owed"]
    elif("income" in keywords and "details" in keywords):
        return BOX_TYPES["income_details"]
    elif("non-discreationary" in keywords):
        return BOX_TYPES["monthly_non_discreationary_expenses"]
    elif("housing" in keywords and "expenses" in keywords):
        return BOX_TYPES["monthly_discreationary_expenses"]
    elif("employer" in keywords and "current" in keywords and "different" in keywords):
        return BOX_TYPES["income_history"]
    else: 
        return BOX_TYPES["none"]

def get_type(box):
    default = "CONSUMER"
    keywords = [x.strip() for x in box["text"].split()]
    if (keywords.index("Bankruptcy") != 0 and is_selected(keywords[keywords.index("Bankruptcy")-1])):
        return "BANKRUPTCY"
    elif (keywords.index("Consumer") != 0 and is_selected(keywords[keywords.index("Consumer")-1])):
        return "CONSUMER"
    else:
        return default

def get_office_use(boxes, office_use):
    for box in boxes:
        keywords = [x.strip() for x in box["text"].split()]
        keywords = [x.lower() for x in keywords]

        if("year" in keywords or "month" in keywords or "day" in keywords):
            date = [x.strip() for x in boxes[boxes.index(box)-1]["text"].split()]
            if(len(date) == 3):
                office_use["date"] = {
                    "year": date[0],
                    "month": date[1],
                    "day": date[2]
                }
        if("pb" in keywords or "cp" in keywords or "division" in keywords):
            if(len(keywords)> 4):
                if("pb" in keywords):
                   office_use["pb"] = keywords[keywords.index("pb")+1]
                if("cp" in keywords):
                   office_use["pb"] = keywords[keywords.index("cp")+1]
                if("i" in keywords):
                   office_use["pb"] = keywords[keywords.index("i")+1]
                if("j" in keywords):
                   office_use["pb"] = keywords[keywords.index("j")+1]
        if("payment" in keywords or "monthly" in keywords):
            for keyword in keywords:
                flag = 0
                if(flag>0):
                    if(flag==1 and isinstance(keyword, (int, long))):
                       office_use["initial_payment"] = keyword
                    if(flag==2 and isinstance(keyword, (int, long))):
                       office_use["monthly_payment"] = keyword
                    if(flag==3 and isinstance(keyword, (int, long))):
                       office_use["total_amount"] = keyword
                if(keyword == "$"):
                    flag +=1
                if(keyword == "#"):
                   office_use["number_of_months"] = keywords[keywords.index(keyword)+3]
        if("comments" in keywords):
            if(len(keywords)>1):
               office_use["comments"] = " ".join(keywords[1:])
    return office_use
        
def get_personal_inf(boxes, personal_inf):
    for box in boxes:
        keywords = [x.strip() for x in box["text"].split()]
        keywords = [x.lower() for x in keywords]

        if(("name:" in keywords or "name" in keywords) and "given" in keywords):
            if(len(keywords)>0):
                names_1 = [x.strip() for x in boxes[boxes.index(box)+1]["text"].split()]
                personal_inf["last_name"] = names_1[0]
                personal_inf["all_given_names"] = " ".join(names_1[1:])
        if(("known" in keywords or "other" in keywords) and "occupation:" in keywords):
            if(len(keywords)>0):
                names_2 = [x.strip() for x in boxes[boxes.index(box)+1]["text"].split()]
                personal_inf["occupation"] = " ".join(names_2[-2:])
                personal_inf["other_names"] = " ".join(names_2[:-2])
        if("address" in keywords or "city" in keywords):
            if(len(keywords)>0):
                names_3 = [x.strip() for x in boxes[boxes.index(box)+1]["text"].split()]
                personal_inf["city"] = " ".join(names_3[-1:])
                personal_inf["apt_no"] = " ".join(names_3[-2:-1])
                personal_inf["address"] = " ".join(names_3[:-3])
        if(("province:" in keywords or "province" in keywords) and "postal" in keywords):
            if(len(keywords)>0):
                names_4 = [x.strip() for x in boxes[boxes.index(box)+1]["text"].split()]
                if(len(names_4)>0):
                    personal_inf["province"] = " ".join(names_4[0])
                if(len(names_4)>1):
                    personal_inf["postal_code"] = " ".join(names_4[1])
                if(len(names_4)>4):
                    personal_inf["address_since"] = {
                        "year": names_4[3],
                        "month": names_4[2],
                        "day": names_4[1]
                    }
        if("level" in keywords or "education" in keywords):
            names_5 = [x.strip() for x in boxes[boxes.index(box)+1]["text"].split()]
            personal_inf["city"] = " ".join(names_5)
        if("residence:" in keywords and "work:" in keywords and "ext" in keywords):
            personal_inf["telephone_numbers"] = {
                "residence": " ".join(keywords[keywords.index("residence:")+1:keywords.index("work:")]),
                "work": " ".join(keywords[keywords.index("work:")+1:keywords.index("ext")]),
                "ext":  " ".join(keywords[keywords.index("ext")+1:]),
                "cell": None,
                "email": None
            }
        if ("cell:" in keywords):
            if "telephone_numbers" not in personal_inf:
                personal_inf["telephone_numbers"] = {
                    "residence": None,
                    "work": None,
                    "ext":  None,
                    "cell": " ".join(keywords[1:]),
                    "email": None
                }
            else:
                personal_inf["telephone_numbers"]["cell"] =  " ".join(keywords[1:])
        if ("email:" in keywords):
            if "telephone_numbers" not in personal_inf:
                personal_inf["telephone_numbers"] = {
                    "residence": None,
                    "work": None,
                    "ext":  None,
                    "cell": None,
                    "email":  "".join(keywords[1:])
                }
            else:
                personal_inf["telephone_numbers"]["email"] =  "".join(keywords[1:])
        if("birthdate:" in keywords or "gender:" in keywords):
            names_6 = [x.strip() for x in boxes[boxes.index(box)+1]["text"].split()]
            if(len(names_6)>0):
                personal_inf["sin"] = " ".join(names_3[:3])
                personal_inf["gender"] = "F" if names_6[-1].lower()=="m" else "M" 
                if(len(names_6)>6):
                    personal_inf["birthdate"] = {
                            "year": names_6[4],
                            "month": names_6[5],
                            "day": names_6[6]
                        }
        if("marital" in keywords or "status:" in keywords):
            names_7 = [x.strip() for x in boxes[boxes.index(box)+1]["text"].split()]
            names_8 = [x.strip() for x in boxes[boxes.index(box)+2]["text"].split()]
            names_7 = [x.lower() for x in names_7]

            if ("common-law:" in names_7 and names_7.index("common-law:") != 0 and is_selected(names_7[names_7.index("common-law:")-1])):
                 personal_inf["marital_status"]: "COMMON_LAW"
            elif ("single:" in names_7 and names_7.index("single:") != 0 and is_selected(names_7[names_7.index("single:")-1])):
                 personal_inf["marital_status"]: "SINGLE"
            elif ("divorced:" in names_7 and names_7.index("divorced:") != 0 and is_selected(names_7[names_7.index("divorced:")-1])):
                 personal_inf["marital_status"]: "DIVORCED"
            elif ("separated:" in names_8 and names_8.index("separated:") != 0 and is_selected(names_8[names_8.index("separated:")-1])):
                 personal_inf["marital_status"]: "SEPARATED"
            elif ("married:" in names_8 and names_8.index("married:") != 0 and is_selected(names_8[names_8.index("married:")-1])):
                 personal_inf["marital_status"]: "MARRIED"
            elif ("widowed:" in names_8 and names_8.index("widowed:") != 0 and is_selected(names_8[names_8.index("widowed:")-1])):
                 personal_inf["marital_status"]: "WIDOWED"
            
            if(len(names_8)>3):
                personal_inf["as_of"]: {
                    "date": {
                        "year": names_8[-3], "month": names_8[-2], "day": names_8[-1]
                    }
                }
        if("debtor:" in keywords and "household" in keywords):
            personal_inf["number_of_persons_household"]: keywords[-1] if keywords[-1]!="debtor:" else 0
        if("financial" in keywords and "under" in keywords): 
            personal_inf["number_of_persons_under_17"] = keywords[-1] if keywords[-1]!="support:" else 0
        
        if("spouse" in keywords and "name" in keywords):
            names_9 = [x.strip() for x in boxes[boxes.index(box)+1]["text"].split()]
            if(len(names_9)>0):
                personal_inf["spouse_last_name"] = names_9[0]
                personal_inf["spouse_given_name"] = " ".join(names_9[1:])
        if("birth" in keywords and "occupation" in keywords):
            names_10 = [x.strip() for x in boxes[boxes.index(box)+1]["text"].split()]
            if(len(names_10)>0):
                personal_inf["spouse_occupation"] = names_10[-1]
            if(len(names_10)>2):
                personal_inf["spouse_date_of_birth"] = {
                    "date": {
                        "year": names_10[0], "month": names_10[1], "day": names_10[2]
                    }
                }
        if("information" in keywords and "dependents" in keywords):
            index = boxes.index(box)+2
            while (index<len(boxes)):
                names_11 = [x.strip() for x in boxes[index]["text"].split()]
                if len(names_11)>2:
                    personal_inf["household_dependents"].append(
                        {
                            "name": names_11[0],
                            "relationship": names_11[1],
                            "date_of_birth": names_11[2] 
                        }
                    )
                index += 1
    return personal_inf                    




            




