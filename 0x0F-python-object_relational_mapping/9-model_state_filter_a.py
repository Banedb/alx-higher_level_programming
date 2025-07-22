#!/usr/bin/python3
"""9-model_state_filter_a module"""

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
    for state in session.query(State).order_by(State.id).filter(
            State.name.ilike('%a%')):
        print(f"{state.id}: {state.name}")
