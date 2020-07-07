from lib.ml_lib import is_selected
from config.proposal import PROPOSAL
BOX_TYPES = {"type": "TYPE", "office_use": "OFFICE_USE", "personal_inf": "PERSONAL_INF", "employment_inf": "EMPLOYMENT_INF", "business_inf": "BUSINESS_INF", "causes_of_insolvency": "CAUSES_OF_INSOLVENCY", "transfer_assests": "TRANSFER_ASSETS", "assets": "ASSETS", "money_owed": "MONEY_OWED", "income_details": "INCOME_DETAILS", "monthly_non_discreationary_expenses": "MONTHLY_NON_DISCREATIONARY_EXPENCES", "monthly_discreationary_expenses": "MONTHLY_DISCREATIONAY_EXPENSES", "income_history": "INCOME_HISTORY", "none": "NONE"}


def make_proposal_obj(doc):
    components = identify_box_types(doc)
    if (components[BOX_TYPES["type"]]):
        PROPOSAL["type"] = get_type(components[BOX_TYPES["type"]][0])
    
    if (components[BOX_TYPES["office_use"]]):
        for box in components[BOX_TYPES["office_use"]]:
            keywords = [x.strip() for x in box["text"].split()]
            keywords = [x.lower() for x in keywords]

            if("year" in keywords or "month" in keywords or "day" in keywords):
                date = [x.strip() for x in components[BOX_TYPES["office_use"]][components[BOX_TYPES["office_use"]].index(box)-1].split()]
                if(len(date) == 3):
                    PROPOSAL["office_use"]["date"]["year"] = date[0]
                    PROPOSAL["office_use"]["date"]["month"] = date[1]
                    PROPOSAL["office_use"]["date"]["day"] = date[2]
            if("pb" in keywords or "cp" in keywords or "division" in keywords)
                if(len(keywords)> 4):
                    if("pb" in keywords):
                        PROPOSAL["office_use"]["pb"] = keywords[keywords.index("pb")+1]
                    if("cp" in keywords):
                        PROPOSAL["office_use"]["pb"] = keywords[keywords.index("cp")+1]
                    if("i" in keywords):
                        PROPOSAL["office_use"]["pb"] = keywords[keywords.index("i")+1]
                    if("j" in keywords):
                        PROPOSAL["office_use"]["pb"] = keywords[keywords.index("j")+1]
            if("payment" in keywords or "monthly" in keywords):
                for keyword in keywords:
                    flag = 0
                    if(flag>0):
                        if(flag==1 and isinstance(keyword, (int, long))):
                            PROPOSAL["office_use"]["initial_payment"] = keyword
                        if(flag==2 and isinstance(keyword, (int, long))):
                            PROPOSAL["office_use"]["monthly_payment"] = keyword
                        if(flag==3 and isinstance(keyword, (int, long))):
                            PROPOSAL["office_use"]["total_amount"] = keyword
                    if(keyword == "$"):
                        flag +=1
                    if(keyword == "#"):
                        PROPOSAL["office_use"]["number_of_months"] = keywords[keywords.index(keyword)+3]
            if("comments" in keywords):
                if(len(keywords)>1):
                    PROPOSAL["office_use"]["comments"] = " ".join(keywords[1:])
            
    return components

    

def identify_box_types(doc):
    box_type = None
    components = {}
    for page in doc:
        for box in page:
            if box_checker(box) is not BOX_TYPES["none"]:
                box_type = box_checker(box)
                components[box_type] = []
            box["type"] = box_type
            print(box)
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
    elif("questions" in keywords and "pleased" in keywords and "call" in keywords):
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




    print(keywords)

