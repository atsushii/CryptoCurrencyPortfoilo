from app.models.crypt_db import Crypt


class CryptValidation():
    """
    Validate input data
    """

    def validate(self, coin_name):
        """
        Check currency name is in db
        """
        crypt = Crypt.find_currency_name(coin_name)

        if crypt is not None:
            return crypt
        return False
