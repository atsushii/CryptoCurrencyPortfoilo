from app import db
from app.models.user_db import User
from app.models.crypt_db import Crypt
from app.utils.crypt_validation import CryptValidation
from sqlalchemy.exc import IntegrityError
from flask import session


class PortfolioService():

    def register(self, user_id, coin_name):
        """
        Insert currency data
        """
        validator = CryptValidation()
        error = validator.validate(coin_name)
        if not error:
            return "Cant find currency name Try again"

        try:
            u = User()
            c = Crypt()
            u.crypt.append(c)
            db.session.add(u)
            db.session.commit()
        except ImportError:
            db.session.roleback()
            return "db error"

        return True
