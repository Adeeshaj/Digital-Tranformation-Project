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
####################################################################################################

APP = Flask(__name__)
APP.config['DEBUG'] = True

@APP.route("/extract/data", methods=['POST'])
def extract_ocr_data():
    if not request.data:
        response = {"response": {"ErrorCode": 400, "Status": "ValidationError", "message": "no request content found"}}
    else:
        content = request.get_json(silent=True)
        if "path" not in content:
            response = {"response": { "ErrorCode": 400, "Status": "ValidationError", "message": "path is required" }}
        elif "name" not in content:
            response = {"response": { "ErrorCode": 400, "Status": "ValidationError", "message": "name is required" }}
        else: 
            file_path = content["path"]
            file_name = content["name"]
            
            run_ocr('Form-Original-1-9.pdf')

    return 0

 #invoking the app instance
if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=5000)