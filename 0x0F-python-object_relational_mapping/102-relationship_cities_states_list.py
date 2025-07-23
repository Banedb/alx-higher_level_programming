#!/usr/bin/python3
"""102-relationship_cities_states_list module"""


from relationship_state import State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}",
        pool_pre_ping=True,
    )
    session = sessionmaker(bind=engine)()
    for city in session.query(City).options(
            joinedload(City.state)).order_by(City.id):
        print(f"{city.id}: {city.name} -> {city.state.name}")
