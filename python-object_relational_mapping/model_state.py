#!/usr/bin/python3

"""
Defines a State class and an instance of Base for SQLAlchemy ORM mapping.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

""" Create an instance of the declarative base """
Base = declarative_base()


class State(Base):
    """
    State class:
    - Inherits from Base.
    - Maps to the MySQL table `states`.
    - Has two columns: `id` (primary key) and `name` (string, max 128 chars).
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
