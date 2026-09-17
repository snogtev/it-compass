
from sqlmodel import Field, SQLModel, create_engine


class Subject(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    district: str = Field(index=True)
    salary_intern: int
    salary_junior: int
    salary_middle: int
    salary_senior: int

sqlite_file_name = 'subjects.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

connect_args = {'check_same_thread': False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)