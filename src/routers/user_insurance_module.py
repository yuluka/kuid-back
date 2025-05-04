from typing import Dict, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db.session import SessionLocal
from src.crud import user_insurance_module as uim_crud
from src.schemas.insurance_module import InsuranceModuleOut
from src.schemas.user_insurance_module import UserInsuranceModuleCreate

router = APIRouter(prefix="/user-insurance", tags=["User Insurance Module"])

def get_db():
    db = SessionLocal()

    try:
        yield db
        
    finally:
        db.close()

@router.get("/has-insurance/{user_id}", response_model=bool)
def check_user_has_insurance(user_id: str, db: Session = Depends(get_db)):
    return uim_crud.user_has_insurance_module(db, user_id)

@router.post("/add", response_model=Dict[str, str])
def create_user_insurance_module(association: UserInsuranceModuleCreate, db: Session = Depends(get_db)) -> Dict[str, str]:
    try:
        return uim_crud.add_user_insurance_module(db, association)
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/insurance/{user_id}", response_model=List[InsuranceModuleOut])
def get_user_insurance_modules(user_id: str, db: Session = Depends(get_db)) -> List[InsuranceModuleOut]:
    """
    Get all insurance modules associated with a user.
    """
    try:
        return uim_crud.get_user_insurance_modules(db, user_id)
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))