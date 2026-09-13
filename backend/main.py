from fastapi import FastAPI

from backend.constants import DISTRICTS, GRADES

app = FastAPI()

@app.get('/')
def get_home_page():
    return {'сообщение': 'Сайт работает!'}

@app.get('/subjects')
def get_subjects(grade: str, district: str | None = None):
    if grade not in GRADES:
        return 'Данного грейда не существует!'
    if district and district not in DISTRICTS:
        return 'Данного округа не существует!'
    return {'Грейд': grade,
            'Округ': district
            } 