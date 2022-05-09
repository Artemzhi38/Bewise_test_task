from sqlalchemy.orm import Session

from . import models, schemas


def create_question(db: Session, question: schemas.Question):
    db_user = models.Question(
        q_id=question.q_id,
        text=question.text,
        answer=question.answer,
        created=question.created,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def read_last_question(db: Session):
    return db.query(
        models.Question
    ).order_by(models.Question.id.desc()).first()


def get_question_by_q_id(db: Session, q_id: int):
    return db.query(
        models.Question
    ).filter(models.Question.q_id == q_id).first()
