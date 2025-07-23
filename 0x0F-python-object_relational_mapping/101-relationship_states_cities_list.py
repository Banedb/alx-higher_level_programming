#!/usr/bin/python3
"""101-relationship_states_cities_list module"""
from relationship_state import State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}',
        pool_pre_ping=True
    )

    session = sessionmaker(bind=engine)()
    for state in session.query(State).options(
            joinedload(State.cities)).order_by(State.id):
        print(f"{state.id}: {state.name}")
        for city in sorted(state.cities, key=lambda x: x.id):
            print(f"\t{city.id}: {city.name}")
