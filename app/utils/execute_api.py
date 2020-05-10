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
