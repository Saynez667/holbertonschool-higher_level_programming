#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from the database
Results are sorted in ascending order by states.id.
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

    # Query states that contain the letter 'a' (case-sensitive)
    states_with_a = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    # Print each matching state
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
