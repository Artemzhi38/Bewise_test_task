from datetime import datetime

import requests
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def format_question(question):
    item = schemas.Question(
        q_id=question["id"],
        text=question["question"],
        answer=question["answer"],
        created=datetime.strptime(
            question["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ"
        ).date(),
    )
    return item


@app.post("/new")
def get_new_questions(
    db: Session = Depends(get_db),
    questions_num: int = 1,
):
    last_question = crud.read_last_question(db)
    if last_question:
        result = schemas.Question(
            q_id=last_question.q_id,
            text=last_question.text,
            answer=last_question.answer,
            created=last_question.created,
        )
    else:
        result = {}

    response = requests.get(
        "https://jservice.io/api/random?count=" + str(questions_num)
    )
    for question in response.json():
        while crud.get_question_by_q_id(db, question["id"]):
            question = requests.get(
                "https://jservice.io/api/random?count=1"
            ).json()[0]
        crud.create_question(db, format_question(question))

    return result
