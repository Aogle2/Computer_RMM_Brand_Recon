"""
This is going to be all the DB models used for this.

I want to start out with using SQLite... this is something that is not really heavy, just a PoC demo thing.

"""
import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()







if __name__ == "__main__":
    engine = sqlalchemy.create_engine('sqlite:///:memory:')


