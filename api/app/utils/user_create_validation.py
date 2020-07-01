from app.models.user_db import User
import re


class UserCreateValidator():
    """
    Validate input data
    """

    def validate(self, form_data):
        """
        Check duplicate data in User table
        """
        exist_user = User.find_user_email_and_name(
            form_data["username"], form_data["email"])

        return exist_user

    def user_form_validation(self, form_data):
        """
        Validate form data
        """

        # username
        if len(form_data["username"]) > 10:
            return False

        # mail
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not re.search(regex, form_data["email"]):
            return False

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

        return True
