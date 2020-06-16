from app import db


class UserCrypt(db.Model):

    __tablename__ = "user_crypt"

    user_id = db.Column(db.Integer, db.ForeignKey(
        "user.user_id"), primary_key=True)

    crypt_id = db.Column(db.Integer, db.ForeignKey(
        "crypt.crypt_id"), primary_key=True)
    num_of_currency = db.Column(db.Float)

    user = db.relationship("User")
    crypt = db.relationship("Crypt")
