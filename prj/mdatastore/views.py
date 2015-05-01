from flask import render_template, Blueprint
from models import TestObj


# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_mdstore = Blueprint('mdatastore', __name__, template_folder='templates', 
    static_folder='static')

@mod_mdstore.route('/')
def index():
    return 'mdatastore says hello'

# Delete this later
@mod_mdstore.route('/test_obj')
def test_obj():
    test_list = TestObj.objects.all()
    return render_template('testobj.html', objs=test_list)

# Delete this later
@mod_mdstore.route('/test_init')
def test_init():
    newone = TestObj(name="Mathew").save()
    anotherone = TestObj(name="Luck").save()
    return 'test init done'