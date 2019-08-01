import webapp2
import jinja2
import os

jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class AboutMe(webapp2.RequestHandler):
    def get(self):
        print("Page is working")
        about_template = jinja_current_dir.get_template("aboutme.html")
        self.response.write(about_template.render())

class Resume(webapp2.RequestHandler):
    def get(self):
        print("page is working")
        resume_template = jinja_current_dir.get_template("resume.html")
        self.response.write(resume_template.render())

class socialMedia(webapp2.RequestHandler):
    def get(self):
        print("page is working")
        socials_template = jinja_current_dir.get_template("socials.html")
        self.response.write(socials_template.render())

class rightNow(webapp2.RequestHandler):
    def get(self):
        print("page is working")
        now_template = jinja_current_dir.get_template("rightNow.html")
        self.response.write(now_template.render())

class Future(webapp2.RequestHandler):
    def get(self):
        print("page is working")
        future_template = jinja_current_dir.get_template("future.html")
        self.response.write(future_template.render())

class Past(webapp2.RequestHandler):
    def get(self):
        print("page is working")
        past_template = jinja_current_dir.get_template("past.html")
        self.response.write(past_template.render())

app = webapp2.WSGIApplication([
    ('/', AboutMe),
    ('/resume', Resume),
    ('/socials', socialMedia),
    ('/now', rightNow),
    ('/future', Future),
    ('/past', Past),
], debug=True)
