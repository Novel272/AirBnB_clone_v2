#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Represent user for MySQL database.

    Inheri from SQLAlchemy Base and links to  MySQL table users.

    Attributes:
        __tablename__ (str):ame of the MySQL table to store users.
        email: (sqlalchemy String): T user's email address.
        password (sqlalchemy String):is user's password.
        first_name (sqlalchemy String): user's first name.
        last_name (sqlalchemy String):s  user's last name.
        places (sqlalchemy relationship): TUser-Place relationship.
        reviews (sqlalchemy relationship): Theiiser-Review relationship.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")

