#!/usr/bin/python3
"""model_city module"""

from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Defines City class that inherits from Base."""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
