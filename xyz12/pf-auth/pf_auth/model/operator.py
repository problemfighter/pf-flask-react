from pf_auth.common.password_util import get_password_hash, validate_password
from pf_sqlalchemy.db.orm import Base, database


class Operator(Base):
    first_name = database.Column("first_name", database.String(100))
    last_name = database.Column("last_name", database.String(100))
    name = database.Column("name", database.String(100))
    email = database.Column("email", database.String(100), unique=True, index=True)
    username = database.Column("username", database.String(100), unique=True, index=True)
    password_hash = database.Column("password_hash", database.String(150), nullable=False, index=True)
    isVerified = database.Column("is_verified", database.Boolean, default=True)
    token = database.Column("token", database.String(200))
    tokens = database.relationship('OperatorToken', backref='operator', lazy=True)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = get_password_hash(password)

    def verify_password(self, password) -> bool:
        return validate_password(self.password_hash, password)
