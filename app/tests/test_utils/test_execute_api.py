import unittest
from app.utils.execute_api import API


class TestAPI(unittest.TestCase):

    def test_data_process(self):
        api = API()
        api_data = api.call_api(currency="BTC")

        result = api.data_process(
            currency_data=api_data, num_of_hold_currency=1)
        none_price = api.data_process(
            currency_data=api_data, num_of_hold_currency=1)

        assert int(result[1]) > 1
        self.assertIsNotNone(result[0])
        assert int(none_price[1]) == 0
