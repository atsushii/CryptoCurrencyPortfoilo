from app import db
from app.models.user_db import User
from app.utils.user_create_validation import UserCreateValidator
from sqlalchemy.exc import IntegrityError


class UserService():

    def register(self, form_data):
        """
        Insert user data to User table
        """
        validator = UserCreateValidator()

        error = validator.validate(form_data)
        if error != True:
            return error

        try:
            user = User(user_name=form_data["username"],
                        user_mail=form_data["email"], user_password=form_data["password"])
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return "db error"

        return True

    def login(self, form_data):
        """
        Login if user was already registered
        """
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
            return "Can't find user id"

        try:
            user.user_name = form_data["new_username"]
            user.user_mail = form_data["new_email"]
            user.user_password = form_data["new_password"]
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return "db error"

        return True

    def delete(self, form_data, user_id):
        """
        Delete user data
        """
        user = User.delete_user_info(user_id,
                                     form_data["username"],
                                     form_data["email"],
                                     form_data["password"])
        if not user:
            return "User information doesn't match try again"
        user_portfolio = user.crypts

        try:
            user_portfolio.clear()
            db.session.add(user)
            db.session.commit()
            db.session.delete(user)
            db.session.commit()

        except IntegrityError:
            db.session.rollback()
            return "db error"

        return True

    def get_user_info_by_user_id(self, user_id):
        """
        Get user infomation for showing info in user desplay
        """
        user = User.update_user_info(user_id)

        if not user:
            return "Can't find user"

        return user
