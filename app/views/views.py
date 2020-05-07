from flask import Flask, Blueprint, render_template, request, redirect, flash, url_for, session
from app.forms.signup.forms import SignupForm
from app.forms.login.forms import Login
from app.forms.update.forms import Update
from app.utils.execute_user_db import UserService
from app.utils.user_create_validation import UserCreateValidator

user_page = Blueprint("user_page", __name__,
                      template_folder="templates")


@user_page.route("/signup", methods=["GET", "POST"])
def signup():
    signup_form = SignupForm()

    if request.method == "POST" and signup_form.validate_on_submit():
        # duplicete check user_name and user_mail
        user_service = UserService()
        error = user_service.register(request.form)
        if error == True:
            return redirect(url_for("user_page.login"))
        # alredy exist same user name ot email
        flash(f"{error} is already existing")
    return render_template("user/signup.html", title="Sign Up", form=signup_form)


@user_page.route("/login", methods=["GET", "POST"])
def login():
    login_form = Login()

    if request.method == "POST" and login_form.validate_on_submit():
        # check if user already created a account
        user_service = UserService()
        error = user_service.login(request.form)
        if error:
            # user name pass 別check 必要
            session["user_id"] = error
            session["login"] = True
            print(session["user_id"])
            print(session["login"])
            flash("Welcome back")
            return redirect(url_for("user_page.login"))

        # alredy exist same user name ot email
        flash("User information is not existing Try again or please signup in signup page")

    return render_template("user/login.html", title="Login", form=login_form)


@user_page.route("/update", methods=["GET", "POST"])
def update():
    update_form = Update()
    if request.method == "POST" and update_form.validate_on_submit():
        # updateされない
        user_service = UserService()
        error = user_service.update(request.form)
        if error:
            flash("Update was Success")
            return redirect(url_for("user_page.update"))
        flash("Can't update")
    return render_template("user/update.html", title="Update", form=update_form)
