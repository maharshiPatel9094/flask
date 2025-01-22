from market import app
from flask import render_template
from market.models import Item
from market.forms import RegisterForm
# Home route
@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

# Market route
@app.route("/market")
def market_page():
    items = Item.query.all()  # Fetch all items from the database
    return render_template("market.html", items=items)

# reguister routes
@app.route("/register")
def register_page():
   form = RegisterForm() #instance of the form 
   
   return render_template("register.html",form=form)