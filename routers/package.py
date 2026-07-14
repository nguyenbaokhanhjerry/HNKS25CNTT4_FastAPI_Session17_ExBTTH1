from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.package import PackageCreate
from services import package as package_service

router = APIRouter(prefix="/packages", tags=["Packages"])

@router.post("/")
def create_package(package: PackageCreate, db: Session = Depends(get_db)):
    return package_service.create_package(db=db, package=package)

@router.get("/")
def read_packages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return package_service.get_packages(db, skip=skip, limit=limit)