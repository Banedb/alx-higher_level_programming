#!/usr/bin/python3
"""12-model_state_update_id_2 module"""

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
    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()
