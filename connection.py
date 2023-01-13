from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/alchemyDB', echo=True)

connection = engine.connect()

try:
    print("Connect is Done")

except:
    print("Not Connect")
