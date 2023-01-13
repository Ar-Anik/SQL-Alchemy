from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/alchemyDB', echo=True)

meta = MetaData()

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('firstname', String(16)),
    Column('lastname', String(16)),
)

sdb = students.select()
connection = engine.connect()
result = connection.execute(sdb)

for row in result:
    print(row, "\n")
