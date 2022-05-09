from datetime import date

from pydantic import BaseModel


class Question(BaseModel):
    q_id: int
    text: str
    answer: str
    created: date

    class Config:
        orm_mode = True
