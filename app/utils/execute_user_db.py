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
