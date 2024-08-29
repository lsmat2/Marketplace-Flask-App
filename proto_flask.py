# Terminal Run Command: python3 <path to proto_flask.py>

from flask import Flask, render_template
app = Flask(__name__)
# at this point, app is ready to respond to all requests with a 404 error
# we will register paths with other responses below.



# register a path for the default method (GET)
@app.route("/")
def render_homepage():
  return render_template("full_landing_page.html")

# register a path for the GET method
# note: the paths are exact; /login/ and /LOGIN do not match this
@app.get("/login")
def render_login():
  return render_template("full_landing_page.html")

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
