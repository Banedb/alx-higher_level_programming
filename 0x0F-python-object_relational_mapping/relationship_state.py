#!/usr/bin/python3
"""model_state module"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Defines State class that inherits from Base."""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    # No need to add nullable, autoincrement, unique cuz PKs enforce all that.
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete-orphan",
        passive_deletes=True
    )
