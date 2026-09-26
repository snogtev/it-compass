from sqlmodel import SQLModel, create_engine

from app.constants import SQLITE_URL
from app.models import Subject  # noqa: F401

connect_args = {'check_same_thread': False}
engine = create_engine(SQLITE_URL, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)