from fastapi import FastAPI, HTTPException
from sqlmodel import Session

from backend.constants import DISTRICTS, GRADES
from backend.data_normalization import create_salary_scores
from backend.database import Subject, create_db_and_tables, engine
from scripts.import_xlsx import import_data

app = FastAPI()

create_db_and_tables()
import_data()
create_salary_scores()

@app.get('/')
def get_home_page():
    return {'сообщение': 'Сайт работает!'}

@app.get('/subjects')
def get_subjects(grade: str, district: str | None = None,):
    if grade not in GRADES:
        raise HTTPException(status_code=400, detail='Данного грейда не сущствует!')
    if district and district not in DISTRICTS:
        raise HTTPException(status_code=400, detail='Данного округа не существует!')
    return {'Грейд': grade,
            'Округ': district
            }

@app.get('/subjects/{id}')
def get_subject(id: int):
    with Session(engine) as session:
        subject = session.get(Subject, id)
        if not subject:
                raise HTTPException(status_code=400, detail='Данного субъекта не сущствует!')
        return subject