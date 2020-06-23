from flask import Flask, Blueprint, render_template, request, redirect, flash, url_for, session, jsonify
from app.forms.signup.forms import SignupForm
from app.forms.login.forms import Login
from app.forms.update.forms import Update
from app.forms.delete.forms import Delete
from app.utils.execute_user_db import UserService
from app.utils.execute_crypt_db import PortfolioService
from app.utils.execute_api import API
import json

user_page = Blueprint("user_page", __name__,
                      template_folder="templates")


@user_page.route("/signup", methods=["POST"])
def signup():
    # duplicete check user_name and user_mail
    user_service = UserService()
    error = user_service.register(json.loads(request.data))
    if error == True:
        return request.data
    # alredy exist same user name or email
    return ""


@user_page.route("/login", methods=["POST"])
def login():
    # check if user already created a account
    user_service = UserService()
    user = user_service.login(json.loads(request.data))
    if user:
        session["user_id"] = user.user_id
        session["login"] = True
        # return user data
        print(session)
        return jsonify(id=user.user_id, username=user.user_name, mail=user.user_mail, password=user.user_password)
    # doesn't match post data with user info in db
    return ""


@user_page.route("/update", methods=["GET", "POST"])
def update():
    if "login" not in session or session["login"] == False:
        return redirect(url_for("user_page.login"))

    update_form = Update()
    if request.method == "POST" and update_form.validate_on_submit():
        user_service = UserService()
        error = user_service.update(request.form, session["user_id"])
        if error:
            flash("Update was Success")
            return redirect(url_for("user_page.account_page"))
        flash(error)
    return render_template("user/update.html", title="Update", form=update_form)


@user_page.route("/delete/<id>", methods=["DELETE"])
def delete(id):
    if "login" not in session or session["login"] == False:
        return ""

    user_service = UserService()
    error = user_service.delete(id)
    if error == True:
        session.pop("user_id", None)
        session["login"] = None
        return ""
    return False


@user_page.route("/fetch/<id>", methods=["GET"])
def fetch(id):
    print("fetch", session)
    if "login" not in session or session["login"] == False:
        return ""

    user_service = UserService()
    user = user_service.get_user_info_by_user_id(id)

    return jsonify(id=user.user_id, username=user.user_name, mail=user.user_mail, password=user.user_password)


@user_page.route("/refetch", methods=["GET"])
def refetch():
    if "login" not in session or session["login"] == False:
        return ""

    user_service = UserService()
    user = user_service.get_user_info_by_user_id(session["user_id"])
    print("refetch", user)
    return jsonify(id=user.user_id, username=user.user_name, mail=user.user_mail, password=user.user_password)


@user_page.route("/logout", methods=["GET", "POST"])
def logout():

    flash("logout! see you soon!")
    session.pop("user_id")
    session["login"] = False
    return redirect(url_for("user_page.login"))


@user_page.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():
    return render_template("user/forgot_password.html")


@user_page.route("/account_page", methods=["GET"])
def account_page():
    if "login" not in session or session["login"] == False:

        return redirect(url_for("user_page.login"))

    if request.method == "GET":
        user_service = UserService()
        user = user_service.get_user_info_by_user_id(session["user_id"])
        if user:
            return render_template("user/account_page.html", title="My Information", user=user)
    return redirect(url_for("user_page.signup"))


@user_page.route("/portfolio", methods=["GET"])
def user_portfolio():
    if "login" not in session or session["login"] == False:

        return redirect(url_for("user_page.login"))

    if request.method == "GET":
        portfolio_service = PortfolioService()
        data = portfolio_service.get_user_portfolio(session["user_id"])
        user_service = UserService()
        user = user_service.get_user_info_by_user_id(session["user_id"])

        if data and user:
            api = API()
            "data[0]: currency name, data[1]: number of hold currency"
            result = api.call_api(data[0])
            result, total_value = api.data_process(result, data[1])
            return render_template("portfolio/user_portfolio.html", title="Portfolio", result=result, num_of_holds=data[1], total_value=total_value, user=user)

    return render_template("portfolio/user_portfolio.html", title="Portfolio", result="", num_of_holds="", total_value=0, user=user)


@user_page.route("/register_currency", methods=["POST", "GET"])
def register_currency():
    print("login" not in session)
    print(session)
    if "login" not in session or session["login"] == False:

        return redirect(url_for("user_page.login"))

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
    if "login" not in session or session["login"] == False:

        return redirect(url_for("user_page.login"))

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
    if "login" not in session or session["login"] == False:

        return redirect(url_for("user_page.login"))

    if request.method == "POST":
        portfolio_service = PortfolioService()
        result = portfolio_service.delete_currency_data(
            session["user_id"], request.form["coin_name"].upper())
        if result:
            flash("Deleted!")
            return redirect(url_for("user_page.user_portfolio"))
        flash("Failer Try Again!")
    return render_template("portfolio/delete_currency.html", title="Delete", currency_name=currency_name)
