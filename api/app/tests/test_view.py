import unittest
from app import db, create_test_app
from app.models.user_db import User
from app.models.crypt_db import Crypt
from app.models.user_crypt_db import UserCrypt
from app.views import views
from flask import jsonify
import json


class TestApis(unittest.TestCase):

    def setUp(self):
        print("setUp test env")

        # init test env
        app = create_test_app()
        self.client = app.test_client()

        # init session
        with self.client.session_transaction() as session:
            session['user_id'] = 1
            session['login'] = True

        db.create_all()

        # init user data
        self.user = User(user_name="atushi",
                         user_mail="test@gmail.com", user_password="Amjsbs@1")

        # init currency data
        ctypt = Crypt(crypt_id=1, crypt_name="BTC")
        ctypt2 = Crypt(crypt_id=2, crypt_name="ETH")

        # init user crypto data
        user_crypto = UserCrypt(user_id=1, crypt_id=1, num_of_currency=2)

        # init user data
        self.exist_user = {"username": "atushi", "email": "test@gmail.com",
                           "password": "Amjsbs@1", "confirmPassword": "Amjsbs@1"}
        self.non_exist_user = {"username": "user", "email": "asda@gmail.com",
                               "password": "Am@test124", "confirmPassword": "Am@test124"}

        db.session.add(self.user)
        db.session.commit()

        db.session.add(ctypt)
        db.session.commit()
        db.session.add(ctypt2)
        db.session.commit()

        db.session.add(user_crypto)
        db.session.commit()

    def tearDown(self):
        print("tearDown")
        db.session.remove()
        db.drop_all()

    def test_signup(self):

        res = self.client.post("/signup", json=self.non_exist_user)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(json.loads(res.data)["ok"])

        res = self.client.post("/signup", json=self.exist_user)

        self.assertEqual(res.data, b"")

    def test_login(self):

        res = self.client.post("/login", json=self.exist_user)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(json.loads(res.data)), 4)

        res = self.client.post("/login", json=self.non_exist_user)

        self.assertEqual(res.data, b"")

    def test_edit(self):

        edit_user = {"username": "editUser", "email": "edit@gmail.com",
                     "password": "Edit@test124", "confirmPassword": "Edit@test124"}

        res = self.client.patch("/edit/1", json=edit_user)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.loads(res.data), edit_user)

    def test_delete(self):

        res = self.client.delete("/delete/1")

        self.assertEqual(res.status_code, 200)
        self.assertTrue(json.loads(res.data)["ok"])

    def test_fetch_user(self):

        res = self.client.get("/fetch")

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(json.loads(res.data)), 4)

    def test_refetch_user(self):

        res = self.client.get("/refetch")

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(json.loads(res.data)), 4)

    def test_logout(self):

        res = self.client.post("/logout/1")

        self.assertEqual(res.status_code, 200)
        self.assertTrue(json.loads(res.data)["ok"])

    def test_send_reset_password(self):

        invalid_email = {"email": "aaaa@gmail.com"}

        res = self.client.post("/forgot_password", json=invalid_email)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, b"")

        valid_email = {"email": "test@gmail.com"}

        res = self.client.post("/forgot_password", json=valid_email)

        self.assertTrue(json.loads(res.data)["ok"])

    def test_fetch_currency(self):

        res = self.client.get("/fetch_currency")

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(json.loads(res.data)), 4)

    def test_register_currency(self):

        test_currency_data = {"symbol": "ETH", "num_hold": 1}
        res = self.client.post("/register_currency/1", json=test_currency_data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(json.loads(res.data)["ok"])

    def test_edit_currency(self):

        test_currency_data = {"symbol": "BTC", "num_hold": 10}
        res = self.client.patch("/edit_currency/1", json=test_currency_data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(json.loads(res.data)), 2)

    def test_delete_currency(self):

        # valid currency
        res = self.client.delete("/delete_currency/1/BTC")

        self.assertEqual(res.status_code, 200)
        self.assertTrue(json.loads(res.data)["ok"])

        # invalid currency
        res = self.client.delete("/delete_currency/1/ETH")

        self.assertEqual(res.data, b"")


if __name__ == "__main__":
    unittest.main()
