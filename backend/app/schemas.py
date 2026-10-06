from pydantic import model_validator
from sqlmodel import SQLModel

from app.enums import District, Grade, Subject


class SubjectRequest(SQLModel):
    grade: Grade
    district: District | None = None
    subject: Subject | None = None

    @model_validator(mode='after')
    def check_single_filter(self):
        if self.district is not None and self.subject:
            raise ValueError('Поиск возможен только по единственному фильтру.')
        return self
    
class SubjectCompareRequest(SQLModel):
    grade: Grade
    first_subject: Subject
    second_subject: Subject

    @model_validator(mode='after')
    def check_different_subjects(self):
        if self.first_subject == self.second_subject:
            raise ValueError('Сравнение возможно только по разным субъектам.')
        return self