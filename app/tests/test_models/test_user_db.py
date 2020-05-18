import unittest
from app.models.user_db import User


class TestUserDB(unittest.TestCase):

    def test_find_email_and_name(self):
        exist_data = User.find_user_email_and_name(
            name="aaa", email="test@gmail.com")
        non_exist_name = User.find_user_email_and_name(
            name="testtest", email="test@gmail.com")
        non_exist_mail = User.find_user_email_and_name(
            name="aaa", email="testtesttest@gmail.com")

        assert exist_data == True
        assert non_exist_name == "User name"
        assert non_exist_mail == "mail address"

    def test_find_user_info(self):
        user = User.find_user_info(name="test3", "test@gmail.com", "Abcdef1@")
        non_exist_user = User.find_user_info(name="testaaaaaa", "test@gmail.com", "Abcdef1@")

        assert user == 3
        assert non_exist_user == False

    def test_update(self):
        user = User.update_user_info(user_id=1)

        self.assertIsNotNone(user)

    def test_delete_user(self):
        correct_user = User.delete_user_info(
            user_id=1, name="aaa", mail="test@gmail.com", password="Abcdef1@")
        incorrect_user = User.delete_user_info(
            user_id=1, name="121212", mail="test@gmail.com", password="Abcdef1@")
        self.assertIsNotNone(correct_user)
        assert incorrect_user == False
