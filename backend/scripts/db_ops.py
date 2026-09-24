from app.database import create_db_and_tables
from scripts.data_normalization import create_salary_scores
from scripts.load_data import import_data

create_db_and_tables()
import_data()
create_salary_scores()