from flask import Blueprint, Flask

mdatastore_pack = Blueprint('mdatastore', __name__, template_folder='templates', static_folder='static')

app = Flask(__name__)

import mdatastore.views