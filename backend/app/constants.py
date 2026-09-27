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