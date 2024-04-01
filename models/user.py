from pydantic import BaseModel
from datetime import datetime

class UserModel(BaseModel):
    name: str
    cname: str
    lscore: int
    phone: int
    location: str
    tags: list
    date: datetime

