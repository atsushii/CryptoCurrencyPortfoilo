from app import db


class UserCrypt():
    user_crypt = db.Table('user_crypt',
                          db.Column("user_id", db.Integer, db.ForeignKey(
                              "user.user_id"), primary_key=True),
                          db.Column("crypt_id", db.Integer, db.ForeignKey(
                              "crypt.crypt_id"), primary_key=True))

    def __repr__(self):
        return f"UserCrypt('{self.user_id}', '{self.crypt_id}')"
