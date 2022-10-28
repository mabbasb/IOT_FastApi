from lib2to3.pytree import Base
from turtle import color
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class RipeFruitStatus(BaseModel):
    plant_id:int
    plant_status:str
    fruit_color:str

class SensorData(BaseModel):
    humidity:str
    temperature:str

class RgvLocation(BaseModel):
    rgv_id:int
    rgv_location:str

class RgvStatus(BaseModel):
    rgv_id:int
    rgv_status:str

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode=True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None