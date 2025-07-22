#!/usr/bin/python3
"""100-relationship_states_cities module"""

from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)
    # new_city.state = new_state
    session.add(new_state)
    session.commit()
