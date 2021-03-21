import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase

from werkzeug.security import generate_password_hash, check_password_hash


class Users(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    login = sqlalchemy.Column(sqlalchemy.String, nullable=True)
import sqlalchemy

from .db_session import SqlAlchemyBase


class Temp(SqlAlchemyBase):
    __tablename__ = 'data'

    id = sqlalchemy.Column(sqlalchemy.BIGINT,
                           primary_key=True, autoincrement=True)
    date = sqlalchemy.Column(sqlalchemy.TIMESTAMP, nullable=True)
    temp = sqlalchemy.Column(sqlalchemy.FLOAT, nullable=True)
    city = sqlalchemy.Column(sqlalchemy.TEXT, nullable=True)