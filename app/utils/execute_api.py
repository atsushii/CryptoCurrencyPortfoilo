from app.config import Config
import urllib.request


class API():

    def __init__(self):
        self.api_key = Config.URL

    def call_api(self, currency):
        url = self.api_key.format(",".join(currency))

        print(urllib.request.urlopen(url).read())
