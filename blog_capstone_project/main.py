from flask import Flask, render_template
from post import Post


app = Flask(__name__)

@app.route('/')
def home():
    blogs = Post()
    return render_template("index.html",posts=blogs.posts)

@app.route("/post/<int:id>")
def get_post(id):
    blogs = Post()
    post = blogs.get_post(id)
    return render_template("post.html",title=post['title'], body=post['body'])

if __name__ == "__main__":
    app.run(debug=True)
