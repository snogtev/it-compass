from enum import Enum

from pydantic import model_validator
from sqlmodel import SQLModel


class Grade(str, Enum):
    APPLICANT = 'applicant'
    INTERN = 'intern'
    JUNIOR = 'junior'
    MIDDLE = 'middle'
    SENIOR = 'senior'


class District(str, Enum):
    CENTRAL = 'central'
    FAR_EASTERN = 'far-eastern'
    NORTH_CAUCASIAN = 'north-caucasian'
    NORTHWESTERN = 'northwestern'
    SIBERIAN = 'siberian'
    SOUTHERN = 'southern'
    URAL = 'ural'
    VOLGA = 'volga'


class SubjectRequest(SQLModel):
    grade: Grade
    district: District| None = None
    subject: str | None = None

    @model_validator(mode='after')
    def check_it_benefits(self):
        if self.district is not None and self.subject:
            raise ValueError('Поиск возможен только по единственному фильтру!')
        return self
