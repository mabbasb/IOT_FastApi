from fastapi import *
from pydantic import BaseModel
from . import Schemas, utils
from fastapi import FastAPI, Response, status, HTTPException
from . import models
from .database import engine, get_db, SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import TIMESTAMP
from datetime import datetime
from .routers import post,user,get,authen
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(get.router)
app.include_router(authen.router)

@app.get("/")
def root():
    return ("Welcome to Management System")




