from app import db
from app.models.user_crypt_db import UserCrypt


class User(db.Model):
    """
    Define user table
    """

    __tablename__ = "user"

    user_id = db.Column("user_id", db.Integer, primary_key=True)
    user_name = db.Column("user_name", db.String(10),
                          unique=True, nullable=False)
    user_mail = db.Column("user_mail", db.String(320),
                          unique=True, nullable=False)
    user_password = db.Column("user_password", db.String(32), nullable=False)
    crypts = db.relationship("Crypt", secondary=UserCrypt.__tablename__,
                             back_populates="users")
    user_crypt = db.relationship("UserCrypt")

    def __repr__(self):
        return f"User('{self.user_name}', '{self.user_mail}', '{self.user_password}')"

    @classmethod
    def find_user_email_and_name(cls, name, email):
        exist_user = User.query.filter_by(
            user_name=name).first()
        if not exist_user is None:
            return "User name"
        exist_email = User.query.filter_by(
            user_mail=email).first()
        if not exist_email is None:
            return "mail address"

        return True

    @classmethod
    def find_user_info(cls, name, mail, password):
        user = User.query.filter_by(user_name=name).first()
        if user is not None and user.user_name == name and user.user_mail == mail and user.user_password == password:
            return user.user_id

        return False

    @classmethod
    def update_user_info(cls, user_id):
        user = User.query.filter_by(user_id=user_id).first()
        if user is not None:
            return user
        return False

    @classmethod
    def delete_user_info(cls, user_id, name, mail, password):
        user = User.query.filter_by(user_id=user_id).first()
        if user is not None and user.user_name == name and user.user_mail == mail and user.user_password == password:
            return user

        return False
