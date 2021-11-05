import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler, Application
from tornado.template import Loader
import logging
import os
from API.Survey import survey_handler
from API.Base  import BaseHandler

handlers = []
handlers.extend(survey_handler.handlers)
handlers.extend([
        (r"/", BaseHandler.MainHandler),
        (r"/survey/", survey_handler.SurveyHandler),
    ])
class MultiTemplateLoader(Loader):
    """Custom template loader that manages multiple template directories.
    """
    def _create_template(self, name):
        #TODO write code for locating all the html files
        return super(MultiTemplateLoader, self)._create_template(name)

def make_app():
    template_path = os.path.join(os.path.dirname(__file__), "../Frontend")
    tloader = MultiTemplateLoader(template_path)
    app = Application(handlers,template_loader=tloader)
    return app

if __name__ == "__main__":
    logging.info("Starting...")
    app = make_app()
    app.listen(8443)
    logging.info("Listening on port 443")
    tornado.ioloop.IOLoop.current().start()