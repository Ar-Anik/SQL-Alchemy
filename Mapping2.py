from sqlalchemy import create_engine
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/alchemyDB', echo=True)

BASE = declarative_base()

class Customer(BASE):
    __tablename__ = "Customer"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

    def __str__(self):
        return self.name

BASE.metadata.create_all(engine)
