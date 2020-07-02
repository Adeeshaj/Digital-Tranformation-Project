import couchdb

user = "admin"
password = "admin"
couchserver = couchdb.Server("http://%s:%s@couchdb:5984/" % (user, password))

#Select/Create DB
dbname = "proposal"
if dbname in couchserver:
    db = couchserver[dbname]
else:
    db = couchserver.create(dbname)

class Proposal:
    def __init__(self, key, type, file_name, office_use, personal_inf, employment_inf, business_inf, causes_of_insolvency, transfer_assests, assets, money_owed, income_details, monthly_non_discreationary_expenses, monthly_discreationary_expenses, income_history):        self.__key = key
        self.__proposal["type"] = type
        self.__proposal["office_use"] = office_use
        self.__proposal["personal_inf"] = personal_inf
        self.__proposal["employment_inf"] = employment_inf
        self.__proposal["business_inf"] = business_inf
        self.__proposal["causes_of_insolvency"] = causes_of_insolvency
        self.__proposal["transfer_assests"] = transfer_assests
        self.__proposal["assets"] = assets
        self.__proposal["money_owed"] = money_owed
        self.__proposal["income_details"] = income_details
        self.__proposal["monthly_non_discreationary_expenses"] = monthly_non_discreationary_expenses
        self.__proposal["monthly_discreationary_expenses"] = monthly_discreationary_expenses
        self.__proposal["income_history"] = income_history


def save():
    doc_id, doc_rev = db.save({self.__key: self.__proposal})
    return doc_id



