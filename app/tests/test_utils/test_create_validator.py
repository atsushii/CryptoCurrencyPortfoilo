import unittest
from app.utils.user_create_validation import UserCreateValidator


class TestUserCreateValidator(unittest.TestCase):

    def test_not_duplicate_user(self):
        form_data = {"username": "Atsushi", "email": "test@gmail.com"}

        validator = UserCreateValidator()
        user = validator.validate(form_data)

        assert user == True

    def test_duplicate_user_name(self):
        form_data = {"username": "duplicate_name",
                     "email": "test_name@gmail.com"}

        validator = UserCreateValidator()
        user = validator.validate(form_data)

        assert user == "User name"

    def test_duplicate_user_email(self):
        form_data = {"username": "masao", "email": "test@gmail.com"}

        validator = UserCreateValidator()
        user = validator.validate(form_data)

        assert user == "mail address"
