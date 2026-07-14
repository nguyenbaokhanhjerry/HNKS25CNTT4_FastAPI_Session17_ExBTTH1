from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from models.associations import package_truck

class Truck(Base):
    __tablename__ = "trucks"

    id = Column(Integer, primary_key=True, index=True)
    license_plate = Column(String(50), nullable=False, unique=True)

    packages = relationship("Package", secondary=package_truck, back_populates="trucks")