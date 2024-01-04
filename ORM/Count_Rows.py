from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Integer, String, Column, Float
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('postgresql+psycopg2://anik:1234@localhost/example')

Session = sessionmaker(bind = engine)
session = Session()

class Boi(Base):
    __tablename__ = 'Boi'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price = Column(Float)
    genre = Column(String(50))

Base.metadata.create_all(engine)

session.add_all([
    Boi(id=1, name='Old Age', price=12.2, genre="fiction"),
    Boi(id=2, name='Saturn Rings', price=13.2, genre="non-fiction"),
    Boi(id=3, name='Supernova', price=121.6, genre='fiction'),
    Boi(id=4, name='History of the world', price=100.5, genre='non-fiction'),
    Boi(id=5, name='Sun City', price=112.2, genre='fiction')
])

session.commit()
result = session.query(Boi).count()

print(result)
