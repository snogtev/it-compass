import pandas as pd
from sqlmodel import Session, delete, select

from app.constants import TABLE_URL
from app.database import engine
from app.models import District, Subject


def load_data():
    df = pd.read_csv(TABLE_URL, skiprows=[0, 2], na_values='Нет данных')

    df_district = df[['district_name', 'district_slug']].drop_duplicates()
    df_subject = df[['name',
                      'name_slug',
                      'salary_average',
                      'salary_intern',
                      'salary_junior',
                      'salary_middle',
                      'salary_senior',
                      'subsistence_minimum'
                      ]]

    df_district = df_district.rename(columns={
        'district_name': 'name',
        'district_slug': 'name_slug',
    })

    df_district.to_sql(name='district', con=engine, if_exists='append', index=False)

    with Session(engine) as session:
        districts = session.exec(select(District)).all()
        district_mapping = {district.name_slug: district.id for district in districts}

    df_subject['district_id'] = df['district_slug'].map(district_mapping)
        
    df_subject.to_sql(name='subject', con=engine, if_exists='append', index=False)

def clear_table():
    with Session(engine) as session:
        session.exec(delete(Subject))
        session.exec(delete(District))
        session.commit()