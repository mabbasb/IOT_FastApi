from sys import prefix
from ..database import get_db
from fastapi import APIRouter
from fastapi import *
from .. import Schemas, models
from fastapi import FastAPI, Response, status, HTTPException
from sqlalchemy.orm import Session
import io
from starlette.responses import StreamingResponse
import cv2
import shutil
from typing import Union


router = APIRouter(prefix = "/posts", tags=['Posts'])

#POST for sensor datas

@router.post("/sensor_data", status_code=status.HTTP_201_CREATED)
def sensor_data_post(data: Schemas.SensorData, db: Session=Depends(get_db)):

    new_post = models.Sensors(**data.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


#POST for ripe fruit status

@router.post("/ripe_fruit_status", status_code=status.HTTP_201_CREATED)
def ripefruit_status_post(data: Schemas.RipeFruitStatus,db: Session=Depends(get_db)):

    new_post = db.query(models.FruitStatus).filter(models.FruitStatus.plant_id == data.plant_id).first()

    if not new_post:
        new_post = models.FruitStatus(**data.dict())
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
    else:
        db.query(models.FruitStatus).filter(models.FruitStatus.plant_id == data.plant_id).update({"fruit_color" : data.fruit_color})
        db.query(models.FruitStatus).filter(models.FruitStatus.plant_id == data.plant_id).update({"plant_status" : data.plant_status})
        db.commit()

    if not data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return new_post


#POST for RGV STATUS

@router.post("/rgv_status", status_code=status.HTTP_201_CREATED)
def rgv_status_post(data: Schemas.RgvStatus, db: Session=Depends(get_db)):

    new_post = db.query(models.RGV_Status).filter(models.RGV_Status.rgv_id == data.rgv_id).first()

    if not new_post:
        new_post = models.RGV_Status(**data.dict())
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
    else:
        db.query(models.RGV_Status).filter(models.RGV_Status.rgv_id == data.rgv_id).update({"rgv_status" : data.rgv_status})
        db.commit()

    if not data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        
    return {"Done"}


#Post for RGV LOCATION

@router.post("/rgv_location", status_code=status.HTTP_201_CREATED)
def rgv_location_post(data: Schemas.RgvLocation, db: Session=Depends(get_db)):

    new_post = db.query(models.RGV_Location).filter(models.RGV_Location.rgv_id == data.rgv_id).first()

    if not new_post:
        new_post = models.RGV_Location(**data.dict())
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
    else:
        db.query(models.RGV_Location).filter(models.RGV_Location.rgv_id == data.rgv_id).update({"rgv_location" : data.rgv_location})
        db.commit()

    if not data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        
    return {"Done"}

@router.post("/file")
async def create_upload_file(file: Union[UploadFile, None] = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        with open("Resources/destination.jpg", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"filename": file.filename}