from app import db


class User(db.Model):
    """
    Define user table
    """

    __tablename__ = "user"

    user_id = db.Column("user_id", db.Integer, primary_key=True)
    user_name = db.Column("user_name", db.String(10))
    user_mail = db.Column("user_mail", db.String(320))
    user_password = db.Column("user_password", db.String(32))

    def __repr__(self):
        return f"User('{self.user_name}', '{self.user_mail}', '{self.user_password}')"
