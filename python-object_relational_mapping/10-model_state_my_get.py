#!/usr/bin/python3
"""
Fetches the State object with the given name from the database hbtn_0e_6_usa.
If the state is not found, prints 'Not found'.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create an engine to connect to the MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a configured session factory
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch the state based on the name passed as argument
    state_name = sys.argv[4]
    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
