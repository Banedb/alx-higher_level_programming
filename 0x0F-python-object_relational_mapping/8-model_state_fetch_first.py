#!/usr/bin/python3
"""8-model_state_fetch_first module"""

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
    first = session.query(State).order_by(State.id).first()
    if first:
        print(f"{first.id}: {first.name}")
    else:
        print("Nothing")
