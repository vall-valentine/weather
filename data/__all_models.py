import sqlalchemy

from .db_session import SqlAlchemyBase


class Temp(SqlAlchemyBase):
    __tablename__ = 'data'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    day = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    month = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    year = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    temp = sqlalchemy.Column(sqlalchemy.String, nullable=True)