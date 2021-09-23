import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler, Application, url
import logging

class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    logging.info("Starting...")
    app = make_app()
    app.listen(8443)
    logging.info("Listening on port 443")
    tornado.ioloop.IOLoop.current().start()