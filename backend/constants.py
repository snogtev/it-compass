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
    far_eastern = 'far-eastern'
    north_caucasian = 'north-caucasian'
    northwestern = 'northwestern'
    siberian = 'siberian'
    southern = 'southern'
    ural = 'ural'
    volga = 'volga'
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

TABLE_URL = 'https://docs.google.com/spreadsheets/d/1-E4EgjpA8y6P0-_NZw2QQFV8Kicgf_G11pMzYV15coo/export?gid=0&format=csv'
SQLITE_URL = 'sqlite:///subjects.db'
