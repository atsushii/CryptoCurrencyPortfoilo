from app.config import Config
from app.utils.crypt_validation import CryptValidation
import urllib.request
import json


class API():

    def __init__(self):
        self.api_key = Config.URL

    def call_api(self, currency):
        url = self.api_key.format(",".join(currency))
        return json.load(urllib.request.urlopen(url))

    def data_process(self, currency_data, num_of_hold_currency):
        currency_list = []
        total_value = 0
        for item, num in zip(currency_data, num_of_hold_currency):
            currency_dict = {}
            currency_dict["symbol"] = item["symbol"]
            currency_dict["price"] = float(item["price"])
            currency_dict["num_hold"] = num
            currency_dict["price_change_pct"] = item["1d"]["price_change_pct"]

            # compute total value
            total_value += currency_dict["price"] * num
            currency_list.append(currency_dict)
        return currency_list, total_value
