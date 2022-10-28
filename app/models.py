from email.mime import base
from enum import unique
from sqlite3 import IntegrityError
from xmlrpc.client import DateTime
from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.expression import null, text
from sqlalchemy.sql.sqltypes import TIMESTAMP

class Sensors(Base):
    __tablename__= "humidity_sensor_data"

    id = Column(Integer, primary_key=True, nullable=False)
    humidity = Column(Integer, nullable=False)
    temperature = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)

class FruitStatus(Base):
    __tablename__= "ripefruit_status"

    id = Column(Integer, primary_key=True, nullable=False)
    plant_id = Column(Integer, nullable=False)
    plant_status = Column(String, nullable=False)
    fruit_color = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)

class RGV_Location(Base):
    __tablename__="rgv_location"

    id = Column(Integer, primary_key=True, nullable=False)
    rgv_id = Column(Integer, ForeignKey("rgv_status.rgv_id", ondelete="CASCADE"),nullable=False)
    rgv_location = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)

class RGV_Status(Base):
    __tablename__="rgv_status"

    id = Column(Integer, primary_key=True, nullable=False)
    rgv_id = Column(Integer, unique=True, nullable=False)
    rgv_status = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
