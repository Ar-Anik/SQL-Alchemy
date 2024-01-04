from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/alchemydb', echo=True)

metadata = MetaData()

parent_table = Table('parent', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('name', String(50)))

child_table = Table('child', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(50)),
                    Column('parent_id', Integer, ForeignKey('parent.id')))

class Parent(object):
    pass

class Child(Parent):  # Make Child inherit from Parent
    pass

mapper(Parent, parent_table)
mapper(Child, child_table)

metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
