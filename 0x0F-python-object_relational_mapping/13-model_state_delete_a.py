#!/usr/bin/python3
"""
Write a script that deletes all State objects with a
name containing the letter a from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select, insert

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    deleteStates = session.query(State).filter(State.name.like(f'%a%')).all()
    if deleteStates:
        for state in deleteStates:
            session.delete(state)
        session.commit()

    session.close()
