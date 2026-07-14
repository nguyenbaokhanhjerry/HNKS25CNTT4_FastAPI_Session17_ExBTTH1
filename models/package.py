# models/package.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from models.associations import package_truck

class Package(Base):
    __tablename__ = "packages"

    id = Column(Integer, primary_key=True, index=True)
    package_code = Column(String(100), unique=True, nullable=False)
    weight = Column(Float, nullable=False)

    warehouse_id = Column(Integer, ForeignKey("warehouses.id"), nullable=False)

    warehouse = relationship("Warehouse", back_populates="packages")
    
    waybill = relationship("Waybill", back_populates="package", uselist=False)
    
    trucks = relationship("Truck", secondary=package_truck, back_populates="packages")