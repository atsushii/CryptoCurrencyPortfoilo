from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Email, InputRequired, EqualTo
from wtforms.fields.html5 import EmailField
import re


def validate_username(self, username):
    """
    must be less tha 10 characters
    """

    if len(username.data) > 10:
        raise ValueError("Name must be less than 10 characters")


def validate_password(self, password):
    """
    Password
        - more than 8 less than 32 characters
        - have a upcase letter
        - have a special character
        - have a number
    """

    if len(password.data) < 8:
        raise ValueError("must be more than 8 characters")
    elif len(password.data) > 32:
        raise ValueError("must be less than 32 characters")
    elif re.search('[0-9]', password.data) is None:
        raise ValueError("Password must have a number")
    elif re.search('[A-Z]', password.data) is None:
        raise ValueError("Password must have a upcase letter")
    elif re.search('[@_!#$%^&*()<>?/\|}{~:]', password.data) is None:
        raise ValueError("Password must have a special character")


class SignupForm(FlaskForm):
    username = StringField("Username", validators=[
        InputRequired("Please enter your name."), validate_username])
    email = EmailField("Email", validators=[InputRequired(
        "Please enter your email adress."), Email("Require a valid email address")])

    password = PasswordField("Password", validators=[InputRequired(
        "Please enter your password"), EqualTo("confirm", message="password must match"), validate_password])
    confirm = PasswordField("Repeat Password")
    submit = SubmitField("Sign In")
