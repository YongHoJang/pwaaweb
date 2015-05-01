from flask import render_template, Blueprint

mod_facade = Blueprint('facade', __name__, template_folder='templates', 
    static_folder='static')


@mod_facade.route('/')
def index():
    
    return render_template('index.html')


@mod_facade.route('/browse')
def browse():
    return render_template('browse.html')


