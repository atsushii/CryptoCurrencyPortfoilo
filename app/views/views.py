from flask import Flask, Blueprint, render_template, request, redirect, flash, url_for
from app.forms.signup.forms import SignupForm
from app.forms.login.forms import Login
from app.utils.execute_user_db import UserService
from app.utils.user_create_validation import UserCreateValidator

signup_page = Blueprint("signup_page", __name__,
                        template_folder="templates")


@signup_page.route("/signup", methods=["GET", "POST"])
def signup():
    signup_form = SignupForm()

    if request.method == "POST" and signup_form.validate_on_submit():
        # duplicete check user_name and user_mail
        user_service = UserService()
        error = user_service.register(request.form)
        if error == True:
            return redirect(url_for("signup_page.login"))
        # alredy exist same user name ot email
        flash(f"{error} is already existing")
    return render_template("user/signup.html", title="Sign Up", form=signup_form)


@signup_page.route("/login", methods=["GET", "POST"])
def login():
    login_form = Login()

    if request.method == "POST" and login_form.validate_on_submit():
        # check if user already created a account
        user_service = UserService()
        error = user_service.login(request.form)
        if error:
            return redirect(url_for("signup_page.signup"))

        # alredy exist same user name ot email
        flash("User information is not existing Try again or please signup in signup page")

    return render_template("user/login.html", title="Login", form=login_form)
