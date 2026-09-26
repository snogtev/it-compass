from fastapi import FastAPI
from sqlmodel import Session, select

from app.constants import Districts, Grade
from app.database import Subject, engine

app = FastAPI()

@app.get('/')
def get_home_page():
    return {'сообщение': 'Сайт работает!'}

@app.get('/subjects')
def get_subjects(grade: Grade, district: Districts | None = None):
    with Session(engine) as session:
        if district:
            statement = select(Subject).where(Subject.district_slug == district)
        else:
            statement = select(Subject.name, Subject.district)
        results = session.exec(statement).all()
        results = [{'name': row.name, 'district': row.district} for row in results]     
    return results

@app.get('/subjects/{id}')
def get_subject(grade: Grade, subject: Subject | None = None):
    with Session(engine) as session:
        subject = session.get(Subject, id)
        return subject