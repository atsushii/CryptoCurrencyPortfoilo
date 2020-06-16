from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Email, InputRequired, EqualTo
from wtforms.fields.html5 import EmailField
import re


def validate_new_username(self, new_username):
    """
    must be less tha 10 characters
    """

    if len(new_username.data) > 10:
        raise ValueError("Name must be less than 10 characters")


def validate_new_password(self, new_password):
    """
    PAssword
        - more than 8 less than 32 characters
        - have a upcase letter
        - have a special character
        - have a number
    """

    if len(new_password.data) < 8:
        raise ValueError("must be more than 8 characters")
    elif len(new_password.data) > 32:
        raise ValueError("must be less than 32 characters")
    elif re.search('[0-9]', new_password.data) is None:
        raise ValueError("Password must have a number")
    elif re.search('[A-Z]', new_password.data) is None:
        raise ValueError("Password must have a upcase letter")
    elif re.search('[@_!#$%^&*()<>?/\|}{~:]', new_password.data) is None:
        raise ValueError("Password must have a special character")


class Update(FlaskForm):
    # username = StringField("Username", validators=[InputRequired("Please enter your current user name.")])

    new_username = StringField("New Username", validators=[
        InputRequired("Please enter your new user name."), validate_new_username])

    # email = EmailField("Email", validators=[InputRequired("Please enter your current email address."), Email("Require a valid email address")])

    new_email = EmailField("New Email", validators=[InputRequired(
        "Please enter your new email address."), Email("Require a valid email address")])

    # password = PasswordField("Password", validators=[InputRequired("Please enter your current password")])

    new_password = PasswordField("New Password", validators=[InputRequired(
        "Please enter your new password"), EqualTo("confirm", message="password must match"), validate_new_password])

    confirm = PasswordField("Repeat Password")

    submit = SubmitField("Update")
