from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import mapper, relationship, sessionmaker, subqueryload

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/alchemydb', echo=True)
metadata = MetaData()

user_table = Table('users', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('username', String(50)),
                   Column('email', String(50)))

address_table = Table('address', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('user_id', Integer, ForeignKey('users.id')),
                      Column('address', String(255)))

class User(object):
    def __init__(self, username, email):
        self.user_name = username
        self.user_email = email

class Address(object):
    def __init__(self, address):
        self.address = address

mapper(User, user_table, properties={
    'user_id': user_table.c.id,
    'user_name': user_table.c.username,
    'user_email': user_table.c.email,
    'addresses': relationship(Address)
})

mapper(Address, address_table, properties={
    'address_id': address_table.c.id,
    'user_id': address_table.c.user_id,
    'address': address_table.c.address
})

metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user1 = User(username='Ar Anik', email='aranik@gmail.com')
address1 = Address(address='Khilgaon, Dhaka-1219')
address2 = Address(address='Tajgone, Dhaka-1212')
user1.addresses = [address1, address2]

address3 = Address(address='123 Main St.')
user2 = User(username='Mr. Shourov', email='abshourov@gmail.com')
user2.addresses = [address3]

address4 = Address(address='Uttara, Village-1111')
user3 = User(username='Mr. Jashim', email='jashim@gmail.com')
user3.addresses = [address4]

session.add(user1)
session.add(user2)
session.add(user3)
session.commit()

users_with_address = session.query(User).options(subqueryload(User.addresses)).all()

for user in users_with_address:
    print(f"User: {user.user_name}, Email: {user.user_email}")
    for address in user.addresses:
        print(f"Address : {address.address}")

