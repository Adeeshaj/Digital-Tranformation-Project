from lib.ml_lib import is_selected
from config.proposal import PROPOSAL
BOX_TYPES = {"type": "TYPE", "office_use": "OFFICE_USE", "personal_inf": "PERSONAL_INF", "employment_inf": "EMPLOYMENT_INF", "business_inf": "BUSINESS_INF", "causes_of_insolvency": "CAUSES_OF_INSOLVENCY", "transfer_assests": "TRANSFER_ASSETS", "assets": "ASSETS", "money_owed": "MONEY_OWED", "income_details": "INCOME_DETAILS", "monthly_non_discreationary_expenses": "MONTHLY_NON_DISCREATIONARY_EXPENCES", "monthly_discreationary_expenses": "MONTHLY_DISCREATIONAY_EXPENSES", "income_history": "INCOME_HISTORY", "none": "NONE"}


def make_proposal_obj(doc):
    doc = identify_box_types(doc)
    temp_arr = []
    for page in doc:
        for box in page:
            if(box["type"] == BOX_TYPES["type"]):
                PROPOSAL["type"] = get_type(box)


    

def identify_box_types(doc):
    box_type = None
    for page in doc:
        for box in page:
            if box_checker(box) is not "NONE":
                box_type = box_checker(box)
            box["type"] = box_type
    
    for page in doc:
        for box in page:
    return doc


def box_checker(box):
    keywords = [x.strip() for x in box["text"].split()]
    
    if("Bankruptcy" in keywords and "Consumer" in keywords and "Proposal" in keywords):
        return BOX_TYPES["type"]
    elif("OFFICE" in keywords and "USE" in keywords and "ONLY" in keywords):
        return BOX_TYPES["office_use"]
    elif("QUESTIONS" in keywords and "PLEASED" in keywords and "CALL" in keywords):
        return BOX_TYPES["personal_inf"]
    elif("EMPLOYMENT" in keywords and "INFORMATION" in keywords):
        return BOX_TYPES["employment_inf"]
    elif("BUSINESS" in keywords and "INFORMATION" in keywords):
        return BOX_TYPES["business_inf"]
    elif("CAUSES" in keywords and "OF" in keywords):
        return BOX_TYPES["causes_of_insolvency"]
    elif("TRANSFER" in keywords and "OF" in keywords and "ASSETS" in keywords):
        return BOX_TYPES["transfer_assests"]
    elif("ASSETS" in keywords):
        return BOX_TYPES["assets"]
    elif("EVERYONE" in keywords and "OWE" in keywords and "MONEY" in keywords):
        return BOX_TYPES["money_owed"]
    elif("INCOME" in keywords and "DETAILS" in keywords):
        return BOX_TYPES["income_details"]
    elif("NON-DISCRETIONARY" in keywords):
        return BOX_TYPES["monthly_non_discreationary_expenses"]
    elif("HOUSING" in keywords and "EXPENSES" in keywords):
        return BOX_TYPES["monthly_discreationary_expenses"]
    elif("EMPLOYER" in keywords and "CURRENT" in keywords and "DIFFERENT" in keywords):
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

