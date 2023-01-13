from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy.orm import mapper

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/alchemyDB', echo=True)

metadata = MetaData()

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('password', String(50)))

class User():
    def __init__(self, name, password):
        self.name = name
        self.password = password

mapper(User, user)
metadata.create_all(engine)
