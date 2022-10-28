from ..database import get_db
from fastapi import APIRouter
from fastapi import *
from .. import models, oauth2
from fastapi import FastAPI, Response, status, HTTPException
from sqlalchemy.orm import Session


router = APIRouter(prefix = "/get_data", tags=['GET POSTS'])

#GET for RIPE FRUIT STATUS

@router.get("/ripe_fruit_status/{id}")
def get_ripefruitstatus(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):

    data = db.query(models.FruitStatus).filter(models.FruitStatus.plant_id == id).order_by(models.FruitStatus.id.asc()).first()
    
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=("Wrong id or id doesnt exist"))

    return {data.plant_status}


#GET for RGV STATUS

@router.get("/rgv_status/{id}")
def get_rgvstatus(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):

    data = db.query(models.RGV_Status).filter(models.RGV_Status.rgv_id == id).first()

    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=("Wrong id or id doesnt exist"))

    return data.rgv_status


#GET for RGV STATUS

@router.get("/rgv_location/{id}")
def get_rgvstatus(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):

    data = db.query(models.RGV_Location).filter(models.RGV_Location.rgv_id == id).first()

    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=("Wrong id or id doesnt exist"))

    return data.rgv_location


#GET for RGV STATUS AND LOCATION

@router.get("/rgv_status_location/{id}")
def get_rgv_statuslocation(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):

    data = db.query(models.RGV_Status.rgv_status, models.RGV_Location.rgv_location).filter(models.RGV_Status.rgv_id == id, models.RGV_Location.rgv_id == id).first()

    return data