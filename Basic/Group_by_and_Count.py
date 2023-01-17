import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Numeric, Integer, VARCHAR

engine = create_engine('postgresql+psycopg2://anik:1234@localhost/example')

meta = MetaData()

books = Table(
    'books', meta,
    Column('bookId', Integer, primary_key=True),
    Column('book_price', Numeric),
    Column('genre', VARCHAR),
    Column('book_name', VARCHAR)
)

meta.create_all(engine)

statement1 = books.insert().values(bookId=1, book_price=12.2, genre='fiction', book_name='Old Age')

statement2 = books.insert().values(bookId=2, book_price=13.2, genre='non-fiction', book_name='Saturn Rings')

statement3 = books.insert().values(bookId=3, book_price=121.6, genre='fiction', book_name='Supernova')

statement4 = books.insert().values(bookId=4, book_price=100.5, genre='non-fiction', book_name='History of the world')

statement5 = books.insert().values(bookId=5, book_price=112.2, genre='fiction', book_name='Sun City')

connection = engine.connect()
connection.execute(statement1)
connection.execute(statement2)
connection.execute(statement3)
connection.execute(statement4)
connection.execute(statement5)

allbook = meta.tables['books']

query = sqlalchemy.select([allbook.c.genre, sqlalchemy.func.count(allbook.c.genre)]).group_by(allbook.c.genre)

result = engine.execute(query).fetchall()

for i in result:
    print(i, "\n")
