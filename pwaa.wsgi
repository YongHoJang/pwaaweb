activate_this = '/home/admin/PYENV/pwaaweb/ENV/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys, os
sys.path.insert(0, '/home/admin/PYENV/pwaaweb/prj')

from prj import app as application
