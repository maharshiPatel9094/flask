from flask import Flask, render_template
import requests

#USE YOUR OWN npoint LINK! OTHERWISE IT WILL NOT WORK 👇
posts = requests.get(" https://api.npoint.io/43f1081e1c8713f30011").json()
# print(posts)

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
