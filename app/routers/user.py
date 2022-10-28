from sys import prefix
from ..database import get_db
from fastapi import APIRouter
from fastapi import *
from .. import Schemas, models, utils
from fastapi import FastAPI, Response, status, HTTPException
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=['Users'])

@router.post("/users/register_new_user", status_code=status.HTTP_201_CREATED, response_model=Schemas.UserOut)
def create_user(user:Schemas.UserCreate, db: Session = Depends(get_db)):
    
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user