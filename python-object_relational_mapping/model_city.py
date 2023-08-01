#!/usr/bin/python3
"""
Class definition of a City
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """create class City inherits Base in model_state"""
    __tablename__ = 'cities'
    id = Column(
                Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True
    )
    name = Column(
                String(128),
                nullable=False
    )
    state_id = Column(
                Integer,
                ForeignKey("states.id"),
                nullable=False
    )
