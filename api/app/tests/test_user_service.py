import unittest
from app.utils.execute_user_db import UserService
from app import db, create_app
from app.models.user_db import User


class TestUserService(unittest.TestCase):

    def setUp(self):
        print("setUp test env")
        # init test env
        self.app = create_app()
        db.create_all()
        self.user_service = UserService()

        # init user data
        self.user = User(user_name="Akon",
                         user_mail="exist@gmail.com", user_password="Amjsbs@1")
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        print("tearDown")
        db.session.remove()
        db.drop_all()

    def test_user_register(self):

        # exist data
        form_data = {"username": "Akon",
                     "email": "exist@gmail.com",
                     }
        res = self.user_service.register(form_data)

        self.assertFalse(res)

        # non exist data
        form_data = {"username": "herry",
                     "email": "new@gmail.com",
                     "password": "Am@sjsj123",
                     "confirmPassword": "Am@sjsj123"}

        res = self.user_service.register(form_data)

        self.assertTrue(res)

        # invalid username
        form_data = {"username": "herryaaaal",
                     "email": "exist@gmail.com",
                     "password": "Am@sjsj123",
                     "confirmPassword": "Am@sjsj123"}

        res = self.user_service.register(form_data)

        self.assertFalse(res)

    def test_user_login(self):
        # inValid form data
        form_data = {"username": "herrykjscsd",
                     "email": "new@gmail.com",
                     "password": "Am@sjsj123",
                     "confirmPassword": "Am@sjsj123"}

        res = self.user_service.login(form_data)

        self.assertFalse(res)

        # non exist user
        form_data = {"username": "herr",
                     "email": "new@gmail.com",
                     "password": "Am@sjsj123",
                     "confirmPassword": "Am@sjsj123"}

        res = self.user_service.login(form_data)

        self.assertFalse(res)

        # exist data
        form_data = {"username": "Akon",
                     "email": "exist@gmail.com",
                     "password": "Amjsbs@1",
                     "confirmPassword": "Amjsbs@1"}

        res = self.user_service.login(form_data)

        self.assertIsNotNone(res)

    def test_user_edit(self):

        # non exist user
        form_data = {"username": "nonexist",
                     "email": "exist@gmail.com",
                     "password": "Amjsbs@1",
                     "confirmPassword": "Amjsbs@1"}

        res = self.user_service.update(form_data=form_data, user_id=1)

        self.assertFalse(res)

        # edit user by exist user id
        form_data = {"username": "new",
                     "email": "new@gmail.com",
                     "password": "Amjsbs@1",
                     "confirmPassword": "Amjsbs@1"}

        res = self.user_service.update(form_data=form_data, user_id=1)

        self.assertTrue(res)

    def test_user_delete(self):

        res = self.user_service.delete(user_id=1)

        self.assertTrue(res)

    def test_find_user_by_id(self):

        res = self.user_service.get_user_info_by_user_id(user_id=1)

        self.assertEqual(self.user, res)

    def test_find_user_by_email(self):

        # Exist user
        res = self.user_service.get_user_info_by_email(
            email=self.user.user_mail)

        self.assertEqual(res, self.user)

        # non exist user
        res = self.user_service.get_user_info_by_email(
            email="nonexist@gmail.com")

        self.assertFalse(res)

    def test_register_new_password(self):

        # Valid new password
        form_data = {
            "password": "Amjsbs@1",
            "confirmPassword": "Amjsbs@1"}

        res = self.user_service.register_new_password(
            user=self.user, form_data=form_data)

        self.assertTrue(res)

        # inValid new password
        form_data = {
            "password": "mjsbs@1",
            "confirmPassword": "mjsbs@1"}

        res = self.user_service.register_new_password(
            user=self.user, form_data=form_data)

        self.assertFalse(res)


if __name__ == "__main__":
    unittest.main()
