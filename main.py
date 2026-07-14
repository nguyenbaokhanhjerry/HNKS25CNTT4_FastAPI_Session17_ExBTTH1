from fastapi import FastAPI
from database import engine, Base
from routers import package 
from models import associations, warehouse, package as model_package, waybill, truck

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(package.router)