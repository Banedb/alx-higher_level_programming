#!/usr/bin/python3
"""14-model_city_fetch_by_state module"""

from model_city import City
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
    for city, state in session.query(City, State).join(
            State, City.state_id == State.id).order_by(City.id):
        print(f"{state.name}: ({city.id}) {city.name}")
