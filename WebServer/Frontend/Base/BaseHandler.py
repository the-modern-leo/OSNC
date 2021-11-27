from tornado.web import RequestHandler

class MainHandler(RequestHandler):
    def get(self):
        self.render("base.html", title="OSNC - Open Source Network Controller",
                    title2="a better way to do networking")