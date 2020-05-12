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
            flash("Welcome back")
            return redirect(url_for("user_page.user_portfolio"))

        # alredy exist same user name ot email
        flash("User information is not existing Try again or please signup in signup page")

    return render_template("user/login.html", title="Login", form=login_form)


@user_page.route("/update", methods=["GET", "POST"])
def update():
    update_form = Update()
    if request.method == "POST" and update_form.validate_on_submit():
        user_service = UserService()
        error = user_service.update(request.form, session["user_id"])
        if error:
            flash("Update was Success")
            return redirect(url_for("user_page.account_page"))
        flash(error)
    return render_template("user/update.html", title="Update", form=update_form)


@user_page.route("/delete", methods=["GET", "POST"])
def delete():
    delete_form = Delete()
    if request.method == "POST" and delete_form.validate_on_submit():
        user_service = UserService()
        error = user_service.delete(request.form, session["user_id"])
        if error == True:
            flash("Thank you see you soon")
            session.pop("user_id")
            session["login"] = False
            flash("Thank you")
            return redirect(url_for("user_page.signup"))
        flash(error)
    return render_template("user/delete.html", title="Delete", form=delete_form)


@user_page.route("/logout", methods=["GET", "POST"])
def logout():
    flash("logout! see you soon")
    session.pop("user_id")
    session["login"] = False
    return redirect(url_for("user_page.login"))


@user_page.route("/account_page", methods=["GET"])
def account_page():
    if request.method == "GET":
        user_service = UserService()
        user = user_service.get_user_info_by_user_id(session["user_id"])
        if user:
            return render_template("user/account_page.html", title="My Information", user=user)
    return redirect(url_for("user_page.signup"))


@user_page.route("/portfolio", methods=["GET"])
def user_portfolio():
    if request.method == "GET":
        portfolio_service = PortfolioService()
        data = portfolio_service.get_user_portfolio(session["user_id"])
        if data:
            api = API()
            "data[0]: currency name, data[1]: number of hold currency"
            result = api.call_api(data[0])
            result, total_value = api.data_process(result, data[1])
            return render_template("portfolio/user_portfolio.html", title="Portfolio", result=result, num_of_holds=data[1], total_value=total_value)

    return render_template("portfolio/user_portfolio.html", title="Portfolio")


@user_page.route("/register_currency", methods=["POST", "GET"])
def register_currency():

    if request.method == "POST":
        portfolio_service = PortfolioService()
        error = portfolio_service.register(
            session["user_id"], request.form["coin_name"].upper(), request.form["num_of_currency"])
        if error == True:
            flash("complete")
            return redirect(url_for("user_page.user_portfolio"))
        flash(error)
    return render_template("portfolio/register_currency.html", title="Register")


@user_page.route("/update_currency/<currency_name>", methods=["POST", "GET"])
def update_currency(currency_name):

    if request.method == "POST":
        portfolio_service = PortfolioService()
        result = portfolio_service.update_currency_data(
            session["user_id"], request.form["coin_name"].upper(), request.form["num_of_currency"])
        if result:
            flash("Updated!")
            return redirect(url_for("user_page.user_portfolio"))
        flash("Failer Try Again!")
    return render_template("portfolio/update_currency.html", title="Update", currency_name=currency_name)


@user_page.route("/delete_currency/<currency_name>", methods=["POST", "GET"])
def delete_currency(currency_name):

    if request.method == "POST":
        portfolio_service = PortfolioService()
        result = portfolio_service.delete_currency_data(
            session["user_id"], request.form["coin_name"].upper())
        if result:
            flash("Deleted!")
            return redirect(url_for("user_page.user_portfolio"))
        flash("Failer Try Again!")
    return render_template("portfolio/delete_currency.html", title="Delete", currency_name=currency_name)
