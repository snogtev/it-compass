from sklearn.preprocessing import minmax_scale
from sqlmodel import Session, select

from backend.database import Subject, engine


def create_salary_scores():
    with Session(engine) as session:
        statement = select(Subject.salary_junior)
        results = session.exec(statement)
        data = results.all()
        scores = minmax_scale(data, feature_range=(1, 100)).astype(int).tolist()

        for i, score in enumerate(scores, start=1):
            subject = session.get(Subject, i)
            subject.salary_junior_score = score

        session.commit()
        session.refresh(subject)


         