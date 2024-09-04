from flask import Flask, render_template, request

app = Flask(__name__)

# Each post is a dict with values for the form fields
posts = []


@app.route("/", methods=['GET'])
def render_homepage():
  return render_template("marketplace.html")

@app.route('/', methods=['POST'])
def index():

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

if __name__ == '__main__':
    app.run(port=3001)