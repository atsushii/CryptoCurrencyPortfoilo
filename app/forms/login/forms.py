from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Email, InputRequired
from wtforms.fields.html5 import EmailField


class Login(FlaskForm):
    username = StringField("Username", validators=[
        InputRequired("Please enter your name.")])
    email = EmailField("email", validators=[InputRequired(
        "Please enter your email adress."), Email("Require a valid email address")])

    password = PasswordField("Password", validators=[InputRequired(
        "Please enter your password")])
    confirm = PasswordField("Repeat Password")

    remember_me = BooleanField("Remember me")
    submit = SubmitField("Login")
