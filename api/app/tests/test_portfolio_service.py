import unittest
from app.utils.crypt_validation import CryptValidation
from app import db, create_test_app
from app.models.user_db import User
from app.models.crypt_db import Crypt
from app.models.user_crypt_db import UserCrypt


class TestPortfolioService(unittest.TestCase):

    def setUp(self):
        print("setUp test env")
        # init test env
        self.app = create_test_app()
        db.create_all()
        self.crypt_validator = CryptValidation()
        # init user data
        user = User(user_name="atushi",
                    user_mail="test@gmail.com", user_password="Amjsbs@1")
        # init currency data
        ctypt = Crypt(ctypt_id=1, crypt_name="BTC")

        db.session.add(user)
        db.session.commit()

        db.session.add(ctypt)
        db.session.commit()

    def tearDown(self):
        print("tearDown")
        db.session.remove()
        db.drop_all()
