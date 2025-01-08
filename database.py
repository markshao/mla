import os
from sqlmodel import SQLModel, create_engine
from models import *

__engine = None
sqldb = "mla.db"
sqlite_url = f"sqlite:///{sqldb}"
def get_engine(sql_url: str = None):
    global __engine
    if not __engine:
        __engine = create_engine(sqlite_url)
    return __engine

def init_database_with_schema(sqlite_url: str = None):
    if os.path.exists(sqldb):
        return 
    engine = get_engine(sqlite_url)
    SQLModel.metadata.create_all(engine)