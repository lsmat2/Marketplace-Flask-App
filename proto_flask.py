from flask import Flask, render_template, request, redirect, session
from flask_login import LoginManager
import re

app = Flask(__name__)
app.config.from_object('config.Config')

_posts = [{"certifications":"None","material":"None","minquan":"100","time":"None","title":"Wood","usage":"100"},
         {"certifications":"None","material":"None","minquan":"300","time":"None","title":"Screws","usage":"200"},
         {"certifications":"None","material":"None","minquan":"500","time":"None","title":"Steel","usage":"500"}]
_login_info = {}

_login_manager = None


###########################
### LANDING PAGE ROUTES ###
###########################

@app.route("/")
def render_homepage():
  return render_template("full_landing_page.html")


####################
### LOGIN ROUTES ###
####################

@app.route("/login", methods=['GET'])
def render_login():
  return render_template("login_page.html")

@app.route("/login", methods=['POST'])
def post_login():
  # Get fields from the form
  username = request.form['username']
  password = request.form['password']
  if username in _login_info and _login_info[username] == password:
    return redirect("/marketplace-view")
  else:
    return "<h1>Invalid login</h1>"
  

####################
### SIGNUP ROUTES ##
####################

@app.route("/signup", methods=['GET'])
def render_signup():
  return render_template("signup_page.html")

@app.route("/signup", methods=['POST'])
def post_signup():
  # Get fields from the form
  username = request.form['username']
  password = request.form['password']
  # Validate email format
  email_regex = r'^.+@.+\.com$'
  if not re.match(email_regex, username):
    return "<script>alert('Invalid email format'); window.location.href='/signup';</script>"
  _login_info[username] = password
  return redirect("/login")


###############################
### MARKETPLACE VIEW ROUTES ###
###############################

@app.route("/marketplace-view", methods=['GET'])
def render_marketplace_view():
  return render_template("marketplace-view.html", posts=_posts)


###############################
### MARKETPLACE POST ROUTES ###
###############################

@app.route('/marketplace-post', methods=['GET'])
def render_marketplace_post():
  return render_template("marketplace-post.html")

@app.route('/marketplace-post', methods=['POST'])
def post_to_marketplace():
    # Get fields from the form
    title = request.form['title']
    usage = request.form['usage']
    minquan = request.form['minquan']
    material = request.form['material']
    certifications = request.form['certifications']
    time = request.form['time']
    # TODO: Include 'other notes'
    if title and usage and minquan and material and certifications and time:
        post = {
            'title': title,
            'usage': usage,
            'minquan': minquan,
            'material': material,
            'certifications': certifications,
            'time': time
        }
        _posts.append(post)
    return render_template("marketplace-post.html")


###################
### RUN THE APP ###
###################

if __name__ == '__main__':
  # _login_manager = LoginManager()
  # _login_manager.init_app(app)
  app.run()