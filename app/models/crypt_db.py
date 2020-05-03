from app import db


class Crypt(db.Model):

    """
    Define cryptcurrency table
    """

    __tablename__ = 'crypt'

    crypt_id = db.Column(
        "crypt_id", db.Integer, primary_key=True)
    crypt_name = db.Column("crypt_name", db.String(20))

    def __repr__(self):
        return f"Crypt('{self.crypt_id}', '{self.crypt_name}')"
