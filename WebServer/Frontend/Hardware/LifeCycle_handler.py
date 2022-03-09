from tornado.web import RequestHandler

class LifeCycleHandler(RequestHandler):
    def get(self):
        self.render("lifecycle.html")

handlers = [
    (r"/lifecycle", LifeCycleHandler),
    (r"/lifecycle/datacenter", LifeCycleHandler),
    (r"/lifecycle/access", LifeCycleHandler),
    (r"/lifecycle/distribution", LifeCycleHandler),
    (r"/lifecycle/core", LifeCycleHandler),
]
