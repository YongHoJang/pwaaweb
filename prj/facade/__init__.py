from flask import Blueprint, Flask

facade_pack = Blueprint('facade', __name__, template_folder='templates', static_folder='static')

app = Flask(__name__)

import facade.views