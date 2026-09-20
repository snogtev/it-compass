from sklearn.preprocessing import MinMaxScaler
from sqlmodel import Session, select

from backend.database import Subject, engine

scaler = MinMaxScaler(feature_range = (1, 100))


def create_salary_scores():
    with Session(engine) as session:
        data = []
        statement = select(Subject.salary_junior)
        results = session.exec(statement)
        data = results.all()
