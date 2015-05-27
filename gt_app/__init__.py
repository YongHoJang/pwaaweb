import os
from eve import Eve
from flask import render_template, redirect, url_for
from flask.ext.login import LoginManager
from schemas import domain
# for using gunicorn
from werkzeug.contrib.fixers import ProxyFix


# Setup app!
# ---
# OLD WAY
SETTINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
    'gts_settings.py')
#print 'SETTINGS_PATH', SETTINGS_PATH

EVE_SETTINGS = {
    'DOMAIN': domain,
    'MONGO_HOST': 'localhost',
    'MONGO_PORT': 27017,
    'MONGO_DBNAME': 'geotaggerdb',
    'URL_PREFIX': 'api',
    'API_VERSION': '0.1'
}

# Setup Eve for API. First, you need to configure Eve with DB params.
app = Eve(settings=EVE_SETTINGS)
# Configure your app with other settings.
app.config.from_object('settings')
#app = Eve(settings=SETTINGS_PATH)

# Blueprint Configuration
from proxy.views_factual import proxy_views
from account.views import account_views, login
from account.models import User
from dstore.views import dstore_views
#from facade.views import facade_views

app.register_blueprint(account_views, url_prefix='/account')
app.register_blueprint(proxy_views, url_prefix='/proxy')
app.register_blueprint(dstore_views, url_prefix='/dstore')
#app.register_blueprint(facade_views, url_prefix='')

# Flask-Login Configuration
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.init_app(app)
login_manager.login_view = '/user/login'

app.wsgi_app = ProxyFix(app.wsgi_app)

# Required method to connect Flask-Login with custom User class
@login_manager.user_loader
def load_user(username):
    print 'load_user - userid', username
    return User.get_with_username(username)

@app.route('/')
def index():
    return redirect(url_for('facade.index'))
