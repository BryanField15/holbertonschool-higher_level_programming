#!/usr/bin/python3
"""
Prints all City objects in the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    usr = sys.argv[1]
    passwrd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(usr, passwrd, db),
        pool_pre_ping=True,
        echo=False
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    cities_to_print = session.query(City, State).
        filter(State.id == City.state_id).all()
    for city, state in cities_to_print:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.commit()
    session.close()
