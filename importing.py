from configload import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.data import importadores
from datetime import datetime

params_postgres = config()

HOST = params_postgres["host"]
DATABASE = params_postgres["database"]
USERNAME = params_postgres["user"]
PASSWORD = params_postgres["password"]

DATABASE_CONNECTION = f'postgresql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}'

engine = create_engine(DATABASE_CONNECTION)
conn = engine.connect()

today = datetime.today().strftime('%Y%m%d')

for importer in importadores:
    url = importer.get('url')
    print(url)

select_importers = 'SELECT * FROM importer'
result = conn.execute(select_importers)

for row in result:
    print(row)

'''
print(engine.table_names())
Session = sessionmaker(bind=engine)

print(params_postgres)
'''
