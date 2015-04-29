activate_this = '/home/admin/PYENV/pwaa_project/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys, os
sys.path.insert(0, '/home/admin/PYENV/pwaa_project/pwaaweb/prj')

from server import app as application