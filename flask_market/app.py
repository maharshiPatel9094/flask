from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Flask app setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Suppress warning

db = SQLAlchemy(app)  # Database instance

# Create the Item table
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(), nullable=False, unique=True)
    description = db.Column(db.String(length=1000), nullable=False)

    def __repr__(self):
        return f"Item(name='{self.name}', price={self.price}, barcode='{self.barcode}')"

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

if __name__ == "__main__":
    # Ensure the database is created within the app context
    with app.app_context():
        db.create_all()

        # Add sample items to the database if empty
        if not Item.query.first():
            sample_items = [
                Item(name="Phone", price=500, barcode="5634723456", description="A smartphone with excellent features."),
                Item(name="Laptop", price=768, barcode="3425347893", description="A high-performance laptop for work and gaming."),
                Item(name="Keyboard", price=167, barcode="45637846578", description="A mechanical keyboard with RGB lighting.")
            ]
            db.session.bulk_save_objects(sample_items)
            db.session.commit()

    # Run the app
    app.run(debug=True)
