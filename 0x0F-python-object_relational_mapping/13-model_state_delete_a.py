#!/usr/bin/python3
"""13-model_state_delete_a module"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}',
        pool_pre_ping=True
    )
    session = sessionmaker(bind=engine)()
    for state in session.query(State).filter(State.name.like('%a%')):
        session.delete(state)
    session.commit()
