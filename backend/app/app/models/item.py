from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Item(Base):
    id: int = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner: "User" = relationship("User", back_populates="items")


class SnotelStation(Base):
    __tablename__ = "snotel_stations"

    id: int = Column(Integer, primary_key=True)
    name = Column(String)
    lat = Column(Float)
    long =  Column(Float)


class SnotelObservation(Base):
    __tablename__ = "snotel_observations"

    station_id: int = Column(Integer, ForeignKey("snotel_stations.id"), primary_key=True)
    datetime = Column(DateTime(timezone=True), primary_key=True)
    air_temp = Column(Float)
    snow_depth = Column(Float)
    snow_water_eq = Column(Float)


class WxStation(Base):
    __tablename__ = "wx_stations"

    id: int = Column(Integer, primary_key=True)
    name = Column(String)
    lat = Column(Float)
    long = Column(Float)


class WxObservation(Base):
    __tablename__ = "wx_observations"

    station_id: int = Column(Integer, ForeignKey("snotel_stations.id"), primary_key=True)
    datetime = Column(DateTime(timezone=True), primary_key=True)
    air_temp = Column(Float)
    wind_gust = Column(Float)
    wind_direction = Column(Float)
    relative_humidity = Column(Float)
    wind_speed = Column(Float)
    solar_radiation = Column(Float)