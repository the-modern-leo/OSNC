from tornado.web import RequestHandler

class SurveyHandler(RequestHandler):
    def get(self):
        self.render("survey.html")

handlers = [
    (r"/survey", SurveyHandler),
]