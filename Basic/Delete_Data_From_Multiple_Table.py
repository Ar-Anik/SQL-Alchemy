from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

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

abd = address.delete().where(address.c.email_add.startswith('abc%'))
connection.execute(abd)

edb = employee.delete().where(employee.c.firstname.startswith('xyz%'))
connection.execute(edb)
