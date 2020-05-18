import unittest
from app.utils.crypt_validation import CryptValidation


class TestCryptValidator(unittest.TestCase):

    def test_validator(self):
        crypt_validator = CryptValidation()
        non_exist_currency = crypt_validator.validate(
            user_id=1, crypt_name="ADA")
        _, crypt = crypt_validator.validate(user_id=1, crypt_name="BTC")
        assert non_exist_currency == False
        assert crypt == "BTC"

    def test_validation_portfolio(self):
        crypt_validator = CryptValidation()

        exist_data = crypt_validator.validate_portfolio_data(user_id=1)
        non_exist_currency = crypt_validator.validate_portfolio_data(user_id=2)
        assert assertIsNotNone(exist_data)
        assert assertIsNone(non_exist_currency)

