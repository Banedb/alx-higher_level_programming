#!/usr/bin/python3
"""7-model_state_fetch_all module"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}',
        pool_pre_ping=True
    )
    session = sessionmaker(bind=engine)()
    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")
