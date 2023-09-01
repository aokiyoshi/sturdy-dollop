from sqlalchemy import Column, ForeignKey, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Doctor(Base): 
    tablename = 'doctors'
    id = Column(Integer, primary_key=True) 
    name = Column(String)

class Locations(Base): 
    tablename = 'locations'
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    latitude = Column(Float)
    longitude = Column(Float)
    distance = Column(Integer)
    timestamp = Column(Integer)

    doctor = relationship("Doctor", backref="locations")

    engine = create_engine('sqlite:///mydatabase.db', echo=True)