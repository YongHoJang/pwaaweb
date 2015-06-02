MONGODB_SETTINGS = {
    'db' : 'pwaadb',
    'host' : 'localhost',
    'port' : 27017
}


# -----------------------
#
# GeoTagger Server Config
#
# -----------------------

from pymongo import MongoClient

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']


# API URL CONFIG
URL_PREFIX = 'api'
API_VERSION = '0.1'


# User Package Settings
is_username_email = True
using_email_validation = True
APPKEY_LENGTH = 8

# Not in framework, I added to give option to use RECAPTCHA
RECAPTCHA_ENABLED = False 
# WTF Configuration for Rechaptcha
RECAPTCHA_USE_SSL = False
# These keys are for a testing purpose
RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'

# Flask-Mail configuration
MAIL_SERVER = '' # example: ''smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
DEFAULT_MAIL_SENDER = MAIL_USERNAME

# App Secret Key
# NEED TO CHANGE FOR EACH APP
SECRET_KEY = 'B1Xp83k/4qY1S~GIH!jnM]KES/,?CT'

# App debug mode
DEBUG = True

# ---------------------------
#
# GeoTagger Server Config End
#
# ---------------------------
