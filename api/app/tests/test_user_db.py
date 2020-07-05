import unittest
from app import db, create_test_app
from app.models.user_db import User


class TestUserDB(unittest.TestCase):

    def setUp(self):
        print("setUp test env")

        # init test env
        self.app = create_test_app()
        db.create_all()

        self.user = User()

        # init user data
        self.test_user = User(user_id=1, user_name="test",
                              user_mail="test@gmail.com", user_password="Amksjfs@124")
        db.session.add(self.test_user)
        db.session.commit()

    def tearDown(self):
        print("tearDown")
        db.session.remove()
        db.drop_all()

    def test_filter_register_user_email_and_name(self):
        # Valid data
        res = self.user.find_user_email_and_name(
            name="test", email="test@gmail.com")

        self.assertFalse(res)

        # exist name in db
        res = self.user.find_user_email_and_name(
            name="noexist", email="test@gmail.com")

        self.assertFalse(res)

        # exist email in db
        res = self.user.find_user_email_and_name(
            name="test", email="aaa@gmail.com")

        self.assertFalse(res)

        # non exist user name and email in db
        res = self.user.find_user_email_and_name(
            name="noexist", email="noexist@gmail.com")

        self.assertTrue(res)

    def test_find_login_user_data(self):

        # user put correct user info
        user = self.user.find_user_info(
            name="test", mail="test@gmail.com", password="Amksjfs@124")

        self.assertEqual(user, self.test_user)

        # user put wrong name
        res = self.user.find_user_info(
            name="aaaa", mail="test@gmail.com", password="Amksjfs@124")

        self.assertFalse(res)

        # user put wrong email
        res = self.user.find_user_info(
            name="test", mail="aaa@gmail.com", password="Amksjfs@124")

        self.assertFalse(res)

        # user put wrong password
        res = self.user.find_user_info(
            name="test", mail="test@gmail.com", password="wrong@123")

        self.assertFalse(res)

    def test_find_user_by_id(self):
        user = self.user.update_user_info(user_id=1)

        self.assertEqual(user, self.test_user)

        user = self.user.delete_user_info(user_id=1)
        self.assertEqual(user, self.test_user)

    def test_get_user_by_email(self):

        user = self.user.get_useid_by_email(email="test@gmail.com")
        self.assertEqual(user, self.test_user)

        # non exist email in db
        res = self.user.get_useid_by_email(email="abcde@gmail.com")
        self.assertFalse(res)


if __name__ == "__main__":
    unittest.main()
