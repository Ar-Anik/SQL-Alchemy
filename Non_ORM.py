from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/alchemyDB', echo=True)

cursor = engine.connect()
query = 'select * from user;'
result = cursor.execute(query)

for i in result:
    print('name: ', i[1])
    print('age: ', i[2], "\n")
