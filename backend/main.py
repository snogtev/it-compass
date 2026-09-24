from fastapi import FastAPI, Path
from sqlmodel import Session

from backend.constants import Districts, Grade
from backend.database import Subject, create_db_and_tables, engine
from backend.scripts.data_normalization import create_salary_scores
from backend.scripts.import_xlsx import import_data

app = FastAPI()

create_db_and_tables()
import_data()
create_salary_scores()

@app.get('/')
def get_home_page():
    return {'сообщение': 'Сайт работает!'}

@app.get('/subjects')
def get_subjects(grade: Grade, district: Districts | None = None):
    return {'Грейд': grade,
            'Округ': district
            }

@app.get('/subjects/{id}')
def get_subject(id: int = Path(ge=1, le=89)):
    with Session(engine) as session:
        subject = session.get(Subject, id)
        return subject