from sqlmodel import Field, SQLModel, create_engine

from app.constants import SQLITE_URL


class Subject(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    district: str = Field(index=True)
    salary_intern: int
    salary_junior: int
    salary_middle: int
    salary_senior: int
    salary_intern_score: int | None = Field(default=None, ge=1, le=100)
    salary_junior_score: int | None = Field(default=None, ge=1, le=100)
    salary_middle_score: int | None = Field(default=None, ge=1, lt=100)
    salary_senior_score: int | None = Field(default=None, ge=1, le=100)

connect_args = {'check_same_thread': False}
engine = create_engine(SQLITE_URL, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)