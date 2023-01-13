from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.sql import select

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/alchemyDB', echo=True)

meta = MetaData()

employee = Table(
    'employee', meta,
    Column('id', Integer, primary_key=True),
    Column('firstname', String(20)),
    Column('lastname', String(20)),
)

address = Table(
    'address', meta,
    Column('id', Integer, primary_key=True),
    Column('emp_id', Integer, ForeignKey('employee.id')),
    Column('postal_add', String(30)),
    Column('email_add', String(30))
)

connection = engine.connect()

jn = employee.join(address, employee.c.id == address.c.id)

db = select([employee, address]).select_from(jn)

result = connection.execute(db)

for row in result:
    print(row)


# Outer Join
jnall = employee.join(address)

dball = select([employee, address]).select_from(jnall)

resultall = connection.execute(dball)

for row in resultall:
    print(row)
