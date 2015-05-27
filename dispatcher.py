from werkzeug.wsgi import DispatcherMiddleware
from prj import app as pwaa
from gt_app import app as gtapp
from werkzeug.serving import run_simple


application = DispatcherMiddleware(pwaa, {
    '/gtapp':     gtapp
})


# When it runs standalone in development
if __name__ == "__main__":
    application.debug = True
    run_simple('localhost', 5000, application, use_reloader=True)