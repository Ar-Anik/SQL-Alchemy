from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/alchemyDB', echo=True)

meta = MetaData()

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('firstname', String(16)),
    Column('lastname', String(16)),
)

# ins = students.insert()
ins1 = students.insert().values(firstname='Ravi', lastname='Kapoor')
ins2 = students.insert().values(firstname='Ar', lastname='Anik')
ins3 = students.insert().values(firstname='DI', lastname='Anan')
ins4 = students.insert().values(firstname='KC', lastname='Mahin')

connection = engine.connect()
result1 = connection.execute(ins1)
result2 = connection.execute(ins2)
result3 = connection.execute(ins3)
result4 = connection.execute(ins4)

print("First : ", result1, "\n")
print("Second : ", result2, "\n")
print("Third : ", result3, "\n")
print("Four : ", result4, "\n")
