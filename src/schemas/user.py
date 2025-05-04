from typing import Optional
from pydantic import BaseModel
from datetime import date

class UserBase(BaseModel):
    name: str
    lastname: str
    email: str
    cellphone: str
    address: str
    birth_date: date

    class Config:
        from_attributes = True

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: str
    score: int

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    name: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[str] = None
    cellphone: Optional[str] = None
    address: Optional[str] = None
    birth_date: Optional[date] = None
    password: Optional[str] = None
    score: Optional[int] = None

    class Config:
        from_attributes = True
