from pydantic import BaseModel

class PackageBase(BaseModel):
    package_code: str
    weight: float
    warehouse_id: int

class PackageCreate(PackageBase):
    pass