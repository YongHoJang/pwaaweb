from flask import render_template, Blueprint, jsonify
from flask import current_app, request
import json
from bson import json_util
from models import SILData


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
    # Get a iso code to fetch.
    iso_code = request.args.get('iso_code')
    # Get the sil info from db
    res_bson = current_app.db.sildata.find_one({'iso_code':iso_code})
    # If no record in db, send to user an empty response.
    if res_bson is None:
        res_json = {}
    else:
        res_json = json_util.dumps(res_bson)
    # In order to use utility to set a proper response header    
    res_obj = json.loads(res_json)
    return jsonify(res_obj)
    





