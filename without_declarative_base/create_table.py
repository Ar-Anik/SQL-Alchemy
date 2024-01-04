from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import mapper, sessionmaker

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/alchemydb', echo=True)

metadata = MetaData()

table1 = Table('table1', metadata,
               Column('id', Integer, primary_key=True),
               Column('key', String(50), unique=True),
               Column('value', String(255)))

class Table1config(object):
    pass

mapper(Table1config, table1)

metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

