from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy  # database

# flask app
app = Flask(__name__)  # app object
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'  # database URI
db = SQLAlchemy(app)  # instance of the class


# create a class which will be a table
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(), nullable=False, unique=True)
    description = db.Column(db.String(length=1000), nullable=False)  # Removed unique=True from description

with app.app_context():
    # Define items
    item = [
        Item(name="Apple Tablet", price=300, barcode="567890123456", description="A lightweight tablet for browsing."),
        Item(name="Monitor", price=250, barcode="678901234567", description="A 24-inch Full HD monitor."),
        Item(name="Mouse", price=20, barcode="789012345678", description="An ergonomic wireless mouse."),
    ]

    # Add items to the database
    db.session.add_all(items)
    db.session.commit()
    print("Items added successfully!")

with app.app_context():
    db.create_all()  # Create the database tables


# home route
@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


# market route
@app.route("/market")
def market_page():
    items = [
        {"id": 1, "name": "phone", "barcode": "5634723456", "price": '$500'},
        {"id": 2, "name": "laptop", "barcode": "3425347893", "price": '$768'},
        {"id": 3, "name": "keyboard", "barcode": "45637846578", "price": '$167'}
    ]
    return render_template("market.html", items=items)


# app run
if __name__ == "__main__":
    app.run(debug=True)
