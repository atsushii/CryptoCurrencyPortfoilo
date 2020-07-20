import unittest
from app.utils.user_create_validation import UserCreateValidator
from app import db, create_app
from app.models.user_db import User


class TestUserValidate(unittest.TestCase):

    def setUp(self):
        print("setUp test env")
        # init test env
        self.app = create_app()
        db.create_all()
        self.user_create_validator = UserCreateValidator()
        # init user data
        user = User(user_name="atushi",
                    user_mail="test@gmail.com", user_password="Amjsbs@1")
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        print("tearDown")
        db.session.remove()
        db.drop_all()

    def test_exist_user_validate(self):
        form_data = {"username": "atushi",
                     "email": "test@gmail.com"}

        res = self.user_create_validator.validate(form_data)

        self.assertFalse(res)

    def test_non_exist_user_validate(self):
        form_data = {"username": "Akon",
                     "email": "exist@gmail.com"}

        res = self.user_create_validator.validate(form_data)

        self.assertTrue(res)

    def test_user_form_validate_by_valid_data(self):

        form_data = {"username": "Akon",
                     "email": "exist@gmail.com",
                     "password": "Smdfkn@1234",
                     "confirmPassword": "Smdfkn@1234"}

        res = self.user_create_validator.user_form_validation(form_data)

        self.assertTrue(res)

    def test_user_form_validate_by_invalid_data(self):

        # invalid username
        form_data = {"username": "Akondxcsdjk",
                     "email": "exist@gmail.com",
                     "password": "Smdfkn@1234",
                     "confirmPassword": "Smdfkn@1234"}

        res = self.user_create_validator.user_form_validation(form_data)

        self.assertFalse(res)

        # invalid email
        form_data = {"username": "Akon",
                     "email": "invalidgail.com",
                     "password": "Smdfkn@1234",
                     "confirmPassword": "Smdfkn@1234"}

        res = self.user_create_validator.user_form_validation(form_data)

        self.assertFalse(res)

        # invalid password not contain number
        form_data = {"username": "Akondxcs",
                     "email": "exist@gmail.com",
                     "password": "Smdfkn@",
                     "confirmPassword": "Smdfkn@"}

        res = self.user_create_validator.user_form_validation(form_data)

        self.assertFalse(res)

        # invalid password not contain capital letter
        form_data = {"username": "Akondxcs",
                     "email": "exist@gmail.com",
                     "password": "mdfkn@1234",
                     "confirmPassword": "mdfkn@1234"}

        res = self.user_create_validator.user_form_validation(form_data)

        self.assertFalse(res)

        # invalid password not contain special character
        form_data = {"username": "Akondxcs",
                     "email": "exist@gmail.com",
                     "password": "mdfkn1234",
                     "confirmPassword": "mdfkn1234"}

        res = self.user_create_validator.user_form_validation(form_data)

        self.assertFalse(res)

        # invalid password not match password and confirm password
        form_data = {"username": "Akondxcs",
                     "email": "exist@gmail.com",
                     "password": "mdfkn@1234",
                     "confirmPassword": "mdfk@1234"}

        res = self.user_create_validator.user_form_validation(form_data)

        self.assertFalse(res)


if __name__ == "__main__":
    unittest.main()
