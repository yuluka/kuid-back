from typing import Optional
from pydantic import BaseModel
from datetime import date

class InsuranceModuleBase(BaseModel):
    name: str
    description: str
    monthly_price: float

    class Config:
        from_attributes = True

class InsuranceModuleCreate(InsuranceModuleBase):
    pass

class InsuranceModuleOut(InsuranceModuleBase):
    id: str

    class Config:
        from_attributes = True

class InsuranceModuleUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    monthly_price: Optional[float] = None

    class Config:
        from_attributes = True