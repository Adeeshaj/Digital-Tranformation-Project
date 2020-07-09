import couchdb

user = "admin"
password = "admin"
couchserver = couchdb.Server("http://%s:%s@localhost:5984/" % (user, password))

#Select/Create DB
dbname = "proposal"
if dbname in couchserver:
    db = couchserver[dbname]
else:
    db = couchserver.create(dbname)

class Proposal:
    def __init__(self, ocr_result ,file_name, proposal):

        self.__ocr_result = ocr_result
        self.__file_name = file_name
        self.__proposal = proposal

    def save(self):
        try:
            doc_id, doc_rev = db.save({
                "ocr_result": self.__ocr_result,
                "file_name": self.__file_name,
                "proposal": self.__proposal
            })
            return doc_id
        except Exception as e:
            print(e)


    def update_proposal(doc_id, proposal):
        try:
            doc = db[doc_id]
            doc["proposal"] = proposal
        except Exception as e:
            print(e)

    def update_ocr_result(doc_id, ocr_result):
        try:
            doc = db[doc_id]
            doc["ocr_result"] = ocr_result
        except Exception as e:
            print(e)



