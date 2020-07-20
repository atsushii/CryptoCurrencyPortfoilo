import unittest
from app.utils.crypt_validation import CryptValidation
from app import db, create_app
from app.models.user_db import User
from app.models.crypt_db import Crypt
from app.models.user_crypt_db import UserCrypt


class TestCryptoValidator(unittest.TestCase):

    def setUp(self):
        print("setUp test env")

        # init test env
        self.app = create_app()
        db.create_all()

        # init user data
        self.user = User(user_name="atushi",
                         user_mail="test@gmail.com", user_password="Amjsbs@1")

        user2 = User(user_name="John",
                     user_mail="test2@gmail.com", user_password="Amjsbs@1")
        # init currency data
        ctypt = Crypt(crypt_id=1, crypt_name="BTC")
        ctypt2 = Crypt(crypt_id=2, crypt_name="ETH")

        # init user crypto data
        user_crypto = UserCrypt(user_id=1, crypt_id=1, num_of_currency=2)
        user_crypto2 = UserCrypt(user_id=1, crypt_id=2, num_of_currency=2)

        self.crypto_validator = CryptValidation()

        db.session.add(self.user)
        db.session.commit()
        db.session.add(user2)
        db.session.commit()

        db.session.add(ctypt)
        db.session.commit()
        db.session.add(ctypt2)
        db.session.commit()

        db.session.add(user_crypto)
        db.session.commit()

        db.session.add(user_crypto2)
        db.session.commit()

    def tearDown(self):
        print("tearDown")
        db.session.remove()
        db.drop_all()

    def test_validator(self):

        user, crypto = self.crypto_validator.validate(
            user_id=1, crypt_name="BTC")

        self.assertEqual(user, self.user)
        self.assertEqual(crypto.crypt_name, "BTC")

        # invalid crypto data
        res = self.crypto_validator.validate(
            user_id=1, crypt_name="ADA")

        self.assertFalse(res)

    def test_validation_portfolio_data(self):

        # user doesn't register crypto data
        res = self.crypto_validator.validate_portfolio_data(user_id=2)

        self.assertFalse(res)

        # user has crypto data
        res = self.crypto_validator.validate_portfolio_data(user_id=1)
        self.assertEqual(res[0], ["BTC", "ETH"])


if __name__ == "__main__":
    unittest.main()
