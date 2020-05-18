import unittest
from app.utils.execute_user_db import UserService


class TestUserService(unittest.TestCase):

    def test_new_user_register(self):
        user_service = UserService()

        form_data = {"user_name": "aaa",
                     "user_mail": "test_register@gmail.com", "user_password": "Abcdefg1@"}
        user = user_service.register()

        assert user == True

    def test_user_login(self):
        user_service = UserService()
        user_id = 1
        form_data = {"user_name": "aaa",
                     "user_mail": "test_register@gmail.com", "user_password": "Abcdefg1@"}
        user = user_service.login(form_data)

        form_data = {"user_name": "bbb",
                     "user_mail": "test_register@gmail.com", "user_password": "Abcdefg1@"}
        is_user = user_service.login(form_data)

        # compare with user id
        assert user == user_id
        # user info isn't exist
        assert is_user == False

    def test_user_update(self):
        user_service = UserService()
        form_data = {"new_username": "bbb",
                     "new_email": "test_register@gmail.com", "new_password": "Abcdefg1@"}
        user_id = 1
        update_user = user_service.update(form_data, user_id)

        user_id = 10
        non_exist_user = user_service.update(form_data, user_id)

        assert update_user == True
        assert non_exist_user == "Can't find user id"

    def test_user_delete(self):

        user_service = UserService()
        form_data = {"user_name": "aaa",
                     "user_mail": "test_register@gmail.com", "user_password": "Abcdefg1@"}
        user_id = 1
        user = user_service.delete(form_data, user_id)

        form_data = {"user_name": "cccc",
                     "user_mail": "test_register@gmail.com", "user_password": "Abcdefg1@"}

        is_user = user_service.delete(form_data, user_id)

        assert user == True
        assert is_user == "User information doesn't match try again"

    def test_user_find(self):
        user_service = UserService()
        user = user_service.get_user_info_by_user_id(user_id=1)
        is_user = user_service.get_user_info_by_user_id(user_id=100)

        self.assertIsNotNone(user)
        assert is_user == "Can't find user"
