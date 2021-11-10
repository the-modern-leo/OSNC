from tornado.web import RequestHandler


class SurveyHandler(RequestHandler):
    def get(self):
        self.write("")

    def post(self):
        self.write("")


handlers = [
    (r"/survey/.*", SurveyHandler),
    (r"/survey/datacenter", SurveyHandler),
]