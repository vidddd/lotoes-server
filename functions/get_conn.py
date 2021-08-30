from configload import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_conn_db():
    params_postgres = config()
    HOST = params_postgres["host"]
    DATABASE = params_postgres["database"]
    USERNAME = params_postgres["user"]
    PASSWORD = params_postgres["password"]

    DATABASE_CONNECTION = f'postgresql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}'

    # echo flag for show looging sql
    engine = create_engine(DATABASE_CONNECTION, echo=True)
    # return engine.connect()
    return engine

def get_session_db():
    params_postgres = config()
    HOST = params_postgres["host"]
    DATABASE = params_postgres["database"]
    USERNAME = params_postgres["user"]
    PASSWORD = params_postgres["password"]

    DATABASE_CONNECTION = f'postgresql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}'

    # echo flag for show looging sql
    engine = create_engine(DATABASE_CONNECTION, echo=True)
    return sessionmaker(bind = engine)