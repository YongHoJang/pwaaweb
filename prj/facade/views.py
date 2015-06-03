from flask import render_template, Blueprint, jsonify
from flask import current_app, request
import json
from bson import json_util
from models import SILData
import sys, hmac, httplib, json, time, hashlib, logging


mod_facade = Blueprint('facade', __name__, template_folder='templates', 
    static_folder='static')


@mod_facade.route('/')
def index():
    return render_template('index.html')


@mod_facade.route('/browse')
def browse():
    return render_template('browse.html')


@mod_facade.route('/getsildata')
def get_sil_data():
    print "======> view.py -> get_sil_data() "
    # Get a iso code to fetch.
    iso_code = request.args.get('iso_code')
    # Get the sil info from db
    res_bson = current_app.db.sildata.find_one({'iso_code':iso_code})
    # If no record in db, send to user an empty response.    
    if res_bson is None:
        res_json = "{}"
    else:
        res_json = json_util.dumps(res_bson)
    # In order to use utility to set a proper response header    
    res_obj = json.loads(res_json)
    print "===> res_obj : ", res_obj
    return jsonify(res_obj)
    

# jfm desc data  Ajax call
@mod_facade.route('/jfmdescdata')
def get_jfmdesc_data():
    print "======> view.py -> get_jfmdesc_data()"
    res_list = []
    # param
    languageIds = request.args.get('languageIds')
    print "===> languageIds: ", languageIds
    # Api 1
    res_str = "/v2/media-components?apiKey=55088da22fc360.94752181&subTypes=featureFilm,shortFilm&metadataLanguageTags=en&&languageIds=%s" % languageIds
    conn = httplib.HTTPSConnection("admin.arclight.org")
    conn.request("GET", res_str)
    res = conn.getresponse()
    print "===> res.reason 1: ", res.reason, res.status
    if res.reason == "OK" :
        res_str = res.read()
    else:
        res_str = "{}"
        print "===> HTTPSConnection Error "
    res_obj = json.loads(res_str)
    #print "======> res_obj 1: ", res_obj
    res_list.append(res_obj)
    # Api 2
    # https://admin.arclight.org/v2/media-components/1_jf-0-0/languages/12200?apiKey=55088da22fc360.94752181
    res_str = "/v2/media-components/1_jf-0-0/languages/%s?apiKey=55088da22fc360.94752181" % languageIds
    print "======> res_str: ", res_str
    conn = httplib.HTTPSConnection("admin.arclight.org")
    conn.request("GET", res_str)
    res = conn.getresponse()
    print "===> res.reason 2: ", res.reason, res.status
    if res.reason == "OK" :
        res_str = res.read()
    else:
        res_str = "{}"
        print "===> HTTPSConnection Error "
    res_obj = json.loads(res_str)
    #print "======> res_obj 2: ", res_obj
    res_list.append(res_obj)
    # list 
    res_json_obj = {}
    res_json_obj["data"] = res_list
    #print "======> res_json_obj: ", res_json_obj
    return jsonify(res_json_obj)



