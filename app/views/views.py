from flask import Flask, Blueprint, render_template, request, redirect, flash, url_for, session
from app.forms.signup.forms import SignupForm
from app.forms.login.forms import Login
from app.forms.update.forms import Update
from app.forms.delete.forms import Delete
from app.utils.execute_user_db import UserService
from app.utils.execute_crypt_db import PortfolioService
from app.utils.execute_api import API

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
        user_service = UserService()
        error = user_service.update(request.form)
        if error:
            flash("Update was Success")
            return redirect(url_for("user_page.update"))
        flash(error)
    return render_template("user/update.html", title="Update", form=update_form)


@user_page.route("/delete", methods=["GET", "POST"])
def delete():
    delete_form = Delete()
    if request.method == "POST" and delete_form.validate_on_submit():
        user_service = UserService()
        error = user_service.delete(request.form)
        if error == True:
            flash("Thank you see you soon")
            session.pop("user_id")
            session["login"] = False
            return redirect(url_for("user_page.signup"))
        flash(error)
    return render_template("user/delete.html", title="Delete", form=delete_form)


@user_page.route("/portfolio", methods=["GET"])
def user_portfolio():
    if request.method == "GET":
        portfolio_service = PortfolioService()
        data = portfolio_service.get_user_portfolio(session["user_id"])
        if data:
            api = API()
            api.call_api(data)
            # finish until getting current currency data using api
            return render_template("portfolio/user_portfolio.html", title="Portfolio", data=data)

        return render_template("portfolio/user_portfolio.html", title="Portfolio")


@user_page.route("/add_coin", methods=["POST", "GET"])
def add_coin():

    if request.method == "POST":
        portfolio_service = PortfolioService()
        error = portfolio_service.register(
            session["user_id"], request.form["coin_name"].upper())
        if error == True:
            flash("complete")
            redirect(url_for("user_page.add_coin"))
        flash(error)
    return render_template("portfolio/add_coin.html", title="Portfolio")
