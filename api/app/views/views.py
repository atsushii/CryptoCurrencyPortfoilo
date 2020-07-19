from flask import Flask, Blueprint, request, session, jsonify
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
    if error:
        return jsonify(ok=True)
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
        return jsonify(id=user.user_id, username=user.user_name, mail=user.user_mail, password=user.user_password)
    # doesn't match post data with user info in db
    return ""


@user_page.route("/edit/<id>", methods=["PATCH"])
def edit(id):

    if session.get("user_id") != int(id):
        return ""

    user_service = UserService()
    response = user_service.update(json.loads(request.data), id)
    if response:
        return request.data

    return ""


@user_page.route("/delete/<id>", methods=["DELETE"])
def delete(id):

    if session.get("user_id") != int(id):
        return ""

    user_service = UserService()
    error = user_service.delete(id)
    if error:
        session.pop("user_id", None)
        session.pop("login", None)
        return jsonify(ok=True)
    return ""


@user_page.route("/fetch", methods=["GET"])
def fetch():

    if not is_login():
        return ""

    user_service = UserService()
    user = user_service.get_user_info_by_user_id(session["user_id"])

    return jsonify(id=user.user_id, username=user.user_name, email=user.user_mail, password=user.user_password)


@user_page.route("/refetch", methods=["GET"])
def refetch():

    if not is_login():
        return ""

    user_service = UserService()
    user = user_service.get_user_info_by_user_id(session["user_id"])

    return jsonify(id=user.user_id, username=user.user_name, email=user.user_mail, password=user.user_password)


@user_page.route("/logout/<id>", methods=["POST"])
def logout(id):

    if session.get("user_id") != int(id):
        return ""

    session.pop("user_id")
    session["login"] = False

    return jsonify(ok=True)


@user_page.route("/forgot_password", methods=["POST"])
def forgot_password():

    if not is_login():

        return ""

    response = json.loads(request.data)
    user_service = UserService()

    user = user_service.get_user_info_by_email(response["email"])

    if not user:
        return ""

    user_service.send_reset_mail(user)

    return jsonify(ok=True)


@user_page.route("/is_valid_token/<token>", methods=["POST"])
def is_valid_token(token):
    user_service = UserService()

    user = user_service.reset_password_by_token(token)
    if user is None:
        return ""

    return jsonify(ok=True)


@user_page.route("/reset_password/<token>", methods=["POST"])
def reset_password(token):
    form_data = json.loads(request.data)
    user_service = UserService()

    user = user_service.reset_password_by_token(token)
    if user is None:
        return ""

    result = user_service.register_new_password(user, form_data)
    if result:
        return jsonify(ok=True)
    return ""


@user_page.route("/fetch_currency", methods=["GET"])
def fetch_currency():

    if not is_login():

        return ""

    portfolio_service = PortfolioService()
    data = portfolio_service.get_user_portfolio(session["user_id"])
    if data:
        api = API()
        "data[0]: currency name, data[1]: number of hold currency"
        result = api.call_api(data[0])
        currency_list, total_value = api.data_process(result, data[1])
        return jsonify(id=session["user_id"], currency_list=currency_list, total_value=total_value)

    return jsonify(id=session["user_id"], currency_list="", total_value=0)


@user_page.route("/register_currency/<id>", methods=["POST"])
def register_currency(id):

    if not is_login():

        return ""

    request_data = json.loads(request.data)

    portfolio_service = PortfolioService()
    error = portfolio_service.register(
        id, request_data["symbol"].upper(), request_data["num_hold"])
    if error:
        return jsonify(ok=True)

    return ""


@user_page.route("/edit_currency/<id>", methods=["PATCH"])
def edit_currency(id):

    if not is_login():

        return ""

    edit_data = json.loads(request.data)
    portfolio_service = PortfolioService()
    result = portfolio_service.update_currency_data(
        id, edit_data["symbol"].upper(), edit_data["num_hold"])
    if result:

        return jsonify(json.loads(request.data))

    return ""


@user_page.route("/delete_currency/<id>/<currency>", methods=["DELETE"])
def delete_currency(id, currency):

    if not is_login():

        return ""

    portfolio_service = PortfolioService()
    result = portfolio_service.delete_currency_data(id, currency.upper())
    if result:
        return jsonify(ok=True)

    return ""


# Check login status
def is_login():
    return session.get("login")
