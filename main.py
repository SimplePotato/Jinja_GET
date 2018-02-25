#!/usr/bin/env python
# coding=utf-8

import os
import jinja2
import webapp2
import datetime


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))



class MainHandler(BaseHandler):
    def get(self):

        infpo = {"sporocilo": "lalala", "posiljatelj": "", "kam_gremo": u"Storžič"}  #unicode z u-jem obvezno za šumnike

        return self.render_template("hello.html", infpo)

class MainHandler2(BaseHandler):
    def get(self):

        cas = datetime.datetime.utcnow().time()
        podatki = {"cas": cas}
        return self.render_template("ura.html", podatki)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route("/pozdrav", MainHandler),
    webapp2.Route("/ura", MainHandler2),
], debug=True)
