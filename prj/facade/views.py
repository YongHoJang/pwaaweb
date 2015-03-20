from facade import app
from facade import facade_pack as package
from flask import render_template

@package.route('/')
def index():
    
    return render_template('index.html')


@package.route('/browse')
def browse():
    return render_template('browse.html')


