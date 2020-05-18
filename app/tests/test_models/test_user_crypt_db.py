import unittest
from app.models.user_crypt_db import UserCrypt


class TestCryptDB(unittest.TestCase):

    def test_find_currency(self):
        is_empty_data = Crypt.find_currency_name(crypt_name="BTC")
        empty_data = Crypt.find_currency_name(crypt_name="ADA")

        assert assertIsNone(empty_data)
        assert assertIsNotNone(is_empty_data)
