# Terminal Run Command: python3 <path to proto_flask.py>

from flask import Flask, render_template, request
app = Flask(__name__)
# at this point, app is ready to respond to all requests with a 404 error
# we will register paths with other responses below.


# Each post is a dict with values for the form fields
posts = []


# register a path for the default method (GET)
@app.route("/")
def render_homepage():
  return render_template("full_landing_page.html")

# register a path for the GET method
# note: the paths are exact; /login/ and /LOGIN do not match this
@app.get("/login")
def render_login():
  return render_template("login_page.html")

# register a path for the GET method for forgot_password
@app.get("/forgot-password")
def render_forgot_pass():
  return "<p>Forgot Password!</p>"

@app.route("/marketplace", methods=['GET'])
def render_marketplace():
  return render_template("marketplace.html")

@app.route('/marketplace', methods=['POST'])
def post_to_marketplace():

    # Get fields from the form
    title = request.form['title']
    usage = request.form['usage']
    minquan = request.form['minquan']
    material = request.form['material']
    certifications = request.form['certifications']
    time = request.form['time']
    

    # TODO: Include 'other notes'
    # Store posts as json dict w/ specific keys
    if title and usage and minquan and material and certifications and time:
        post = {
            'title': title,
            'usage': usage,
            'minquan': minquan,
            'material': material,
            'certifications': certifications,
            'time': time
        }
        posts.append(post)

    # Pass the posts to the template
    return render_template('marketplace.html', posts=posts)




# register a path for the POST method
@app.post("/code")
def code():
  return "<p>Thanks for sending us your code</p>"

# register a path with wildcards; argument must match angle-bracketed part of path
@app.get("/welcome/<user>/<greeting>")
def get_welcome(user, greeting):
  return "<p>Hello, "+user+", thanks for telling us "+repr(greeting)+"!</p>"

# register several methods to the same function with a request body
@app.route("/echo", methods=["GET","POST"])
def echo():
  from flask import request
  return f'''<p>You used method {request.method}</p>
<p>You send the following form data: {request.form}</p>'''






# run it either with the command line invocation
#    python3 -m flask --app [name of file.py] run
# or by adding code to this file as follows:
if __name__ == '__main__':
  app.run()
