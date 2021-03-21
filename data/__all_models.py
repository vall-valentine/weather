import sqlalchemy

from .db_session import SqlAlchemyBase


class Temp(SqlAlchemyBase):
    __tablename__ = 'data'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    date = sqlalchemy.Column(sqlalchemy.TIMESTAMP, nullable=True)
    temp = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    city = sqlalchemy.Column(sqlalchemy.String, nullable=True)