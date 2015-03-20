from mdatastore import app
from mdatastore import mdatastore_pack as package
from flask import render_template
from models import TestObj


@package.route('/')
def index():
    return 'mdatastore says hello'

# Delete this later
@package.route('/test_obj')
def test_obj():
    test_list = TestObj.objects.all()
    return render_template('testobj.html', objs=test_list)

# Delete this later
@package.route('/test_init')
def test_init():
    newone = TestObj(name="Mathew").save()
    anotherone = TestObj(name="Luck").save()
    return 'test init done'