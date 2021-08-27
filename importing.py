from configload import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.data import importadores

params_postgres = config()

HOST = params_postgres["host"]
DATABASE = params_postgres["database"]
USERNAME = params_postgres["user"]
PASSWORD = params_postgres["password"]

DATABASE_CONNECTION = f'postgresql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}'

engine = create_engine(DATABASE_CONNECTION)
conn = engine.connect()


select_importers = 'SELECT * FROM importer'
result = conn.execute(select_importers)

for row in result:
    print(row)

'''
print(engine.table_names())
Session = sessionmaker(bind=engine)

print(params_postgres)
'''