import unittest
from app import db, create_app
from app.models.crypt_db import Crypt


class TestCryptoDB(unittest.TestCase):

    def setUp(self):
        print("setUp test env")

        # init test env
        self.app = create_app()
        db.create_all()

        self.crypto = Crypt()

        # init crypto data
        crypto = Crypt(crypt_id=1, crypt_name="BTC")
        db.session.add(crypto)
        db.session.commit()

    def tearDown(self):
        print("tearDown")
        db.session.remove()
        db.drop_all()

    def test_fetch_curency_data_by_name(self):
        res = self.crypto.find_currency_name(crypt_name="BTC")
        self.assertIsNotNone(res)

        res = self.crypto.find_currency_name(crypt_name="ETH")
        self.assertIsNone(res)


if __name__ == "__main__":
    unittest.main()
