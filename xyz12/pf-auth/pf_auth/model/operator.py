from pf_sqlalchemy.db.orm import Base, database


class Operator(Base):
    first_name = database.Column("first_name", database.String(100))
    last_name = database.Column("last_name", database.String(100))
    name = database.Column("name", database.String(100))
    email = database.Column("email", database.String(100), unique=True, index=True)
    username = database.Column("username", database.String(100), unique=True, index=True)
    password = database.Column("password", database.String(150), nullable=False, index=True)
    isVerified = database.Column("is_verified", database.Boolean, default=True)
    token = database.Column("token", database.String(200))
    tokens = database.relationship('OperatorToken', backref='operator', lazy=True)
