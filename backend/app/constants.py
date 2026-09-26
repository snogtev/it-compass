from enum import Enum

DISTRICTS = (
    'central',
    'far-eastern',
    'north-caucasian',
    'northwestern',
    'siberian',
    'southern',
    'ural',
    'volga',
)

class Districts(str, Enum):
    central = 'central'
    far_eastern = 'far_eastern'
    north_caucasian = 'north_caucasian'
    northwestern = 'northwestern'
    siberian = 'siberian'
    southern = 'southern'
    ural = 'ural'
    volga = 'volga '
class Grade(str, Enum):
    applicant = 'applicant'
    intern = 'intern'
    junior = 'junior'
    middle = 'middle'
    senior = 'senior'

GRADES = (
    'applicant',
    'intern',
    'junior',
    'middle',
    'senior',
)

SALARY_FIELDS = {
    f'salary_{grade}': f'salary_{grade}_score'  
    for grade in GRADES
    if grade != 'applicant'
}

TABLE_URL = 'https://docs.google.com/spreadsheets/d/1lIBTPfrnWqKXFGtRRADZOQvK1OPc1kHU6KBLiLMRR1s/export?gid=0&format=csv'
SQLITE_URL = 'sqlite:///subjects.db'