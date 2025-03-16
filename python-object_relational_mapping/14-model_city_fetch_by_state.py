#!/usr/bin/python3
"""List all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City  # Don't forget to import the City class!

if __name__ == "__main__":

    # Check the number of arguments
    if len(sys.argv) != 4:
        exit(1)

    # Connect to the database
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, db_name),
        pool_pre_ping=True
    )

    # Create the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the cities and associated states
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Display the results
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
