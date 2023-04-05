from sqlalchemy import create_engine,MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = 'sqlite:///fastapidb.sqlite3'
meta = MetaData()

engine = create_engine(DB_URL,connect_args={'check_same_thread': False})

sessionlocal = sessionmaker(autocommit=False, bind=engine)
Base =declarative_base()
