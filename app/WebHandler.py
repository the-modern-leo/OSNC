from tornado.web import RequestHandler,Application,url
from tornado.template import Loader

class MainHandler(RequestHandler):
    def get(self):
        self.render("MainPage.html", title="NetRunner")
class VlanHandler(RequestHandler):
    def get(self):
        items = ["1", "2", "3"]
        self.render("VlanHomePage.html", title="Vlans",items=items)


app = Application([
    url(r"/", MainHandler),
    url(r"/Vlans", VlanHandler, name="Vlans"),
    ],autoreload=True,debug=True)