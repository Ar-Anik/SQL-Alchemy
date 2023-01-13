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

meta.create_all(engine)

connection = engine.connect()
connection.execute(employee.insert(), [
    {'firstname': 'Ar', 'lastname': 'Anik'},
    {'firstname': 'AC', 'lastname': 'Anik'},
    {'firstname': 'AI', 'lastname': 'Oni'},
    {'firstname': 'Priya', 'lastname': 'Rajhans'},
    {'firstname': 'Abdul', 'lastname': 'Satter'},
])

connection.execute(address.insert(), [
    {'emp_id': 1, 'postal_add': 'Khilgaon, Dhaka', 'email_add': 'aranik@gmail.com'},
    {'emp_id': 2, 'postal_add': 'Chandpur, Motlab', 'email_add': 'acanik@gmail.com'},
    {'emp_id': 3, 'postal_add': 'Cumilla, Chandina', 'email_add': 'aioni@gmail.com'},
    {'emp_id': 4, 'postal_add': 'Pune, India', 'email_add': 'priyar@gmail.com'},
    {'emp_id': 5, 'postal_add': 'Uttara, Dhaka', 'email_add': 'abduls@gmail.com'},
])

edb = employee.select()
result = connection.execute(edb)

for row in result:
    print(row)

adb = address.select()
result = connection.execute(adb)

for row in result:
    print(row)
