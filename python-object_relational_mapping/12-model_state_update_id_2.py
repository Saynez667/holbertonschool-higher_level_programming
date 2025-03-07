#!/usr/bin/python3
"""
Updates the name of the State object where id = 2 to 'New Mexico'.
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

    # Get the state object with id = 2
    state = session.query(State).filter(State.id == 2).first()

    if state:
        # Update the state's name
        state.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
