from tornado.web import RequestHandler,Application,url

class MainHandler(RequestHandler):
    def get(self):
        self.render("MainPage.html", title="My title")

class StoryHandler(RequestHandler):
    def get(self, story_id):
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("template.html", title="My title", items=items)


app = Application([
    url(r"/", MainHandler),
    url(r"/story/([0-9]+)", StoryHandler, name="story")
    ],autoreload=True)