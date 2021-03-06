from app import db, mail
from app.models.user_db import User
from app.utils.user_create_validation import UserCreateValidator
from sqlalchemy.exc import SQLAlchemyError
from flask_mail import Message
import re


class UserService():

    def register(self, form_data):
        """
        Insert user data to User table
        """
        validator = UserCreateValidator()

        error = validator.validate(form_data)
        if not error:
            return error

        error = validator.user_form_validation(form_data)
        if not error:
            return error

        try:
            user = User(user_name=form_data["username"],
                        user_mail=form_data["email"], user_password=form_data["password"])
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            return False

        return True

    def login(self, form_data):
        """
        Login if user was already registered
        """

        validator = UserCreateValidator()

        error = validator.user_form_validation(form_data)
        if not error:
            return error

        # check user is already existing in db
        return User.find_user_info(form_data["username"],
                                   form_data["email"],
                                   form_data["password"])

    def update(self, form_data, user_id):
        """
        Update user data
        """
        user = User.update_user_info(user_id)

        if not user:
            return False

        validator = UserCreateValidator()

        error = validator.validate(form_data)
        if not error:
            return error

        error = validator.user_form_validation(form_data)
        if not error:
            return error

        try:
            user.user_name = form_data["username"]
            user.user_mail = form_data["email"]
            user.user_password = form_data["password"]
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            return False

        return True

    def delete(self, user_id):
        """
        Delete user data
        """
        user = User.delete_user_info(user_id)
        user_portfolio = user.crypts

        try:
            user_portfolio.clear()
            db.session.add(user)
            db.session.commit()
            db.session.delete(user)
            db.session.commit()

        except SQLAlchemyError:
            db.session.rollback()
            return False

        return True

    def get_user_info_by_user_id(self, user_id):
        """
        Get user information for showing info in user desplay
        """
        user = User.update_user_info(user_id)

        return user

    def reset_password_by_token(self, token):
        return User.vertify_reset_token(token)

    def get_user_info_by_email(self, email):
        """
        Get user information by eamil for reset password
        """
        user = User.get_useid_by_email(email)

        if not user:
            return False
        return user

    def send_reset_mail(self, user):
        token = User.get_reset_token(user.user_id)

        msg = Message("Password Reset Request",
                      sender="noreply@crypt.com", recipients=[user.user_mail])

        msg.body = f'''To reset your password, type the below temp password on Reset password page:
        {"http://localhost:3000/form/resetPassword/" + token}

        If you didn't make this request simply ignore this mail and no change password
        '''

        mail.send(msg)
        print("complete sending email")

    def register_new_password(self, user, form_data):
        """
        Insert user data to User table
        """
        # password
        if len(form_data["password"]) < 8:
            return False
        elif not re.search("[0-9]", form_data["password"]):
            return False
        elif not re.search("[A-Z]", form_data["password"]):
            return False
        elif not re.search("[@_!#$%^&*()<>?/\|}{~:]", form_data["password"]):
            return False
        elif form_data["password"] != form_data["confirmPassword"]:
            return False

        try:
            user.user_password = form_data["password"]
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            return False

        return True
