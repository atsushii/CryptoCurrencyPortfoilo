from flask import Flask, Blueprint, flash, render_template, request, redirect
from app.forms.signup.forms import SignupForm
from app.forms.login.forms import Login

signup_page = Blueprint("signup_page", __name__,
                        template_folder="templates")


@signup_page.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()

    if request.method == "POST" and form.validate_on_submit():
        # add db check
        return redirect("/login")
    return render_template("user/signup.html", title="Sign Up", form=form)


@signup_page.route("/login", methods=["GET", "POST"])
def login():
    form = Login()

    if request.method == "POST" and form.validate_on_submit():
        return "login"

    return render_template("user/login.html", title="Sign Up", form=form)
