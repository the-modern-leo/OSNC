### local imports ###
from Frontend.Base import BaseHandler
from Frontend.Survey import Survey_handler
from Frontend import uimodules

### global imports ###
import tornado.ioloop
import tornado.web
from tornado.web import Application
from tornado.template import Loader
import logging
import os

sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(sh)

handlers = []
# handlers.extend(survey_handler.handlers)
handlers.extend([
        (r"/", BaseHandler.MainHandler),
    ])
handlers.extend(Survey_handler.handlers)

settings = {
    "ui_modules": uimodules,
}

def make_app():
    logger.debug("Starting...")
    template_path = os.path.join(os.path.dirname(__file__), "Frontend")
    static_files = os.path.join(os.path.dirname(__file__), "Frontend/static")
    tloader = Loader(template_path)
    app = Application(handlers,template_loader=tloader,
                      static_path=static_files,debug=True,**settings)
    return app

if __name__ == "__main__":
    app = make_app()
    app.listen(8443)
    logger.debug("Listening on port 443")
    tornado.ioloop.IOLoop.current().start()