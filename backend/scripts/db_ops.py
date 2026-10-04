import pandas as pd
from sqlmodel import Session, delete

from app.constants import TABLE_URL
from app.database import engine
from app.models import Subject


def load_data():
    df = pd.read_csv(TABLE_URL, skiprows=[0, 2], na_values='Нет данных')

    df.to_sql(name='subject', con=engine, if_exists='append', index=False)
    
def clear_table():
    with Session(engine) as session:
        statement = delete(Subject)
        session.exec(statement)
        session.commit()