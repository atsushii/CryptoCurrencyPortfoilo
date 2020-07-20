import unittest
from app.utils.execute_crypt_db import PortfolioService
from app import db, create_app
from app.models.user_db import User
from app.models.crypt_db import Crypt
from app.models.user_crypt_db import UserCrypt


class TestPortfolioService(unittest.TestCase):

    def setUp(self):
        print("setUp test env")

        # init test env
        self.app = create_app()
        db.create_all()

        # init user data
        user = User(user_name="atushi",
                    user_mail="test@gmail.com", user_password="Amjsbs@1")

        user2 = User(user_name="John",
                     user_mail="test2@gmail.com", user_password="Amjsbs@1")

        # init currency data
        ctypt = Crypt(crypt_id=1, crypt_name="BTC")

        self.portfolio_service = PortfolioService()

        db.session.add(user)
        db.session.commit()
        db.session.add(user2)
        db.session.commit()

        db.session.add(ctypt)
        db.session.commit()

    def tearDown(self):
        print("tearDown")
        db.session.remove()
        db.drop_all()

    def test_register(self):

        # arg is valid currency name
        res = self.portfolio_service.register(
            user_id=1, crypt_name="BTC", num_of_currency=5)

        self.assertTrue(res)

        # arg is invalid currency name
        res = self.portfolio_service.register(
            user_id=1, crypt_name="ETH", num_of_currency=1)
        self.assertFalse(res)

    def test_fetch_portfolio_data(self):

        # add test data to user_crypt db
        self.portfolio_service.register(
            user_id=1, crypt_name="BTC", num_of_currency=5)

        res = self.portfolio_service.get_user_portfolio(user_id=1)

        self.assertIsNotNone(res)

        res = self.portfolio_service.get_user_portfolio(user_id=2)

        self.assertFalse(res)

    def test_edit_portfolio(self):

        res = self.portfolio_service.update_currency_data(
            user_id=1, currency_name="BTC", num_hold=10)

        self.assertTrue(res)

    def test_delete_currency_from_portfolio(self):

        # add test data to user_crypt db
        self.portfolio_service.register(
            user_id=1, crypt_name="BTC", num_of_currency=5)

        # valid data
        res = self.portfolio_service.delete_currency_data(
            user_id=1, currency_name="BTC")

        self.assertTrue(res)

        res = self.portfolio_service.delete_currency_data(
            user_id=1, currency_name="ADA")

        self.assertFalse(res)


if __name__ == "__main__":
    unittest.main()
