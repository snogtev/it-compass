from sklearn.preprocessing import minmax_scale
from sqlmodel import Session, select

from app.constants import SALARY_FIELDS
from app.database import engine
from app.models import Subject


def create_salary_scores():
    with Session(engine) as session:
        subjects = session.exec(select(Subject)).all()
        
        for salary_field, score_field in SALARY_FIELDS.items():
            raw_data = [getattr(i, salary_field) for i in subjects]
            scores = minmax_scale(raw_data, feature_range=(1, 100)).astype(int).tolist()

            for subject, score in zip(subjects, scores):
                if score > 0:
                    setattr(subject, score_field, score)

        session.commit()