from app import db


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
