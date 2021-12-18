from tornado.web import RequestHandler

class SurveyHandler(RequestHandler):
    def get(self):
        self.render("survey.html")

class PowerHandler(RequestHandler):
    def get(self):
        self.render("survey_power.html")

handlers = [
    (r"/survey", SurveyHandler),
    (r"/survey/power", PowerHandler),
]