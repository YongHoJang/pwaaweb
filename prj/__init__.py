from flask import Flask, redirect, url_for
from flask import render_template
from pymongo import Connection

# Set settings.
app = Flask(__name__)
app.config.from_object('settings')

# Connect mongodb
mongo_host = app.config['MONGODB_SETTINGS']['host']
mongo_port = app.config['MONGODB_SETTINGS']['port']
mongo_db = app.config['MONGODB_SETTINGS']['db']

connection = Connection(mongo_host, mongo_port)
app.db = connection[mongo_db]

# Import packages 
from facade.views import mod_facade
# Register blueprints
app.register_blueprint(mod_facade, url_prefix='/f') # facade is for a front end

@app.route('/')
def index():
    # Redirect root landing page to facade index.
    return redirect(url_for('facade.index'))
