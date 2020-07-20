import unittest
from app.utils.execute_api import API
from app import db, create_app


class TestApiCall(unittest.TestCase):

    def setUp(self):
        print("setUp test env")

        # init test env
        self.app = create_app()

        self.api = API()

    def tearDown(self):
        pass

    def test_call_api(self):

        res = self.api.call_api(currency=["BTC"])

        self.assertNotEqual(res, [])

    def test_data_process(self):
        currency_data = self.api.call_api(currency=["BTC"])

        currency_list, totla_value = self.api.data_process(currency_data=currency_data,
                                                           num_of_hold_currency=[5])

        self.assertIsNotNone(totla_value)
        self.assertNotEqual(currency_list, [])


if __name__ == "__main__":
    unittest.main()
