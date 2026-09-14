from fastapi import FastAPI, HTTPException

from backend.constants import DISTRICTS, GRADES
from backend.database import create_db_and_tables

app = FastAPI()

create_db_and_tables()

@app.get('/')
def get_home_page():
    return {'сообщение': 'Сайт работает!'}

@app.get('/subjects')
def get_subjects(grade: str, district: str | None = None):
    if grade not in GRADES:
        raise HTTPException(status_code=400, detail='Данного грейда не существует!')
    if district and district not in DISTRICTS:
        raise HTTPException(status_code=400, detail='Данного округа не существует!')
    return {'Грейд': grade,
            'Округ': district
            }