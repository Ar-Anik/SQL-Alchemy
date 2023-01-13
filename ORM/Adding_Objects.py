from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/alchemyDB', echo=True)

Base = declarative_base()

class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    address = Column(String(40))
    email = Column(String(40))

Session = sessionmaker(bind=engine)
session = Session()

row1 = Customers(name='Ravi Kumar', address='Khilgaon', email='ravi@gmail.com')

session.add(row1)

session.add_all([
    Customers(name='Komal Pande', address='Dhaka', email='komal@gmail.com'),
    Customers(name='Rajender Nath', address='Gulistan', email='nath@gmail.com'),
    Customers(name='S.M.Krishna', address='Motijil', email='smk@gmail.com')
])

session.commit()
