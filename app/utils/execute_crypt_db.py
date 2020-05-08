from app import db
from app.models.user_db import User
from app.models.crypt_db import Crypt
from app.utils.crypt_validation import CryptValidation
from sqlalchemy.exc import IntegrityError
from flask import session


class PortfolioService():

    def register(self, user_id, crypt_name):
        """
        Insert currency data
        """
        validator = CryptValidation()
        # return crypt and user data
        result = validator.validate(user_id, crypt_name)
        if not result:
            return "Cant find currency name Try again"

        try:
            result[0].portfolio.append(result[1])
            db.session.commit()
        except IntegrityError:
            db.session.roleback()
            return "db error"

        return True
