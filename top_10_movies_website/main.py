from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

##CREATE DB
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


##CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()
 
 
# flask forms 
class  MovieForm(FlaskForm):
     rating = StringField("Your rating out of 10 e.g. 7.5",validators=[DataRequired()])
     review = StringField("Your review",validators=[DataRequired()])
     submit = SubmitField("Submit")
     


# home route
@app.route("/")
def home():
    result = db.session.execute(db.select(Movie))
    all_movies = result.scalars().all()
    return render_template("index.html", movie=all_movies)

# update route 
@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = MovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    # Pre-populate the form with the current movie data
    form.rating.data = str(movie.rating) if movie.rating else ""
    form.review.data = movie.review if movie.review else ""
    return render_template("edit.html", movie=movie, form=form)

# delete route --> id , delete, update 
@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie,movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)