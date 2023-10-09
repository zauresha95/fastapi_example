import re
from datetime import date
from pydantic import BaseModel, validator


class SUser(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    birthday: date

    @classmethod
    @validator('email')
    def check_email(cls, v):
        if not re.match('(\w|\.)+\@+[a-zA-Z]+\.[a-zA-Z]+', v):
            raise ValueError('must be mail format')
        return v.title()

    class Config:
        from_attributes = True
