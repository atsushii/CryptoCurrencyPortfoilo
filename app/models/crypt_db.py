from app import db
from app.models.user_crypt_db import UserCrypt


class Crypt(db.Model):

    """
    Define cryptcurrency table
    """

    __tablename__ = 'crypt'

    crypt_id = db.Column(
        "crypt_id", db.Integer, primary_key=True)
    crypt_name = db.Column("crypt_name", db.String(20),
                           unique=True, nullable=False)
    user = db.relationship("User",
                           secondary=UserCrypt.user_crypt, backref=db.backref("portfolio", lazy="dynamic"))

    def __repr__(self):
        return f"Crypt('{self.crypt_id}', '{self.crypt_name}')"

    @classmethod
    def find_currency_name(cls, crypt_name):

        crypt = Crypt.query.filter_by(crypt_name=crypt_name).first()
        return crypt
