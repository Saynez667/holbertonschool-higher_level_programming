#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
If the table is empty, prints "Nothing".
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

    # Fetch the first state object ordered by id
    first_state = session.query(State).order_by(State.id).first()

    # Print the first state or "Nothing" if no states exist
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
