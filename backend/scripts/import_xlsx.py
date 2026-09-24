import pandas as pd

from backend.constants import TABLE_URL
from backend.database import engine


def import_data():
    df = pd.read_csv(TABLE_URL)

    df.to_sql(name='subject', con=engine, if_exists='append', index=False)