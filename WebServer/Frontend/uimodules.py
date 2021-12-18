from tornado.web import UIModule

class HeaderNav(UIModule):
    def render(self):
        return self.render_string("nav.html")

class SideNav(UIModule):
    def render(self):
        return self.render_string("sidenav.html")

class HeaderHtml(UIModule):
    def render(self):
        return self.render_string("header.html")