from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/alchemyDB', echo=True)

Base = declarative_base()

class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    address = Column(String(40))
    email = Column(String(40))

Base.metadata.create_all(engine)
