#!/usr/bin/python3
"""
Module that contains he class definition of a State
and an instance Base = declarative_base()
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Class state that inherits from Base"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True,)
    name = Column(String(128), nullable=False)
