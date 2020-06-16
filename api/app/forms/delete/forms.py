from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Email, InputRequired, EqualTo
from wtforms.fields.html5 import EmailField


class Delete(FlaskForm):
    username = StringField("Username", validators=[
        InputRequired("Please enter your name.")])
    email = EmailField("email", validators=[InputRequired(
        "Please enter your email adress."), Email("Require a valid email address")])

    password = PasswordField("Password", validators=[InputRequired(
        "Please enter your password"), EqualTo("confirm", message="password must match")])
    confirm = PasswordField("Repeat Password")

    submit = SubmitField("Delete")
