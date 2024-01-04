from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/alchemyDB', echo=True)

Base = declarative_base()

class Test(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    address = Column(String(40))
    email = Column(String(40))

Session = sessionmaker(bind=engine)
session = Session()

row1 = Test(name='Anik', address="xyz", email='xyz@gmail.com')

session.add(row1)

session.add_all([
    Test(name="abc", address="gulistan", email="abc@gmail.com"),
    Test(name="def", address="motijil", email="def@gmail.com"),
    Test(name="ijk", address="Framget", email="ijk@gmail.com"),
])

session.commit()