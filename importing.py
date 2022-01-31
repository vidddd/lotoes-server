
from functions.get_conn import get_conn_db
from config.data import importadores_lista
from lotoesserver.entities.importer import *
'''

# retur a engine object
engine = get_conn_db()

delete_importers = 'DELETE  FROM importer'
result = engine.execute(delete_importers)

query="INSERT INTO importer (name ,name_system ,active ,sorteo_type,url,param_fecha,dias)  VALUES(%s,%s,%s,%s,%s,%s,%s)"
id=engine.execute(query,importadores_lista)
print("Rows Added  = ",id.rowcount)
    

select_importers = 'SELECT * FROM importer'
result = engine.execute(select_importers)

for row in result:
    print(row)
    '''
