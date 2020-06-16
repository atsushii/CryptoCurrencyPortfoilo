from app.models.user_db import User


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
