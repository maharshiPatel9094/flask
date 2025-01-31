from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField

# creating the forms firlds
class RegisterForm(FlaskForm):
    username = StringField(label='User Name: ')
    email = StringField(label='Email Address: ')
    password1 = PasswordField(label='Password: ')
    password2 = PasswordField(label='Confirm Password: ')
    submit = SubmitField(label='Create Account')
