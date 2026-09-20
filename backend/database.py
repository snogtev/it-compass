from sqlmodel import Field, SQLModel, create_engine

from backend.constants import SQLITE_URL


class Subject(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    district: str = Field(index=True)
    salary_intern: int
    salary_junior: int
    salary_middle: int
    salary_senior: int
    salary_intern_score: int | None = Field(default=None)
    salary_junior_score: int | None = Field(default=None)
    salary_middle_score: int | None = Field(default=None)
    salary_senior_score: int | None = Field(default=None)

connect_args = {'check_same_thread': False}
engine = create_engine(SQLITE_URL, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)