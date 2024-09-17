from flask import Flask, render_template, request
app = Flask(__name__)

# Storage for marketplace posts
# posts = []
# Sample posts for testing
posts = [{"certifications":"None","material":"None","minquan":"100","time":"None","title":"Wood","usage":"100"},
         {"certifications":"None","material":"None","minquan":"300","time":"None","title":"Screws","usage":"200"},
         {"certifications":"None","material":"None","minquan":"500","time":"None","title":"Steel","usage":"500"}]


### LANDING PAGE ROUTE ###
@app.route("/")
def render_homepage():
  return render_template("full_landing_page.html")


### LOGIN ROUTES ###

@app.get("/login")
def render_login():
  return render_template("login_page.html")

@app.get("/posts")
def render_forgot_pass():
  return posts


### MARKETPLACE ROUTES ###

@app.route("/marketplace-view", methods=['GET'])
def render_marketplace_view():
  return render_template("marketplace-view.html", posts=posts)

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
        posts.append(post)
    return render_template("marketplace-post.html")


### RUN THE APP ###
if __name__ == '__main__':
  app.run()
