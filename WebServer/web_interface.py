### local imports ###
from Frontend.Base import BaseHandler
from WebServer.Frontend.Survey import Survey_handler

### global imports ###
import tornado.ioloop
import tornado.web
from tornado.web import Application
from tornado.template import Loader
import logging
import os
from pathlib import Path


handlers = []
# handlers.extend(survey_handler.handlers)
handlers.extend([
        (r"/", BaseHandler.MainHandler),
        # (r"/survey/", survey_handler.SurveyHandler),
    ])

def make_app():
    template_path = os.path.join(os.path.dirname(__file__), "Frontend")
    tloader = Loader(template_path)
    app = Application(handlers,template_loader=tloader)
    return app

if __name__ == "__main__":
    logging.info("Starting...")
    app = make_app()
    app.listen(8443)
    logging.info("Listening on port 443")
    tornado.ioloop.IOLoop.current().start()