from fastapi import FastAPI, Query
from sqlmodel import Session, select

from app.database import Subject, engine
from app.schemas import SubjectRequest

app = FastAPI()

@app.get('/')
def get_home_page():
    return {'сообщение': 'Сайт работает!'}

@app.get('/subjects')
def get_subjects(subject_request: SubjectRequest = Query()):  # noqa: B008
    with Session(engine) as session:

        if subject_request.district:
            statement = select(Subject).where(Subject.district_slug == subject_request.district)

        elif subject_request.subject:
            statement = select(Subject).where(Subject.name_slug == subject_request.subject)

        elif subject_request.district is None and subject_request.subject is None:
            statement = select(Subject)

        results = session.exec(statement).all()
        
        results = {'data':
                   [{'id': row.id,
                    'name': row.name,
                    'district': row.district
                    }
                    for row in results]
                   }        
             
    return results