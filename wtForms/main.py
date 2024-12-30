from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired


# form class
class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired()]) #validators are used for validating the data field.
    password = PasswordField(label="Password", validators=[DataRequired()]) #password field makes the password hidden.
    submit = SubmitField(label="Log In")

# flask app
app = Flask(__name__)
app.secret_key = "ghfegywukahjfdsjsghfd"


# routes
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@gmail.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
        
    return render_template("login.html",form=login_form)

if __name__ == "__main__":
    app.run(debug=True)