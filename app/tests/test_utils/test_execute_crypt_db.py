import unittest
from app.utils.execute_crypt_db import PortfolioService


class TestPortfolioService(unittest.TestCase):

    def test_new_currency_register(self):
        portfolio = PortfolioService()

        # exist currency information in db
        exist_currency = portfolio.register(
            user_id=1, crypt_name="BTC", num_of_currency=1)
        empty_currency = portfolio.register(
            user_id=1, crypt_name="ADA", num_of_currency=1)

        assert exist_currency == True
        assert empty_currency == "Cant find currency name Try again"

    def test_find_user_portfolio(self):
        portfolio = PortfolioService()

        result = portfolio.get_user_portfolio(user_id=1)

        self.assertIsNotNone(result)

    def test_update_currency_update(self):
        portfolio = PortfolioService()
        result = portfolio.update_currency_data(
            user_id=1, currency_name="BTC", num_of_hold=5)
        assert result == True

    def test_delete_currency_data(self):

        portfolio = PortfolioService()

        result = portfolio.delete_currency_data(user_id=1, currency_name="BTC")

        assert result == True
