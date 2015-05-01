from flask import Flask, redirect, url_for
from flask import render_template
from flask.ext.mongoengine import MongoEngine

# Set settings.
app = Flask(__name__)
app.config.from_object('settings')

# Connect mongodb
db = MongoEngine(app)


# Import packages 
from mdatastore.views import mod_mdstore
from facade.views import mod_facade
# Register blueprints
app.register_blueprint(mod_mdstore, url_prefix='/mdstore') # mdatastore is for a back end logic tier.
app.register_blueprint(mod_facade, url_prefix='/f') # facade is for a front end

@app.route('/')
def index():
    # Redirect root landing page to facade index.
    return redirect(url_for('facade.index'))
