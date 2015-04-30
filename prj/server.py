from flask import Flask, redirect, url_for
from flask import render_template
from mdatastore import mdatastore_pack
from facade import facade_pack
from flask.ext.mongoengine import MongoEngine

# Set settings.
app = Flask(__name__)
app.config.from_object('settings')

# Connect mongodb
db = MongoEngine(app)


# Register blueprints
app.register_blueprint(mdatastore_pack, url_prefix='/mdstore') # mdatastore is for a back end logic tier.
app.register_blueprint(facade_pack, url_prefix='/f') # facade is for a front end

@app.route('/')
def index():
    # Redirect root landing page to facade index.
    return redirect(url_for('facade.index'))

if __name__ == "__main__":
    app.debug = True
    app.run(host= '0.0.0.0')



