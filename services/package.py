# services/package.py
from sqlalchemy.orm import Session
from models.package import Package
from schemas.package import PackageCreate

def create_package(db: Session, package: PackageCreate):
    db_package = Package(
        package_code=package.package_code,
        weight=package.weight,
        warehouse_id=package.warehouse_id
    )
    db.add(db_package)
    db.commit()
    db.refresh(db_package)
    return db_package

def get_packages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Package).offset(skip).limit(limit).all()