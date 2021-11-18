from pf_sqlalchemy.db.orm import database, PrimeBase


class OperatorToken(database.Model):
    id = database.Column("id", database.BigInteger, primary_key=True)
    token = database.Column("token", database.String(350), nullable=False)
    name = database.Column("name", database.String(25))
    created = database.Column("created", database.DateTime, default=database.func.now())
    updated = database.Column("updated", database.DateTime, default=database.func.now(), onupdate=database.func.now())
    operatorId = database.Column("operator_id", database.BigInteger, database.ForeignKey('operator.id'), nullable=False)
