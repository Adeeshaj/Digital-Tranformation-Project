#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2019 Zeptolytics
####################################################################################################
"""Flask Server entry point"""

##############################LIBRARY IMPORTS#######################################################
import json
from flask import Flask, request
from lib.tessaract_lib import run_ocr
from lib.proposal_lib import make_proposal_obj
from models.proposal import Proposal
####################################################################################################

APP = Flask(__name__)
APP.config['DEBUG'] = True

@APP.route("/extract/data", methods=['POST'])
def extract_ocr_data():
    doc = []
    if not request.data:
        response = {"response": {"status": 400, "error": "ValidationError", "message": "no request content found"}}
    else:
        content = request.get_json(silent=True)
        if "path" not in content:
            response = {"response": { "status": 400, "error": "ValidationError", "message": "path is required" }}
        elif "name" not in content:
            response = {"response": { "status": 400, "error": "ValidationError", "message": "name is required" }}
        else: 
            file_path = content["path"]
            file_name = content["name"]
            
            doc = run_ocr(file_path)
            proposal_obj = make_proposal_obj(doc)
            print(len(doc))
            proposal = Proposal(doc ,file_name, proposal_obj)
            proposal_id = proposal.save()
            response = {"response": { "status": 200, "data": proposal_obj }}
    print("Done!")
    return json.dumps(response)

 #invoking the app instance
if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=5000)