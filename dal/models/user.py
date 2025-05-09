from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    tg_id: int
    dorm: int