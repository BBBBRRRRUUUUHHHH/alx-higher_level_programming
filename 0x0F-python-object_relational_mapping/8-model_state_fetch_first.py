#!/usr/bin/python3
"""
Write a script that prints the first
State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    with engine.connect() as connection:
        query = select(State).order_by(State.id.asc())
        state = connection.execute(query).fetchone()
        if state:
            print(f"{state.id}: {state.name}")
        else:
            print("Nothing")

    engine.dispose()
