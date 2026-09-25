import pandas as pd

from app.constants import TABLE_URL
from app.database import engine


def import_data():
    df = pd.read_csv(TABLE_URL, skiprows=[0, 2], na_values='N/A')

    df.to_sql(name='subject', con=engine, if_exists='append', index=False)