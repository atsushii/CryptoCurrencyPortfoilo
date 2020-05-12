from app import db
from app.models.user_db import User
from app.models.crypt_db import Crypt
from app.models.user_crypt_db import UserCrypt
from app.utils.crypt_validation import CryptValidation
from sqlalchemy.orm.exc import FlushError


class PortfolioService():

    def register(self, user_id, crypt_name, num_of_currency):
        """
        Insert currency data
        """
        validator = CryptValidation()
        # return crypt and user data
        result = validator.validate(user_id, crypt_name)
        if not result:
            return "Cant find currency name Try again"

        try:
            # 0 user, 1 crypy
            user_crypt = UserCrypt(num_of_currency=num_of_currency)
            user_crypt.user = result[0]
            result[1].user_crypt.append(user_crypt)
            db.session.add(result[1])
            db.session.commit()
        except FlushError:
            db.session.rollback()
            return f"Alredy {crypt_name} in your portfolio"

        return True

    def get_user_portfolio(self, user_id):
        """
        Get user's currency data
        """
        validator = CryptValidation()
        result = validator.validate_portfolio_data(user_id)

        return result

    def update_currency_data(self, user_id, currency_name, num_of_hold):
        """
        update currency information
        """
        # get user info
        user = User.update_user_info(user_id)
        # get currency data
        user_data = user.crypts
        num_data = user.user_crypt

        try:

            for name, num in zip(user_data, num_data):
                if name.crypt_name == currency_name:
                    num.num_of_currency = num_of_hold
                    break
            db.session.commit()

        except FlushError:
            db.session.rollback()
            return False

        return True

    def delete_currency_data(self, user_id, currency_name):
        """
        Delete currency from portfolio
        """
        # get user info
        user = User.update_user_info(user_id)
        # get currency data
        user_data = user.crypts
        try:
            for i, name in enumerate(user_data):
                if name.crypt_name == currency_name:
                    del user_data[i]
            db.session.add(user)
            db.session.commit()
        except FlushError:
            db.session.rollback()
            return False

        return True
