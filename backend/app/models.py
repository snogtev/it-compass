from sqlmodel import Field, Relationship, SQLModel


class District(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False)
    name_slug: str = Field(index=True, unique=True, nullable=False)

    subjects: list['Subject'] = Relationship(back_populates='district')


class Subject(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False)
    name_slug: str = Field(index=True, unique=True, nullable=False)

    district_id: int = Field(foreign_key='district.id')
    district: District | None = Relationship(back_populates='subjects')

    subsistence_minimum: int | None = Field(default=None)

    salary_average: int | None = Field(default=None)
    salary_intern: int | None = Field(default=None)
    salary_junior: int | None = Field(default=None)
    salary_middle: int | None = Field(default=None)
    salary_senior: int | None = Field(default=None)

    salary_average_score: int | None = Field(default=None)
    salary_intern_score: int | None = Field(default=None)
    salary_junior_score: int | None = Field(default=None)
    salary_middle_score: int | None = Field(default=None)
    salary_senior_score: int | None = Field(default=None)