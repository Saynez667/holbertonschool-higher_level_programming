#!/usr/bin/python3
"""
Adds a new State object "Louisiana" to the database hbtn_0e_6_usa.
Displays the new state's id after creation.
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

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new state to the session and commit it to the database
    session.add(new_state)
    session.commit()

    # Print the ID of the newly added state
    print(new_state.id)

    # Close the session
    session.close()
