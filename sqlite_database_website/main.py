from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# CREATING THE APP:
app = Flask(__name__, template_folder="templates", static_folder="static")

# CREATING THE DATABASE:
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"  
db = SQLAlchemy()
db.init_app(app)


# CREATING THE TABLE:
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context(): 
    db.create_all()


@app.route("/")
def home():
    # READING ALL RECORDS:
    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
    return render_template("home.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # CREATING A NEW RECORD:
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)