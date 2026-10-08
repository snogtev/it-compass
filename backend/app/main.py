from fastapi import FastAPI, Query
from sqlmodel import Session, or_, select

from app.database import District, Subject, engine
from app.enums import Subject as SubjectEnum
from app.schemas import SubjectCompareRequest, SubjectRequest

app = FastAPI()

@app.get('/subjects')
def get_subjects(subject_request: SubjectRequest = Query()):  # noqa: B008
    with Session(engine) as session:

        if subject_request.district:
            statement = (select(Subject).join(District)
                         .where(District.name_slug == subject_request.district)
                         )

        elif subject_request.subject:
            statement = select(Subject).where(Subject.name_slug == subject_request.subject)

        elif subject_request.district is None and subject_request.subject is None:
            statement = select(Subject)

        results = session.exec(statement).all()

        results = {
                   'data':
                   [{'id': row.id,
                    'name': row.name,
                    'name_slug': row.name_slug,
                    'district': row.district
                    }
                    for row in results]
                   }        
             
    return results

@app.get('/subjects/{subject_slug}')
def get_subject(subject_slug: SubjectEnum):
    with Session(engine) as session:
        statement = select(Subject).where(Subject.name_slug == subject_slug)
        result = session.exec(statement).all()

        result = {
                   'data':
                   [{'id': row.id,
                    'name': row.name,
                    'name_slug': row.name_slug,
                    'district': row.district
                    }
                    for row in result]
                   }
             
    return result

@app.get('/subjects/compare')
def get_subjects_compare(subject_compare_request: SubjectCompareRequest = Query()):  # noqa: B008
    with Session(engine) as session:
        
        statement = select(Subject).where(or_(Subject.name_slug == subject_compare_request.first_subject, Subject.name_slug == subject_compare_request.second_subject))
        results = session.exec(statement).all()

        results = {
                   'data':
                   [{'id': row.id,
                    'name': row.name,
                    'name_slug': row.name_slug,
                    'district': row.district
                    }
                    for row in results]
                   }        
             
    return results