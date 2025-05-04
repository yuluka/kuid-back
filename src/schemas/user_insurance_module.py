from pydantic import BaseModel
from typing import Optional

class UserInsuranceModuleBase(BaseModel):
    insurance_module_id: str
    user_id: str

    class Config:
        from_attributes = True

class UserInsuranceModuleCreate(UserInsuranceModuleBase):
    pass

class UserInsuranceModuleOut(UserInsuranceModuleBase):
    status: bool

    class Config:
        from_attributes = True

class UserInsuranceModuleUpdate(BaseModel):
    insurance_module_id: Optional[str] = None
    user_id: Optional[str] = None
    status: Optional[bool] = None

    class Config:
        from_attributes = True