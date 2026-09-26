from sqlmodel import Field, SQLModel


class Subject(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    name_slug: str = Field(index=True)
    district: str = Field(index=True)
    district_slug: str = Field(index=True)
    salary_intern: int | None = Field(default=None)
    salary_junior: int | None = Field(default=None)
    salary_middle: int | None = Field(default=None)
    salary_senior: int | None = Field(default=None)
    salary_intern_score: int | None = Field(default=None, ge=1, le=100)
    salary_junior_score: int | None = Field(default=None, ge=1, le=100)
    salary_middle_score: int | None = Field(default=None, ge=1, lt=100)
    salary_senior_score: int | None = Field(default=None, ge=1, le=100)
    subsistence_minimum: int | None = Field(default=None)