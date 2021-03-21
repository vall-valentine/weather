import sqlalchemy
from .db_session import SqlAlchemyBase


class Temp(SqlAlchemyBase):
    __tablename__ = 'data'

    id = sqlalchemy.Column(sqlalchemy.BIGINT,
                           primary_key=True, autoincrement=True)
    date = sqlalchemy.Column(sqlalchemy.TIMESTAMP, nullable=True)
    temp = sqlalchemy.Column(sqlalchemy.FLOAT, nullable=True)
    city = sqlalchemy.Column(sqlalchemy.TEXT, nullable=True)