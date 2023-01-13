from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, select
from sqlalchemy import and_, or_, asc, desc, between

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
and_db = select([employee]).where(and_(employee.c.lastname == 'anik', employee.c.id < 3))
result = connection.execute(and_db)

print(result.fetchall(), "\n")

or_db = select([employee]).where(or_(employee.c.lastname == 'Anik', employee.c.id < 3))
result = connection.execute(or_db)

print(result.fetchall(), "\n")

ascOrderDB = select([employee]).order_by(asc(employee.c.lastname))
result = connection.execute(ascOrderDB)

print(result.fetchall(), "\n")

dscOrderDB = select([employee]).order_by(desc(employee.c.lastname))
result = connection.execute(dscOrderDB)

print(result.fetchall(), "\n")

betweenDB = select([employee]).where(between(employee.c.id, 2, 4))
result = connection.execute(betweenDB)

print(result.fetchall())
