from app.models.crypt_db import Crypt
from app.models.user_db import User


class CryptValidation():
    """
    Validate input data
    """

    def validate(self, user_id, crypt_name):
        """
        Check currency name is in db
        """
        crypt = Crypt.find_currency_name(crypt_name)
        # get user info
        user = User.update_user_info(user_id)

        if crypt is not None and user != False:
            return user, crypt
        return False

    def validate_portfolio_data(self, user_id):
        """
        Check user has currency data in db
        """
        # get current portfolio info
        name_of_currency_list = []
        num_of_currency_list = []
        currency = []
        user = User.update_user_info(user_id)
        user_data = user.crypts
        num_data = user.user_crypt
        if not user_data:
            return False
        for name, num in zip(user_data, num_data):
            name_of_currency_list.append(name.crypt_name)
            num_of_currency_list.append(num.num_of_currency)
        currency.append(name_of_currency_list)
        currency.append(num_of_currency_list)
        return currency
