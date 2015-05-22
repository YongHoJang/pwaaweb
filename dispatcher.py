from werkzeug.wsgi import DispatcherMiddleware
from prj import app as pwaa
from gt_app import app as gtapp

application = DispatcherMiddleware(pwaa, {
    '/gtapp':     gtapp
})