from sklearn.preprocessing import minmax_scale
from sqlmodel import Session, select

from backend.constants import SALARY_FIELDS
from backend.database import Subject, engine


def create_salary_scores():
    with Session(engine) as session:

        for salary_field, score_field in SALARY_FIELDS.items():
            statement = select(getattr(Subject, salary_field))
            results = session.exec(statement)
            data = results.all()
            scores = minmax_scale(data, feature_range=(1, 100)).astype(int).tolist()
            for i, score in enumerate(scores, start=1):
                subject = session.get(Subject, i)
                setattr(subject, score_field, score)

        session.commit()
        session.refresh(subject)


         