from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flask app setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Suppress warning
app.config['SECRET_KEY'] = '60eae47fb49343464a73e3da' #for form
db = SQLAlchemy(app)  # Database instance

from market import routes