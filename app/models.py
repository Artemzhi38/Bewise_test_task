from sqlalchemy import Column, Date, Integer, String

from .db import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    q_id = Column(Integer, unique=True)
    text = Column(String)
    answer = Column(String)
    created = Column(Date)
