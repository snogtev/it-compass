from fastapi import FastAPI

from backend.constants import GRADES

app = FastAPI()

@app.get('/')
def get_home_page():
    return {'сообщение': 'Сайт работает!'}

@app.get('/subjects')
def get_subjects(grade: str):
    if grade not in GRADES:
        return 'Данного грейда не существует!'
    return {'Грейд': f'{grade}'}