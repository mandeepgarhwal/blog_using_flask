from flask import Flask, render_template
from jinja2 import Environment, PackageLoader, select_autoescape
import requests

env = Environment(
    loader=PackageLoader("main"),
    autoescape=select_autoescape()
)

app = Flask(__name__)

@app.route("/")
def home():
    template = env.get_template('index.html')
    response = requests.get("https://api.npoint.io/9f3a1157ac616b94b44c")
    print(response.json())
    return template.render(allposts = response.json())
@app.route("/about")
def about():
    template = env.get_template('about.html')
    return template.render()
@app.route("/contact")
def contact():
    template = env.get_template('contact.html')
    return template.render()
@app.route("/post/<num>")
def post(num):
    template = env.get_template('post.html')
    response = requests.get("https://api.npoint.io/9f3a1157ac616b94b44c")
    allposts = response.json()
    currpost = {}
    print(num)
    print(type(num))
    for post in allposts:
        print(post)
        print(post["id"])
        if str(post["id"]) == num:
            currpost = post
            print(currpost)
    print(currpost)
    return template.render(post = currpost)


if  __name__ == "__main__":
    app.run(debug=True)